#!/usr/bin/env python

############################################################
# This code uses the Beebotte API, you must have an account.
# You can register here: http://beebotte.com/register
############################################################

from beebotte import *

class Display:
    def __init__(self, resource_name, channel_name = 'RaspberryPi'):
        ### Replace API_KEY and SECRET_KEY with those of your account
        bbt = BBT('API_KEY', 'SECRET_KEY')
        self.resource = Resource(bbt, channel_name, resource_name)

    def write(self, value):
        try:
            #Send value to Beebotte
            resource.write(value)
        except Exception:
            pass
            ## Process exception here
            print("Error while writing to Beebotte")
