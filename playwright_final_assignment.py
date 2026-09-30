from playwright.sync_api import sync_playwright
from datetime import datetime
import os

# -----------------------------------
# Settings
# -----------------------------------

URL = "https://www.cricbuzz.com/cricket-match/live-scores"

OUTPUT_FOLDER = r"D:\Cricbuzz_Screenshots"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

today = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

SCREENSHOT_FILE = os.path.join(
    OUTPUT_FOLDER,
    f"cricbuzz_score_{today}.png"
)

# -----------------------------------
# Playwright
# -----------------------------------

with sync_playwright() as p:

    print("Opening Cricbuzz...")

    browser = p.chromium.launch(
        headless=False
    )

    page = browser.new_page(
        viewport={
            "width": 1400,
            "height": 1000
        }
    )

    page.goto(URL, wait_until="domcontentloaded")

    print("Waiting for scores...")
    page.wait_for_timeout(5000)

    # Take screenshot of the page
    print("Taking screenshot...")

    page.screenshot(
        path=SCREENSHOT_FILE,
        full_page=True
    )

    print("Screenshot saved:")
    print(SCREENSHOT_FILE)

    page.wait_for_timeout(3000)

    browser.close()

print("Done.")