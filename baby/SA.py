import random 

ServerURL = 'https://class.iottalk.tw' #For example: 'https://iottalk.tw'
MQTT_broker = 'class.iottalk.tw' # MQTT Broker address, for example:  'iottalk.tw' or None = no MQTT support
MQTT_port = 5566
MQTT_encryption = True
MQTT_User = 'iottalk'
MQTT_PW = 'iottalk2023'

device_model = 'linebot007'
IDF_list = ['linebot_json_i']
ODF_list = ['linebot_json_o']
device_id = '123456789' #if None, device_id = MAC address
device_name = 'web'
exec_interval = 1  # IDF/ODF interval

import requests, json
import config
api_url = f"{config.APP_URL}/get_baby_state" # url to call api for getting baby state

def on_register(r):
    print('Server: {}\nDevice name: {}\nRegister successfully.'.format(r['server'], r['d_name']))

def linebot_json_i():
    # message = read_message()
    # response = requests.get(api_url)
    # response = response.json()["state"]
    # if response:
    #     return message
    # else:
    id = 'A007'
    return {"id": id}

def linebot_json_o(data:list):
    print(data[0])
    return data[0]
