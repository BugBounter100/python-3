import COVID19Py
covid19=COVID19Py.COVID19()
covid19=COVID19Py.COVID19(data_source="csbs")
latest = covid19.getLatest()
# locations = covid19.getLocations(rank_by='recovered')
# print(locations)
# death = covid19.getLocations(rank_by='deaths')
# print (death)
# location = covid19.getLocationByCountryCode("India", timelines=True)
confirm=covid19.getLocations(rank_by="confirmed")
print(confirm)
