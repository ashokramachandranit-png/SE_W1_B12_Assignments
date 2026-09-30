import pyautogui
import time

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 2

# Open Windows Run
pyautogui.hotkey("win", "r")
time.sleep(2)

# Open Chrome with a specific profile
pyautogui.write(
    'chrome.exe --profile-directory="Ashok"'
)
pyautogui.press("enter")

# Wait for Chrome
time.sleep(5)

# Open Google
pyautogui.hotkey("ctrl", "l")
pyautogui.write("https://www.google.com")
pyautogui.press("enter")