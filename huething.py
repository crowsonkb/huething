#!/usr/bin/env python3

"""This is a work in progress to control my four Philips Hue bulbs. It does not
currently support many capabilities of the Philips Hue system, but may be useful
as an example or proof of concept.
"""

import argparse
import json
import pprint
import sys

import colour
import requests
from qhue import qhue

#: The first value in each tuple is the brightness scaling to apply. The second
#: value is the mired shift to apply. Light 4 is the reference light because it
#: is a bare bulb. The others need mired shift applied due to lampshades.
SETTINGS = [
    (1.0, -25, True),
    (1.0, -25, True),
    (0.7, -5, True),
    (0.63, 0, True)
]

class State():
    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('-b', '--brightness',
                            help='the brightness scaling factor',
                            default=1, type=float)
        # parser.add_argument('-d', '--debug',
        #                     help='print debug information',
        #                     action='store_true')
        # parser.add_argument('--dry-run',
        #                     help='just print what actions would be taken',
        #                     action='store_true')
        parser.add_argument('--dump',
                            help='dump out complete lighting state',
                            action='store_true')
        parser.add_argument('--host',
                            help='the hostname/ip of the philips hue bridge',
                            default='philips-hue')
        parser.add_argument('-k', '--temperature',
                            help='the color temperature in kelvins',
                            default=4000, type=float)
        parser.add_argument('-t', '--transition-time',
                            help='the transition time in seconds',
                            default=0.4, type=float)
        parser.add_argument('-u', '--username',
                            help='the username to act as when interacting with the bridge',
                            required=True)

        self.args = parser.parse_args()
        self.bridge = qhue.Bridge(self.args.host, self.args.username)

# def request(method, path, data=''):
#     if S.args.debug or S.args.dry_run:
#         sys.stderr.write('{} {} {}\n'.format(method.__name__, path, data))
#     if not S.args.dry_run:
#         response = method(S.endpoint+path, data=data)
#         if S.args.debug:
#             sys.stderr.write('{} {}\n'.format(response.status_code, response.text))
#         return response
#     return None

def main():
    if S.args.dump:
        pprint.pprint(S.bridge())
        return

    for light, setting in enumerate(SETTINGS):
        print(S.bridge.lights[light+1].state(
            transitiontime=int(S.args.transition_time*10),
            on=setting[2],
            bri=min(254, int(S.args.brightness * setting[0] * 254)),
            xy=colour.CCT_to_xy(1e6 / (1e6/S.args.temperature + setting[1]))
        ))

if __name__ == '__main__':
    S = State()
    main()
