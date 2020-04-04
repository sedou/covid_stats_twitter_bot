from pandas.io.html import read_html
from matplotlib import pyplot as plt
from twitter_creds import *
import tweepy, pandas, requests
import urllib.request, urllib

url = 'https://www.worldometers.info/coronavirus/coronavirus-cases/#total-cases'
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
request = urllib.request.Request(url,headers={'User-Agent': user_agent})
response = urllib.request.urlopen(request)
html = response.read()
pd = read_html(html, index_col=False, attrs={'class':'table'})
df = pd[0]
cur_infected = df[0][1].replace(',', '')
mild = df[0][3].replace(',', '').split()
serious = df[0][5].replace(',', '').split()
mild_pie = mild[0]
serious_pie = serious[0]

labels = 'Mild Cases', 'Serious or Critical Cases'
sizes = [mild_pie, serious_pie]
explode = (0,  0.3)
colors = ('#007CC3','#F66D44')
fix1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, autopct='%1.1f%%', shadow=True, startangle=40, colors=colors, textprops={'fontsize': 12})
ax1.axis('equal')
plt.legend(labels, bbox_to_anchor=(0.6, 0.9))
graph_image = plt.savefig('condition_pie.png', bbox_inches='tight')
#plt.show()
plt.close(fix1)
img_path = '/yourfilepath/condition_pie.png'
msg = f'''Currently infected patients: {df[0][1]}

{df[0][3]} are in mild condition
{df[0][5]} are in serious or critical condition.'''

def post():
    api.update_with_media(img_path, msg)
post()
