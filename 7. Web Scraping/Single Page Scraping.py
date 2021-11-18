from urllib.request import urlopen
from bs4 import BeautifulSoup

#Get html page that you want to scrape
html = urlopen('https://treehouse-projects.github.io/horse-land/index.html')
soup = BeautifulSoup(html.read(), 'html.parser')

#print html with indents
print(soup.prettify())

# find all divs and loop through
divs = soup.find_all('div', {'class': 'featured'})
for div in divs:
    print(div)
    
#Use find to find the first instance of an item

#can chain to find child elements
featured_header = soup.find('div', {'class': 'featured'}).h2
#get text - get block of text - use as the last step
print(featured_header.get_text())

for button in soup.find(attrs = {'class': 'button button--primary'}):
    print(button)
    
# quicker option
for button in soup.find(class_= 'button button--primary'):
    print(button)

#Use to get links
for link in soup.find_all('a'):
    print(link.get('href'))
