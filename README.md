# Kasper Scrapy UEL

This project is a Scrapy-based web scraper designed to extract course information from the University of East London's website.

## Project Structure

- **scraper.py**: The main spider file that handles the scraping process.
- **items.py**: Defines the data structure for storing scraped data.
- **uel.csv**: Contains the list of URLs to scrape.

## Complexities and Solutions

### Data Extraction
- **Complexity**: Extracting various pieces of course information such as fees, intake dates, course duration, and requirements using CSS selectors and XPath.
- **Solution**: Utilizes robust CSS selectors and XPath expressions to accurately locate and extract the required information.
- **Challenge**: Handling missing or inconsistent data fields.
- **Outcome**: Implemented try-except blocks and conditional checks to manage missing data gracefully.

### Data Structuring
- **Complexity**: Structuring the extracted data into a well-defined format for further processing.
- **Solution**: Uses the `KasperItem` class to structure the data, ensuring consistency.
- **Challenge**: Ensuring that all relevant data fields are populated correctly.
- **Outcome**: Defined clear item fields and used appropriate data extraction techniques to populate them.

### URL Handling
- **Complexity**: Managing and iterating over a list of URLs to scrape.
- **Solution**: Reads URLs from a CSV file and uses Scrapy's `start_requests` method to initiate scraping.
- **Challenge**: Ensuring that all URLs are correctly formatted and accessible.
- **Outcome**: Successfully reads and processes URLs, logging each URL being scraped for transparency.

## How to Run the Project

1. Clone the repository:
   ```sh
   git clone https://github.com/faisal-fida/kasper_scrapy_uel.git
   ```
2. Navigate to the project directory:
   ```sh
   cd kasper_scrapy_uel
   ```
3. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Run the Scrapy spider:
   ```sh
   scrapy crawl scraper
   ```

## Conclusion

This project demonstrates the complexities of web scraping, from data extraction and structuring to handling URLs and missing data. It provides a robust solution for scraping course information, with potential for further enhancements and scalability.
