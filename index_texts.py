import requests
from bs4 import BeautifulSoup
import time


import sqlite3

# Connect to the database (creates the file if it doesn't exist)
conn = sqlite3.connect('hawaiian_newspaper.db')

# Create a cursor to execute SQL commands
c = conn.cursor()

# Create the text_entries table with the specified columns
c.execute('''CREATE TABLE IF NOT EXISTS text_entries (base_link text, title text, page_number int, page_link text, contents text)''')

# Commit the changes and close the connection
conn.commit()
conn.close()

links = [line.strip() for line in open('output.txt', 'r')]

for url in links:
	time.sleep(2)
	i = 1
	base_url = url
	next_url = base_url
	while True:
		print(next_url)
		page = requests.get(next_url)
		soup = BeautifulSoup(page.content, 'html.parser')
		links = soup.find_all('a')
		link = ""

		for the_link in links:
			if "ʻaoʻao aʻe" in the_link.text:
					link = the_link
		try:
			body_text = soup.find('div', {'class': 'Section1'}).text
			title = soup.find('h3').text.split('\n')[0]

			conn = sqlite3.connect('hawaiian_newspaper.db')
			c = conn.cursor()
			c.execute("INSERT OR REPLACE INTO text_entries VALUES (?, ?, ?, ?, ?)", (base_url, title, i, next_url, body_text))
			conn.commit()
			conn.close()
		except Exception as e:
			print(e)

		if link == "":
			break

		next_url = "https://nupepa.org" + link['href']
		i += 1
		time.sleep(2)
	print("-------------------REACHED END OF", base_url, "at", i, "pages----------------------")
	print()