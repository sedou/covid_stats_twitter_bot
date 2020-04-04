import requests, tweepy, random
from twitter_creds import *
from pandas.io.html import read_html
url2 = 'https://ourworldindata.org/coronavirus-testing-source-data#'
#url = 'https://ourworldindata.org/coronavirus'

dff = read_html(url2, attrs={'class':''})
both = dff[0][0]
total_tests = dff[0][1]
country = dff[0][0]
date = dff[0][2]
total_tests.pop(0)
country.pop(0)
date.pop(0)
pair = list(zip(country, total_tests, date))
random_country = random.choices(pair, weights=None, cum_weights=None, k=1)

res = [[ i for i, j, k in random_country ], [ j for i, j, k in random_country ], [k for i,j,k in random_country]]
answer = f'''Amount of coronavirus tests done in {res[0]} is {res[1]} as of {res[2]}

#coronavirus #COVID19 #CoronaVirusUpdates #Covid_19'''.replace('[', '').replace(']', '').replace("'", '').replace('nan', 'no data')

def post():
    api.update_status(answer)
post()