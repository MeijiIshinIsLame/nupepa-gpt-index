import requests
from bs4 import BeautifulSoup
import time

# Make a request to the website
text_links = []
for i in range(0, 104):
	url = f'https://nupepa.org/gsdl2.5/cgi-bin/nupepa?e=d-0nupepa--00-0-0--010---4-----text---0-1l--1haw-Zz-1---20-about---0003-1-0000utfZz-8-00&a=d&cl=CL2.{i}'
	response = requests.get(url)

	# Parse the HTML content with BeautifulSoup
	soup = BeautifulSoup(response.content, 'html.parser')

	# Find all the links with "text" at the end
	all_links = soup.find_all('a')
	for link in all_links:
		if str(link.get('href')).endswith('=text'):
			text_links.append('https://nupepa.org' + str(link.get('href').strip()))

	# Print out the links
	for link in text_links:
		print(link)
		print()
	time.sleep(2)
	print("-----------------------------------------------")
	print(len(text_links))
	print("-----------------------------------------------")

with open('output.txt', 'w') as f:

    # Iterate over the list and write each string to a new line in the file
	for link in text_links:
		f.write(link + '\n')