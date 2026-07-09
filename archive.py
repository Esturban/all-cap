import pandas as pd
import run
def process_websites_from_csv(csv_path):
    df = pd.read_csv(csv_path)
    for url in df['url']:
        run.selenium_scroll_script(url)