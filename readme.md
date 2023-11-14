# Data Engineering Assessment

## Project Overview

This project is developed as part of a data engineering assessment to demonstrate the ability to scrape web content programmatically. The script is designed to fetch article titles and URLs from the homepage of a news website and then iteratively scrape the content of each article, handling pagination when necessary.

## Functionality

- The script first scrapes the main page for article titles and URLs.
- It uses the collected URLs to scrape the full text content of each article.
- Pagination is handled automatically, with the script capable of fetching content spread across multiple pages.
- The content is sanitized to avoid issues with file-naming conventions on different operating systems.
- Each article's content is saved as a text file, with the title of the article as the filename.

## Technologies Used

- Python 3
- Libraries: `requests` for HTTP requests, `BeautifulSoup4` for HTML parsing, and `re` for regular expression operations.

## Setup and Execution

1. Ensure Python 3 is installed on your system.
2. Install the required Python packages by running `pip install requests beautifulsoup4`.
3. Clone this repository to your local machine.
4. Navigate to the project directory and run the script with `python main.py`.
5. Scraped articles will be saved in the `articles` directory.

## Project Structure

- `main.py`: The main script that orchestrates the scraping process.
- `articles/`: Directory where the scraped articles are stored as text files.

## Acknowledgments

- Thanks to the `requests` and `BeautifulSoup` communities for providing such powerful tools for web scraping.

## Author

`Rahmadiyan Muhammad`

- Porto: [https://rian.social
- Medium: [https://medium.com/@rianying
- Linkedin: [https://www.linkedin.com/in/rahmadiyanmuhammad/