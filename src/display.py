#!/usr/bin/env python

############################################################
# This code uses the Beebotte API, you must have an account.
# You can register here: http://beebotte.com/register
############################################################

from beebotte import *
from beebotteCredentials import BeebotteCredentials

class Display:
    def __init__(self, resource_name, channel_name = 'RaspberryPi'):
        
        (key, secret) = BeebotteCredentials().getKeys()
        bbt = BBT(key, secret)

        self.resource = Resource(bbt, channel_name, resource_name)

    def write(self, value):
        try:
            #Send value to Beebotte
            self.resource.write(value)
            print(value)
        except Exception:
            pass
            ## Process exception here
            print("Error while writing to Beebotte")
