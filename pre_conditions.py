from bs4 import BeautifulSoup
import requests, tweepy
import numpy as np
import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib.pyplot as plt
from twitter_creds import *

# urls for data
url = 'https://www.worldometers.info/coronavirus/'
age_url = url + 'coronavirus-age-sex-demographics/'

# in this file I haven't used pandas which would be way easier to do
res_age = requests.get(age_url)
soup_age = BeautifulSoup(res_age.content, 'lxml')
table_age_body = soup_age.find_all('tbody')[2]
cardiov = table_age_body.find_all('tr')[1].get_text().split()
cardio = cardiov[2]
diabet = table_age_body.find_all('tr')[2].get_text().split()
diabetes = diabet[1]
hyper = table_age_body.find_all('tr')[4].get_text().split()
hypertension = hyper[1]
resp = table_age_body.find_all('tr')[3].get_text().split()
respiratory = resp[3]
canc = table_age_body.find_all('tr')[5].get_text().split()
cancer = canc[1]

# graph
zero = '0%'
objects = ' ', 'Cancer', 'Respiratory', 'Hypertension', 'Diabetes', 'Cardiovascular'
fig, ax = plt.subplots(figsize=(9,5))
y_pos = np.arange(len(objects))
percentages = [zero, cancer, respiratory, hypertension, diabetes, cardio]
ax.barh(y_pos, percentages, align='center')
ax.set_yticks(y_pos)
ax.set_yticklabels(objects)
ax.invert_yaxis()
ax.set_title('Coronavirus Death Rate For Cases With Pre-existing Condition')
graph_image = plt.savefig('graph_image_pre.png')
#plt.show()

img_path_pre_condition = 'graph_image_pre.png'
msg = f'''Death Rate For Cases With Pre-existing Condition:

Cardiovascular disease: {cardio}
Diabetes: {diabetes}
Chronic respiratory disease: {respiratory}
Hypertension: {hypertension}
Cancer: {cancer}'''

# posts message with bar graph
def post_pre_condition():
    api.update_with_media(img_path_pre_condition, msg)
post_pre_condition()
