from bs4 import BeautifulSoup
import requests, tweepy, random
import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib.pyplot as plt
from twitter_creds import *
from pandas.io.html import read_html
import urllib.request, urllib
from datetime import date

today = date.today()
today = today.strftime("%B %d, %Y")

url = 'https://www.worldometers.info/coronavirus/coronavirus-death-toll/'
url2 = 'https://www.worldometers.info/coronavirus/'

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
request = urllib.request.Request(url,headers={'User-Agent': user_agent})
request2 = urllib.request.Request(url2,headers={'User-Agent': user_agent})
response = urllib.request.urlopen(request)
response2 = urllib.request.urlopen(request2)
html = response.read()
html2 = response2.read()
pd1 = read_html(html, index_col=False, attrs={'class':'table'})
pd2 = read_html(html2, index_col=False, attrs={'class':'table'})
table1 = pd1[1]
table2 = pd2[0]

# picks needed columns from table 1&2, picks latests updated data
col_cases_24h = table2[table2.columns[2]]
col_deaths_24h = table1[table1.columns[1]]
deaths_24h = f'+{col_deaths_24h[0]}'
cases_24h = col_cases_24h[0].replace(',', '')

# graph
df = pd1[0]
date = df[df.columns[0]]
total = df[df.columns[1]]
fig, ax = plt.subplots()
ax.plot(date, total)
ax.set(ylabel='Deaths', title=f'Total Coronavirus Deaths as of {today}')
plt.xticks(date[::7])
fig.autofmt_xdate()
ax.invert_xaxis()
plt.grid(True, which='major', axis='y')
graph_image = plt.savefig('corona_dtoll_graph.png')
img_path = 'corona_dtoll_graph.png'
#plt.show()

msg = f'''COVID19 New Cases & Deaths as of {today}:

New Cases in last 24 hours: {cases_24h}
Deaths in last 24 hours: {deaths_24h}

#coronavirus #covid19 #CoronaVirusUpdates #COVID_19'''

# posts msg and graph to twitter
def post_deaths_cases_24h():
    api.update_with_media(img_path, msg)
post_deaths_cases_24h()
