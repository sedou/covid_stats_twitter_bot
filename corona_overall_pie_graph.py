# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests, json, pprint, tweepy, threading, random
from matplotlib import pyplot as plt
from twitter_creds import *
from datetime import date


today = date.today()
d2 = today.strftime("%B %d, %Y")

# inneficient method of scraping data
url = 'https://www.worldometers.info/coronavirus/'
res = requests.get(url)
soup = BeautifulSoup(res.content, 'lxml')
total_infected = soup.find('div', class_='maincounter-number').get_text().strip()
deaths = soup.find_all('div', {'class':'maincounter-number'})[1].get_text().strip()
recovered = soup.find_all('div', {'class':'maincounter-number'})[2].get_text().strip()
active_cases = soup.find_all('div', {'class':'number-table-main'})[0].get_text().strip()
serious_cases = soup.find_all('span', {'class':'number-table'})[1].get_text().strip()

# replacing , with blank space
deaths2 = deaths.replace(',', '')
recovered2 = recovered.replace(',', '')
active_cases2 = active_cases.replace(',', '')
serious_cases2 = serious_cases.replace(',', '')
total_infected2 = total_infected.replace(',', '')
mortality = (int(deaths2)/int(total_infected2))*100

# message
message = f'''Total COVID-19 Cases: {total_infected}
Currently Infected: {active_cases}
Recovered: {recovered}
Deaths: {deaths}
Serious or Critical: {serious_cases}

Data scraped from worldometers.info
#coronavirus #COVID19 #CoronaVirusUpdates #Covid_19'''

# graph
labels = 'Currently Infected', 'Recovered', 'Deaths', 'Serious or Critical'
sizes = [active_cases2, recovered2, deaths2, serious_cases2]
explode = (0, 0, 0.3, 0.4)
colors = ('#007CC3','#228B22','#F66D44','#FDBB2F')
fix1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=40, colors=colors)
ax1.axis('equal')
plt.title(f'Covid 19 cases and outcomes on {d2}')
graph_image = plt.savefig('coronagraph.png')
#plt.show()
plt.close(fix1)

img_path = 'coronagraph.png'

# post to twitter
def post_main():
    api.update_with_media(img_path, message)
post_main()
