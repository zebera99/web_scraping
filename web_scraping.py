import requests
from bs4 import BeautifulSoup


response = requests.get('https://workey.codeit.kr/ratings/index')
rating_page = response.text

soup = BeautifulSoup(rating_page, 'html.parser')
program_title = soup.select('td.program')

program_titles = []

for tag in program_title:
    program_titles.append(tag.get_text())

print(program_titles)
