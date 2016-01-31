#!/usr/bin/env python3

from urllib.request import urlopen
from lxml import etree
import re
from utils.xmlhelper import etree2dict

class Weather(object):
    def __init__(self,url=None):
        if url is None:
            self.url = "http://meteo.ftj.agh.edu.pl/meteo/meteo.xml"
        else:
            self.url = url
        self.data = None
        self.refresh()

    def refresh(self):
        with urlopen(self.url) as response:
            msg = response.read() 
        tree = etree.fromstring(msg)
        self.data = etree2dict(tree)['meteo']
    #
    def _format(self,data):
        unit = None
        try:
            val = re.match('(-|\d|\.)+',data).group(0)
            unit = data[len(val)+1:]
            val = float(val) 
        except AttributeError:
            val = data
        return {'value' : val,
                'unit'  : unit }

    def basics(self):
        return {'temperature' : self.temperature(),
                'humidity'    : self.humidity(),
                'pressure'    : self.pressure(),
                'windspeed'   : self.windspeed()}

    def temperature(self):
        return self._format(self.data['dane_aktualne']['ta'])

    def humidity(self):
        return self._format(self.data['dane_aktualne']['ua'])

    def windchill(self):
        return self._format(self.data['dane_aktualne']['owindchill'])

    def dewpoint(self):
        return self._format(self.data['dane_aktualne']['odew'])

    def heatindex(self):
        return self._format(self.data['dane_aktualne']['oheatindex'])

    def windspeed(self):
        return self.windspeedavg()

    def windspeedavg(self):
        return self._format(self.data['dane_aktualne']['sm'])

    def windspeedmax(self):
        return self._format(self.data['dane_aktualne']['sx'])

    def winddirection(self):
        return self._format(self.data['dane_aktualne']['dm'])

    def pressure(self):
        return self.pressuresea()

    def pressuresea(self):
        return self._format(self.data['dane_aktualne']['barosealevel'])

    def pressurealt(self):
        return self._format(self.data['dane_aktualne']['pa'])

    def precipitation(self):
        return self._format(self.data['dane_aktualne']['rc'])

    def tendency(self):
        return self.data['dane_aktualne']['tendency']


if __name__ == '__main__':
    #print(Weather().data)
    print(Weather().basics())
