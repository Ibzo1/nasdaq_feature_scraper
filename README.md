# nasdaq_feature_scraper
This repository contains Python scripts for scraping various types of data from Nasdaq, including short interest, options chain, and institutional investors for specific stocks.


INSTRUCTIONS:

## Requirements

- Python 3.x
- Firefox Browser
- GeckoDriver

## Installation

1. Ensure you have Python 3 installed on your system.

2. Clone this repository:
    run: "git clone https://github.com/yourusername/nasdaq-data-scraper.git"

3. Navigate to the cloned directory:
    run: "cd nasdaq-data-scraper"

4. Install required Python libraries in main directory:
    run: "pip install -r requirements.txt"


5. Make sure you have Firefox installed. If not, download and install it from [Mozilla Firefox](https://www.mozilla.org/en-US/firefox/new/).

6. Download GeckoDriver from [GitHub](https://github.com/mozilla/geckodriver/releases) and ensure it's in your system's PATH or specify its path in the scripts.

## Usage

Run `main.py` with the desired ticker symbol to scrape data from Nasdaq:
Replace `<ticker_symbol>` with the actual stock ticker (e.g., `TSLA` for Tesla).

## Caution

This tool scrapes data from Nasdaq's website, which may change its layout or URL structure. Ensure the scripts are up to date with these changes.

## Contributing

Feel free to fork this project, make changes, and submit pull requests. Your contributions are welcome!

## License

This project is open-source and available under the [MIT License](LICENSE).



