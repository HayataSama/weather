##################
# import section #
##################
import requests
import json
import datetime
from threading import Timer
from bs4 import BeautifulSoup


####################
# global variables #
####################
pollution_dict = {}


# gets the pollution rate and adds its value to mylist
def get_pollution():
    now = datetime.datetime.now().strftime("%Y-%m-%d, %H:%M")
    data = requests.get('http://airnow.tehran.ir/')
    soup = BeautifulSoup(data.text, 'html.parser')
    pollution_rate  = soup.find(id="ContentPlaceHolder1_lblAqi3h").text
    pollution_dict[now] = (pollution_rate)

    # appends new pollution data to pollution_data.json file
    with open('pollution_data.json', 'a') as pollution_data:
        json.dump(pollution_dict, pollution_data)
    pollution_dict.clear()
    
    # repeats function every n seconds
    Timer(60, get_pollution).start()



get_pollution()