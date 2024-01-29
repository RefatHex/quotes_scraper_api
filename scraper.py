import requests
from lxml import html
import sqlite3

connection = sqlite3.connect('db.sqlite3')
cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS quotes(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        quote TEXT,
        author TEXT
    )''')
connection.commit()

def scrape(link):
    r = requests.get(link)
    response = html.fromstring(r.content)

    containers = response.xpath('//div[@class="quote"]')
    print(r.status_code)

    for container in containers:
        quote = container.xpath('.//span[@class="text"]/text()')
        quote = quote[0] if quote else ''

        author = container.xpath('.//span[@class="author"]/text()')
        author = author[0].replace("'", "''") if author else ''

        # Use parameterized query to insert data
        cursor.execute('''
            INSERT INTO quotes(quote, author) VALUES(?, ?)
        ''', (quote, author))

        connection.commit()
        print(quote, author)

link = 'https://quotes.toscrape.com/'
scrape(link)

connection.close()
