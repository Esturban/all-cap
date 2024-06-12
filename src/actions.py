import time
import random

def smooth_scroll_with_pause(driver):
    """Performs smooth and natural scrolling in the browser window."""
    for _ in range(10):  # 5 gentle scrolls
        for __ in range(20):  # Each scroll is broken down into smaller steps for smoothness
            driver.execute_script("window.scrollBy(0, 10);")  # Small vertical scroll step
            time.sleep(random.uniform(0.01, 0.1))  # Short pause between small steps for a more natural scroll
