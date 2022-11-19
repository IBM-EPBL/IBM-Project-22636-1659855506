#IBM Watson IOT Platform
#pip install wiotp-sdk
import wiotp.sdk.device
import time
import random
import requests, json

myConfig={
    "identity": {
        "orgId": "ctzzci",
        "typeId": "NodeMCU",
        "deviceId": "12345"
        },
        "auth": {
            "token":"oi40wrmfL17BOT4EW-"
            },
}

client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

while True:
    name="Smartbridge"
    #in area location
    #latitude-17.4225176
    #longitude-78.5458842
    #out area location
    latitude=17.4225176
    longitude=78.588783
    myData={'name':name,'lat':latitude,'lon':longitude}
    client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
    print("Published data Successfully: %s", myData)
       
           
    time.sleep(5)
client.disconnect()