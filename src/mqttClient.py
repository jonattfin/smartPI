#!/usr/bin/env python

import paho.mqtt.client as mqtt

class MqttClient:
    def __init__(self, resource, channel = 'RaspberryPi'):
        self.client = mqtt.Client()
        self.client.username_pw_set("token:token")
        self.client.connect("mqtt.beebotte.com", 1883, 60)

        self.channel = channel
        self.resource = resource
        
    def write(self, value):
        try:
            self.client.publish("{0}/{1}".format(self.channel, self.resource), value, 1)
            print(value)
        except Exception:
            pass
            ## Process exception here
            print("Error while writing to Beebotte")
