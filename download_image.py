import sys
from playwright.sync_api import sync_playwright
import requests

if len(sys.argv) < 3:
    print(f"Usage: python {sys.argv[0]} <IMAGE_URL> <OUTPUT_FILE>")
    sys.exit(1)

IMAGE_URL = sys.argv[1]
OUTPUT_FILE = sys.argv[2]

TOKEN = "API KEY HERE"  # Replace with your actual Browserless API token
#IMAGE_URL = "https://www.annalsofoncology.org/cms/10.1016/j.annonc.2021.09.005/asset/e37cdd66-714e-41f5-89bc-db0a8fa60240/main.assets/gr1_lrg.jpg"

# Step 1: Ask Browserless to unblock the URL first

# Browserless opens the target URL in a real browser, handles bot-detection challenges,
# and returns what you ask for — such as HTML, cookies, screenshots, or a live browser WebSocket endpoint

res = requests.post(
    f"https://production-sfo.browserless.io/unblock?token={TOKEN}&proxy=residential",
    json={
        "url": IMAGE_URL,
        "browserWSEndpoint": True, # apart from unblocking, give me a WebSocket URL so I can connect my own Playwright code to that live browser
        "ttl": 60000, # time to live. keeps that browser alive long enough for your script to connect after /unblock finishes
    },
    timeout=120,
)

print("Unblock status:", res.status_code)
print("Unblock response:", res.text[:500])

res.raise_for_status()
ws_endpoint = res.json()["browserWSEndpoint"]

# Step 2: Connect Playwright to the already-unblocked browser
with sync_playwright() as p:
    # Attach Playwright to the already-unblocked browser
    browser = p.chromium.connect_over_cdp(f"{ws_endpoint}?token={TOKEN}") #CDP — Chrome DevTools Protocol
    try:
        # Reuse the existing context/page Browserless already opened
        context = browser.contexts[0]
        page = context.pages[0]

        # Download bytes inside the browser session
        data = page.evaluate("""
            async () => {
                const res = await fetch(window.location.href, {
                    credentials: 'include'
                });
                if (!res.ok) {
                    throw new Error(`HTTP ${res.status}`);
                }
                const buf = await res.arrayBuffer();
                return Array.from(new Uint8Array(buf));
            }
        """)

        with open(OUTPUT_FILE, "wb") as f:
            f.write(bytes(data))

        print(f"Saved {OUTPUT_FILE}")
    finally:
        browser.close()