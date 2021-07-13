import pprint
import COVID19Py as covid

covid19 = covid.COVID19()

def c(command, location):
    if location == None:
        latest = (covid19.getLocations(rank_by = command))
        return (str(f'`{pprint.pformat(str(latest))}')[0:1998] + '`')
    else:
        place = covid19.getLocationByCountryCode(location)
        return (str(f'`{pprint.pformat(place, indent = 2)}`'))
