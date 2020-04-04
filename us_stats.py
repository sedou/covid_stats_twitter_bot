import requests, tweepy
import numpy as np
import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib.pyplot as plt
from twitter_creds import *
import urllib
import pandas as pd
from pandas.io.html import read_html
from datetime import date
import datetime

today = date.today()
d2 = today.strftime("%B %d, %Y")

url = 'https://www.worldometers.info/coronavirus/country/us/'
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
request = urllib.request.Request(url,headers={'User-Agent': user_agent})
response = urllib.request.urlopen(request)
html = response.read()

pd = read_html(html, index_col=False, attrs={'class':'table'})
df = pd[0]

today = datetime.datetime.today().strftime('%d-%m-%Y')
df.to_csv(f'us_stats/us_stats_{today}.csv')

state = df['USAState'][:8]
total_cases = df['TotalCases'][:8] #.astype(str)
new_cases = df['NewCases'][:8]
total_deaths = df['TotalDeaths'][:8]
active_cases = df['ActiveCases'][:8]
width = 0.275

r1 = np.arange(len(state)) #index
r2 = [x + width for x in r1]
r3 = [x + width for x in r2]
r4 = [x + width for x in r3]

plt.bar(r2, total_cases, width, color='#003f5c',edgecolor='white', label = 'Total Cases', zorder=3)
plt.bar(r3, active_cases, width, color='#ffa600',edgecolor='white', label = 'Active Cases', zorder=3)
plt.bar(r4, total_deaths, width, color='#ff7c43', edgecolor='white', label = 'Total Deaths', zorder=3)
plt.xticks([x + width for x in range(len(state))], state)
plt.legend(('Total Cases', 'Active Cases', 'Total Deaths'), bbox_to_anchor=(1, 1))
plt.grid(True, which='major', axis='y', linestyle='dashed', zorder=9)
plt.xticks(rotation=18)
plt.yticks(rotation=30)
plt.title(f'Covid19 USA Stats by State on {d2}')
#plt.show()
plt.savefig('us_stats_state.png')
plt.close()

img = '/your_filepath/us_stats_state.png'

msg = f'Covid19 Stats in USA by State on {d2}'

def post():
    api.update_with_media(img, msg)
post()
