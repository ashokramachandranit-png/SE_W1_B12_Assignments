import pyautogui
import pyperclip
import subprocess
import time
import os
from datetime import datetime


# ============================================================
# CONFIGURATION
# ============================================================

CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

STOCK_URL = "https://finance.yahoo.com/quote/AAPL/"

OUTPUT_FOLDER = r"D:\Daily_Report"

EXCEL_FILE = os.path.join(
    OUTPUT_FOLDER,
    f"daily_report_{datetime.now().strftime('%Y-%m-%d')}.xlsx"
)

SCREENSHOT_FILE = os.path.join(
    OUTPUT_FOLDER,
    f"daily_report_{datetime.now().strftime('%Y-%m-%d')}.png"
)


# ============================================================
# PYAutoGUI SETTINGS
# ============================================================

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 1


# ============================================================
# CREATE OUTPUT FOLDER
# ============================================================

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

print("Output folder:", OUTPUT_FOLDER)


# ============================================================
# STEP 1 - OPEN CHROME
# ============================================================

print("Opening Chrome...")

subprocess.Popen([
    CHROME_PATH,
    STOCK_URL
])

time.sleep(8)


# ============================================================
# STEP 2 - OPEN AAPL STOCK PAGE
# ============================================================

print("Opening AAPL stock page...")

pyautogui.hotkey("ctrl", "l")
pyautogui.write(STOCK_URL)
pyautogui.press("enter")

time.sleep(8)


# ============================================================
# STEP 3 - COPY STOCK PRICE
# ============================================================

print("Copying stock price...")

# Click approximately on the AAPL price
# You may need to adjust this position depending on
# your screen resolution/browser zoom.

pyautogui.click(500, 250)

time.sleep(1)

# Select visible text
pyautogui.hotkey("ctrl", "a")
pyautogui.hotkey("ctrl", "c")

time.sleep(1)

stock_price = pyperclip.paste()

print("Copied data:", stock_price)


# ============================================================
# STEP 4 - OPEN MICROSOFT EXCEL
# ============================================================

print("Opening Microsoft Excel...")

pyautogui.hotkey("win", "r")
time.sleep(2)

pyautogui.write("excel")
pyautogui.press("enter")

time.sleep(8)

print("Excel opened.")


# ============================================================
# STEP 5 - CREATE NEW WORKBOOK
# ============================================================

print("Creating Excel report...")

# New workbook
pyautogui.hotkey("ctrl", "n")

time.sleep(3)


# ============================================================
# STEP 6 - ENTER REPORT DATA
# ============================================================

current_datetime = datetime.now().strftime(
    "%Y-%m-%d %H:%M:%S"
)

comment = "Stock price checked successfully."

# Header row
pyautogui.write("Date & Time")
pyautogui.press("tab")

pyautogui.write("Stock Value")
pyautogui.press("tab")

pyautogui.write("Comment")

pyautogui.press("enter")


# Data row
pyautogui.write(current_datetime)
pyautogui.press("tab")

pyautogui.write(stock_price)
pyautogui.press("tab")

pyautogui.write(comment)


# ============================================================
# STEP 7 - SAVE EXCEL FILE
# ============================================================

print("Saving Excel file...")

pyautogui.hotkey("ctrl", "shift", "s")

time.sleep(3)

# Enter file path
pyautogui.hotkey("ctrl", "a")

pyautogui.write(EXCEL_FILE)

pyautogui.press("enter")

time.sleep(5)

# Handle possible Excel format confirmation
pyautogui.press("enter")

time.sleep(3)


# ============================================================
# STEP 8 - TAKE SCREENSHOT
# ============================================================

print("Taking screenshot...")

screenshot = pyautogui.screenshot()

screenshot.save(SCREENSHOT_FILE)

print("Screenshot saved:", SCREENSHOT_FILE)


# ============================================================
# FINISHED
# ============================================================

print()
print("======================================")
print("Daily report completed successfully!")
print("======================================")
print("Excel file:")
print(EXCEL_FILE)
print()
print("Screenshot:")
print(SCREENSHOT_FILE)