huething
========

This is a work in progress to control my four Philips Hue bulbs. It does not currently support many capabilities of the Philips Hue system, but may be useful as an example or proof of concept.

Dependencies
------------

- [Python](https://www.python.org) >= 3.4
- [colour](http://colour-science.org)
- [requests](http://docs.python-requests.org/en/latest/)

Usage
-----
```
usage: huething.py [-h] [-b BRIGHTNESS] [--dump] [--host HOST]
                   [-k TEMPERATURE] [-t TRANSITION_TIME] -u USERNAME

optional arguments:
  -h, --help            show this help message and exit
  -b BRIGHTNESS, --brightness BRIGHTNESS
                        the brightness scaling factor
  --host HOST           the hostname/ip of the philips hue bridge
  -k TEMPERATURE, --temperature TEMPERATURE
                        the color temperature in kelvins
  -t TRANSITION_TIME, --transition-time TRANSITION_TIME
                        the transition time in seconds
  -u USERNAME, --username USERNAME
                        the username to act as when interacting with the
                        bridge
```
