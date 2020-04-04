from bs4 import BeautifulSoup
import requests, random, urllib
import tweepy
import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib.pyplot as plt
from twitter_creds import *
from pandas.io.html import read_html

url = 'https://www.worldometers.info/coronavirus/'
countries_url = url +'#countries'
res_new_stats = requests.get(countries_url)
soup_new_stats = BeautifulSoup(res_new_stats.content, 'html.parser')

table_body = soup_new_stats.find_all('tbody')[1]
cases_24h = table_body.find_all('td')[2].get_text()
deaths_24h = table_body.find_all('td')[4].get_text()

urld = 'https://www.worldometers.info/coronavirus/coronavirus-death-toll/'
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
request = urllib.request.Request(urld,headers={'User-Agent': user_agent})
response = urllib.request.urlopen(request)
html = response.read()

#urld = 'https://www.worldometers.info/coronavirus/coronavirus-death-toll/'
pd = read_html(html, index_col=False, attrs={'class':'table'})
df = pd[0]
date = df[df.columns[0]]
total = df[df.columns[1]]
fig, ax = plt.subplots()
ax.plot(date, total)
ax.set(ylabel='Deaths', title='Total Coronavirus Deaths')
plt.xticks(date[::7])
fig.autofmt_xdate()
ax.invert_xaxis()
plt.grid(True, which='major', axis='y')
#ax.legend(['Deaths'], loc='upper left')
graph_image = plt.savefig('corona_dtoll_graph.png')
img_path = '/home/mongo/Desktop/corona_stats_bot/corona_dtoll_graph.png'
plt.show()

msg = f'''Coronavirus Deaths & New Cases Today:

Deaths in last 24 hours: {deaths_24h}
New Cases in last 24 hours: {cases_24h}'''

def post_deaths_cases_24h():
    api.update_with_media(img_path, msg)
post_deaths_cases_24h()
