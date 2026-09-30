import pyautogui
import os
import time
from datetime import datetime

# Folder location on D drive
screenshot_folder = r"D:\Screenshots"

# Create the folder if it doesn't already exist
os.makedirs(screenshot_folder, exist_ok=True)

print("Screenshot folder:", screenshot_folder)

# Take 5 screenshots
for i in range(1, 6):

    # Create a timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Create the screenshot filename
    filename = os.path.join(
        screenshot_folder,
        f"screenshot_{i}_{timestamp}.png"
    )

    # Take screenshot
    pyautogui.screenshot(filename)

    print(f"Screenshot {i} saved: {filename}")

    # Wait 3 seconds
    time.sleep(3)

print("All screenshots completed!")