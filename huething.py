#!/usr/bin/env python

import argparse
import colour
import json
import requests
import sys

parser = argparse.ArgumentParser()
parser.add_argument('-b', '--brightness',
    help='the brightness scaling factor',
    default=1.,
    type=float)
parser.add_argument('-d', '--debug',
    help='print debug information',
    action='store_true')
parser.add_argument('--host',
    help='the hostname/ip of the philips hue bridge',
    default='philips-hue')
parser.add_argument('-k', '--temperature',
    help='the color temperature in kelvins',
    default=4000.,
    type=float)
parser.add_argument('-u', '--username',
    help='the username to act as when interacting with the bridge',
    required=True)

args = parser.parse_args()
endpoint = 'http://{}/api/{}'.format(args.host, args.username)

def request(method, path, data=''):
    if args.debug:
        sys.stderr.write('{} {} {}\n'.format(method.func_name, path, data))
    response = method(endpoint+path, data=data)
    if args.debug:
        sys.stderr.write('{} {}\n'.format(response.status_code, response.text))
    return response

# The first value in each tuple is the brightness scaling to apply. The second
# value is the mired shift to apply. Light 4 is the reference light because it
# is a bare bulb. The others need mired shift applied due to lampshades.
settings = [
    (1.0, -25),
    (1.0, -25),
    (0.7, -5),
    (0.63, 0)
]

computed_params = []
for setting in settings:
    bri = min(255, int(args.brightness * setting[0] * 255))
    ct = 1000000. / (1000000./args.temperature + setting[1])
    computed_params.append({'bri': bri, 'xy': colour.CCT_to_xy(ct)})

for index, param in enumerate(computed_params):
    path = '/lights/{}/state'.format(index+1)
    data = json.dumps(param)
    request(requests.put, path, data)
