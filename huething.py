#!/usr/bin/env python

import argparse
import json
import requests

parser = argparse.ArgumentParser()
parser.add_argument('-b', '--brightness',
    help='the brightness scaling factor',
    default=1.0,
    type=float)
parser.add_argument('--host',
    help='the hostname/ip of the philips hue bridge',
    default='philips-hue')
parser.add_argument('-u', '--username',
    help='the username to act as when interacting with the bridge',
    required=True)

args = parser.parse_args()
endpoint = 'http://{}/api/{}'.format(args.host, args.username)

# TODO: check return status code, content, etc. What follows is basically only
# a test.

# Light 4 is the reference light because it is a bare bulb. The others need
# mired shift applied due to lampshades. The desired white point is 4000K.
settings = [(255, 225), (255, 225), (180, 245), (160, 250)]
for index, setting in enumerate(settings):
    url = '{}/lights/{}/state'.format(endpoint, index+1)
    data=json.dumps({'bri': int(setting[0]*args.brightness), 'ct': setting[1]})
    requests.put(url, data=data)

# known good state:
# requests.put(endpoint+'/lights/1/state', data='{"bri":255,"ct":225}')
# requests.put(endpoint+'/lights/2/state', data='{"bri":255,"ct":225}')
# requests.put(endpoint+'/lights/3/state', data='{"bri":180,"ct":245}')
# requests.put(endpoint+'/lights/4/state', data='{"bri":160,"ct":250}')
