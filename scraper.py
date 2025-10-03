import pandas as pd
import requests
from bs4 import BeautifulSoup
url = "http://quotes.toscrape.com/"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
response = requests.get(url, headers=headers)  
html_text = response.text
soup = BeautifulSoup(html_text, 'html.parser')
all_quotes = soup.find_all('div', class_='quote')
quotes = []
for quote in all_quotes:
  text = quote.find('span', class_='text').text
  author = quote.find('small', class_='author').text
  tags = quote.find_all('a', class_='tag')
  tag_list = [tag.text for tag in tags]
  quotes.append({'text': text, 'author': author, 'tags': tag_list})
df = pd.DataFrame(quotes)
df.to_csv('quotes.csv', index=False)
print(df)  