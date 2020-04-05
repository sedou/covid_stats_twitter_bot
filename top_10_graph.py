from pandas.io.html import read_html
from matplotlib import pyplot as plt
from twitter_creds import *
import pandas, requests, tweepy
import urllib.request, urllib
import numpy as np
from datetime import date


today = date.today()
d2 = today.strftime("%B %d, %Y")

# this gets dataframe thats needed
url = 'https://www.worldometers.info/coronavirus/'
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
request = urllib.request.Request(url,headers={'User-Agent': user_agent})
response = urllib.request.urlopen(request)
html = response.read()
pd = read_html(html, index_col=False, attrs={'class':'table'})
df = pd[0]

# data
countries = df['Country,Other'][1:11]
total_cases = df['TotalCases'][1:11]
total_deaths = df['TotalDeaths'][1:11]
new_cases = df['NewCases'][1:11]

# graph
index = np.arange(len(countries))
coll = ('#B71C1C', '#E74C3C', '#FF8F00', '#ff7c43', '#f95d6a', '#d45087', '#a05195', '#665191', '#2f4b7c', '#003f5c')

plt.bar(countries, total_cases, color = coll, zorder=3)
plt.grid(True, which='major', axis='y', linestyle='dashed', zorder=9)
plt.rcParams['axes.axisbelow'] = True
plt.ylabel('Total Cases', fontsize=10)
plt.xticks(rotation=25)
plt.yticks(rotation=30)
plt.title(f'Countries With Most Covid19 Cases (CN excl.) on {d2}')
plt.savefig('10countries.png', bbox_inches='tight')
plt.show()
img = '10countries.png'

# message
msg = f'10 Countries With Most Covid19 Cases'

# post to twitter
def post():
    api.update_with_media(img, msg)
post()
