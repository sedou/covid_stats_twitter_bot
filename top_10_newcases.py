from pandas.io.html import read_html
from matplotlib import pyplot as plt
from twitter_creds import *
import tweepy, pandas
import urllib.request, urllib
import numpy as np
from datetime import date
import datetime

# d2 prints todays date when called
today = date.today()
d2 = today.strftime("%B %d, %Y")

# gets dataframe from url
url = 'https://www.worldometers.info/coronavirus/'
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
request = urllib.request.Request(url,headers={'User-Agent': user_agent})
response = urllib.request.urlopen(request)
html = response.read()
pd = read_html(html, index_col=False, attrs={'class':'table'})
df = pd[0]

# stats from first 10 countries
countries = df['Country,Other'][1:11]
total_cases = df['TotalCases'][1:11]
total_deaths = df['TotalDeaths'][1:11]
new_cases = df['NewCases'][1:11]
#first_case = df['1stcase'][1:11]

# different format to save csv
todayy = datetime.datetime.today().strftime('%d-%m-%Y')
df.to_csv(f'data/top_10_newcases_{todayy}.csv')

# graph
index = np.arange(len(countries))
#coll = ('#B71C1C', '#E74C3C', '#FF8F00', '#ff7c43', '#f95d6a', '#d45087', '#a05195', '#665191', '#2f4b7c', '#003f5c')
#coll = ('#ffa600', '#B71C1C', '#E74C3C', '#ff7c43', '#f95d6a', '#d45087', '#a05195', '#665191', '#2f4b7c', '#003f5c')
coll = ('#845EC2','#2C73D2','#0081CF','#0089BA','#008E9B','#008F7A','#00737A','#136473','#265667','#2F4858')
neww = new_cases.fillna('0')
neww = neww.str.replace('+', '')
newww = neww.str.replace(',', '')
newww=newww.astype(int)
newww.sort_values()
plt.bar(countries, newww, color = coll, zorder=3)
plt.grid(True, which='major', axis='y', linestyle='dashed', zorder=9)
plt.ylabel('Amount of New Cases', fontsize=10)
plt.xticks(rotation=25)
plt.yticks(rotation=30)
plt.title(f' Covid19 New Cases Today (CN excl.) on {d2}')
plt.legend(('No bar - No data at the time',), bbox_to_anchor=(0.5, 1), fontsize=8)
plt.savefig('newcasescountries.png', bbox_inches='tight')
#plt.show()

# image path
img = 'newcasescountries.png'

# message
msg = f'Covid19 New Cases Today'

# post to twitter
def post():
    api.update_with_media(img, msg)
post()
