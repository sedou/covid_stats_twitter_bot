from pandas.io.html import read_html
from twitter_creds import *
import urllib.request, urllib, random
from datetime import date

today = date.today()
today = today.strftime("%B %d, %Y")

url = 'https://www.worldometers.info/coronavirus/'
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
request = urllib.request.Request(url,headers={'User-Agent': user_agent})
response = urllib.request.urlopen(request)
html = response.read()
pd = read_html(html, index_col=False, attrs={'class':'table'})
df = pd[0]

# picks random row between row 1-120, row 0 is whole world data and rows after 120 dont have much data
rr_ = df.loc[random.randint(1,120)]

# if theres nan result replaces it with no data string
# replaces trailing zero .0 and removes ,
rr = rr_.fillna('no data').astype(str).str.replace('.0', '',regex=False).replace(',', '')

answer = f'''COVID19 Stats for {rr[0]} as of {today}:

Total Cases: {rr[1]}
New Cases: {rr[2]}
Total Deaths: {rr[3]}
New Deaths: {rr[4]}
Total Recovered: {rr[5]}
Active Cases: {rr[6]}
Serious/Critical Cases: {rr[7]}
Total Tests: {rr[10]}
Tests/1M pop: {rr[11]}

#coronavirus #COVID19'''

# posts answer to twitter
def post():
    api.update_status(answer)
post()
