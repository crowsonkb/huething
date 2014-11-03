#!/usr/bin/env python

import argparse
import requests

parser = argparse.ArgumentParser()
parser.add_argument('-b', '--bridge',
    help='the hostname/ip of the philips hue bridge',
    default='philips-hue')
parser.add_argument('-u', '--username',
    help='the username to act as when interacting with the bridge',
    required=True)

args = parser.parse_args()
endpoint = 'http://{}/api/{}'.format(args.bridge, args.username)

# TODO: check return status code, content, etc. What follows is basically only
# a test.

# Light 4 is the reference light because it is a bare bulb. The others need
# mired shift applied due to lampshades. The desired white point is 4000K.
requests.put(endpoint+'/lights/1/state', data='{"bri":255,"ct":225}')
requests.put(endpoint+'/lights/2/state', data='{"bri":255,"ct":225}')
requests.put(endpoint+'/lights/3/state', data='{"bri":180,"ct":245}')
requests.put(endpoint+'/lights/4/state', data='{"bri":160,"ct":250}')
