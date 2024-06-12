#import argparse

from src import actions, utils
import platform
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
import time
import chromedriver_autoinstaller


def selenium_scroll_script(website):
    """Launches Selenium WebDriver, navigates to a website, and records the interaction."""
    print("Launching Selenium WebDriver in full screen...")

    # Setup Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")  # This is important for some versions of Chrome
    chrome_options.add_argument("--remote-debugging-port=9222")  # This is recommended

    if platform.system() == 'Linux':
        chrome_options.binary_location = "/opt/chrome/chrome-linux64/chrome"
        chrome_service = ChromeService(executable_path="/opt/chromedriver/chromedriver-linux64/chromedriver")
    elif platform.system() == 'Darwin':  # macOS
        chromever = chromedriver_autoinstaller.get_chrome_version()
        print(chromever)
        if not chromever:
            chrome_loc = chromedriver_autoinstaller.install()
        else:
            chrome_loc = f'venv/lib/python3.12/site-packages/chromedriver_autoinstaller/{125}/chromedriver'

        chrome_service = ChromeService(executable_path=chrome_loc)
    
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    print("Getting the website")
    # Set up driver
    driver.get(website)
    time.sleep(2)  # Allow some time for the page to load
    print("Stop waiting")
    output_file = utils.format_filename_from_url(website) + ".mp4"
    print(output_file)
    recording_process = utils.start_ffmpeg_recording(output_file)
    time.sleep(3)  # Give a moment before starting interactions

    actions.smooth_scroll_with_pause(driver)  # Perform natural scrolling
    print("Scrolling")
    time.sleep(10)  # Complete the recording duration
    utils.stop_ffmpeg_recording(recording_process)
    driver.quit()

selenium_scroll_script('https://evadvisory.ca')

# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(description='Process a single URL with selenium_scroll_script.')
#     parser.add_argument('url', type=str, help='The URL to process')
#     parser.add_argument('--test', action='store_true', help='Run a test with a predefined URL')

#     args = parser.parse_args()

#     if args.test:
#         selenium_test()
#     else:
#         selenium_scroll_script(args.url)
