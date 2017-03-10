from bs4 import BeautifulSoup
import requests

#returns the last 20 tweets from the username entered by the user
#there must be an existing user account for the username entered

name = raw_input("Enter a valid twitter user: ")
if name.startswith('@'):
    name = name[1:]
url = 'https://twitter.com/' + name

r = requests.get(url)

data=r.text
soup = BeautifulSoup(data, "html.parser")

title = soup.title.text
tweets = soup.findAll('div', {'class':'tweet'})
counter = 1
print '\n' + title + '\n'

for tweet in tweets[:20]:
    print str(counter) + '.  ' + tweet.find('p').text + '\n'
    counter += 1
