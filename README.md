# Web Scraping with Concurrency

### Description
This project demonstrates how to use multithreading to perform web scraping efficiently. It scrapes multiple web pages concurrently, collects specific data (article titles), and stores the results in a CSV file. The use of threads speeds up the process of scraping by handling multiple requests at the same time.

### Features
- The script will send HTTP requests to several URLs 
- Concurrency: Uses multithreading to scrape multiple pages simultaneously, improving the efficiency of the web scraping process.
- Data Extraction: Extracts specific data (e.g., titles) from each page using BeautifulSoup.
- Results Storage: Saves the extracted data into a CSV file for easy access and analysis.
- Error Handling: The script handles errors gracefully and continues scraping even if some pages fail.

### Requirements
Before running the script, make sure you have the following installed:
- Python 3.x (version 3.6 or higher is recommended)
  
Required Python Libraries:
- requests: For sending HTTP requests.
- beautifulsoup4: For parsing HTML pages.
- threading: For multithreading support.
  
### How to use
- Update the urls list in the script to include the pages you want to scrape.
- Run the script: python app.py

### Example Output
![image](https://github.com/user-attachments/assets/b4618dda-5107-426c-b921-bc3a8cb7d4cd)
