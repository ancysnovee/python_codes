#Distance using Haversine Formula:

import math
r=6371
latitude1=float(input("enter the latitude of the first city"))
longitude1=float(input("enter the longitude of the first city"))
latitude2=float(input("enter the latitude of the second city"))
longitude2=float(input("enter the longitude of the second city"))
radi_latitude1=math.radians(latitude1)
radi_longitude1=math.radians(longitude1)
radi_latitude2=math.radians(latitude2)
radi_longitude2=math.radians(longitude2)
lat_diff=radi_latitude2-radi_latitude1
long_diff=radi_longitude2-radi_longitude1
a=math.sin(lat_diff/2)**2 + math.cos(radi_latitude1)* math.cos(radi_latitude2)* math.sin(long_diff/2)**2
c=2*math.atan2(math.sqrt(a),math.sqrt(1-a))
d=r*c
print(f"the distance is {d:.2f}km")

