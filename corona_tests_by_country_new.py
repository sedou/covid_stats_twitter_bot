import requests, tweepy, random, re
from twitter_creds import *
import bs4

url = 'https://ourworldindata.org/covid-testing'
hashtags = '#coronavirus #COVID19 #CoronaVirusUpdates #Covid_19 #COVID19Pandemic'

res = requests.get(url)
soup = bs4.BeautifulSoup(res.content, 'lxml')

austria = f'''Austria {soup.findAll("p")[61]}

{hashtags}'''
australia = f'''Australia {soup.findAll("p")[58]}

{hashtags}'''
bahrain = f'''Bahrain {soup.findAll("p")[64]}

{hashtags}'''
belgium = f'''Belgium {soup.findAll("p")[67]}

{hashtags}'''
canada = f'''Canada {soup.findAll("p")[70]}

{hashtags}'''
costa = f'''Costa Rica {soup.findAll("p")[73]}

{hashtags}'''
cze = f'''Czechia {soup.findAll("p")[76]}

{hashtags}'''
den = f'''Denmark {soup.findAll("p")[79]}

{hashtags}'''
ecuador = f'''Ecuador {soup.findAll("p")[82]}

{hashtags}'''
est = f'''Estonia {soup.findAll("p")[85]}

{hashtags}'''
fin = f'''Finland {soup.findAll("p")[88]}

{hashtags}'''
fr = f'''France {soup.findAll("p")[91]}

{hashtags}'''
ger = f'''Germany {soup.findAll("p")[94]}

{hashtags}'''
gre = f'''Greece {soup.findAll("p")[97]}

{hashtags}'''
ice = f'''Iceland {soup.findAll("p")[100]}

{hashtags}'''
india = f'''India {soup.findAll("p")[103]}

{hashtags}'''
indo = f'''Indonesia {soup.findAll("p")[109]}

{hashtags}'''
#print(indo)
ire = f'''Ireland {soup.findAll("p")[112]}

{hashtags}'''
italy = f'''Italy {soup.findAll("p")[115]}

{hashtags}'''
japan = f'''Japan {soup.findAll("p")[118]}

{hashtags}'''
lithuania = f'''Lithuania {soup.findAll("p")[121]}

{hashtags}'''
mal = f'''Malaysia {soup.findAll("p")[124]}

{hashtags}'''
nl = f'''Netherlands {soup.findAll("p")[127]}

{hashtags}'''
nz = f'''New Zealand {soup.findAll("p")[130]}

{hashtags}'''
nor = f'''Norway {soup.findAll("p")[133]}

{hashtags}'''
pak = f'''Pakistan {soup.findAll("p")[136]}

{hashtags}'''
phi = f'''Philippines {soup.findAll("p")[139]}

{hashtags}'''
rus = f'''Russia {soup.findAll("p")[142]}

{hashtags}'''
sen = f'''Senegal {soup.findAll("p")[145]}

{hashtags}'''
sin = f'''Singapore {soup.findAll("p")[148]}

{hashtags}'''
sa = f'''South Africa {soup.findAll("p")[154]}

{hashtags}'''
sk = f'''South Korea {soup.findAll("p")[157]}

{hashtags}'''
swe = f'''Sweden {soup.findAll("p")[160]}

{hashtags}'''
swi = f'''Switzerland {soup.findAll("p")[163]}

{hashtags}'''
tw = f'''Taiwan {soup.findAll("p")[166]}

{hashtags}'''
th = f'''Thailand {soup.findAll("p")[169]}

{hashtags}'''
tun = f'''Tunisia {soup.findAll("p")[172]}

{hashtags}'''
tk = f'''Turkey {soup.findAll("p")[175]}

{hashtags}'''
uk = f'''United Kingdom {soup.findAll("p")[178]}

{hashtags}'''
us = f'''United States {soup.findAll("p")[181]}

{hashtags}'''
uru = f'''Uruguay {soup.findAll("p")[187]}

{hashtags}'''
vie = f'''Vietnam {soup.findAll("p")[190]}

{hashtags}'''

# list of all countries to make random choice from
countries = [austria,australia,bahrain,belgium,canada,costa,cze,den,ecuador,est,fin,fr,ger,gre,
ice,india,indo,ire,italy,japan,lithuania,mal,nl,nz,nor,pak,phi,rus,sen,sin,sa,sk,swe,swi,tw,th,tun,
tk,uk,us,uru,vie]

# chooses random country and cleans up the string
random_country = random.choice(countries).replace('<p>', '').replace('<strong>', '').replace('</strong>', '').replace('</p>', '').replace('estimate', 'Estimates').replace('Latest', 'Latest Testing').replace('NA', 'no data')

def post():
    api.update_status(random_country)
post()
