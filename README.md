# Flask Quotes Scrapper

## Description
This project is a simple Flask application that provides an API to retrieve data from a SQLite database containing quotes. It also includes a web scraping script to populate the database with quotes from a website.

## Installation
1. Clone the repository:
    ```
    git clone <repository-url>
    ```
2. Install dependencies:
    ```
    pip install -r requirements.txt
    ```

## Usage
1. Run the Flask application:
    ```
    python app.py
    ```
2. Access the API endpoints:
    - Retrieve all quotes: `GET /data`
    - Retrieve a specific quote by ID: `GET /data/<id>`

## Web Scraping
- The `scrape.py` script fetches quotes from [quotes.toscrape.com](https://quotes.toscrape.com/) and inserts them into the SQLite database.

## Technologies Used
- Flask
- SQLite
- Requests
- lxml

## Contributing
Contributions are welcome! Please feel free to submit a pull request.
