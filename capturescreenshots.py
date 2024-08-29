import mss
import time
import os
import re

# time interval between screenshots (in seconds)
interval = 0.1

# directory to save screenshots
output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "trainingimgs")
os.makedirs(output_dir, exist_ok=True)

# function to find the highest numbered screenshot file
def get_last_screenshot_number(output_dir):
    screenshots = [f for f in os.listdir(output_dir) if re.match(r'screenshot_\d+\.png', f)]
    if not screenshots:
        return -1
    last_screenshot = max(screenshots, key=lambda x: int(re.findall(r'\d+', x)[0]))
    return int(re.findall(r'\d+', last_screenshot)[0])

try:
    print("Starting to take screenshots. Press Ctrl+C to stop.")
    # start numbering from the last existing screenshot number + 1
    screenshot_count = get_last_screenshot_number(output_dir) + 1
    with mss.mss() as sct:
        while True:
            monitor = sct.monitors[1]
            screenshot = sct.grab(monitor)
            screenshot_path = os.path.join(output_dir, f"screenshot_{screenshot_count}.png")
            mss.tools.to_png(screenshot.rgb, screenshot.size, output=screenshot_path)
            screenshot_count += 1

            time.sleep(interval)
except KeyboardInterrupt:
    print(f"Stopped taking screenshots. {screenshot_count - get_last_screenshot_number(output_dir) - 1} new screenshots taken.")
