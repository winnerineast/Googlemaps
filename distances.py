# -*- coding: utf-8 -*-
# Read this page before you code
# - https://developers.google.com/maps/documentation/distance-matrix/intro#DistanceMatrixRequests
import googlemaps

gmaps = googlemaps.Client(key='AIzaSyC9TBOkZcAaUnRstNvjbvttreJ3d2PceEU')
f = open('./result.txt', 'w')

origins = ["唐山",
"秦皇岛",
"邯郸",
"邢台",
"保定",
"张家口",
"承德",
"沧州"]
destinations = ["太原",
"大同",
"阳泉",
"长治",
"晋城",
"朔州",
"晋中",
"运城"]

matrix = googlemaps.client.distance_matrix(gmaps,origins, destinations,
                                     mode="driving",
                                     language="zh-CN",
                                     avoid="highways",
                                     units="metric")
i = 0
for element in matrix["rows"]:
    currentOrigins = origins[i]
    j = 0
    for current in element["elements"]:
        print(currentOrigins+" - "+destinations[j]+" = "+current["distance"]["text"])
        f.writelines(currentOrigins+" - "+destinations[j]+" = "+current["distance"]["text"]+"\n")
        f.flush()
        j = j+1
    i = i + 1
f.close()

