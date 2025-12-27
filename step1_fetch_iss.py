import requests
 
TLE_URL="https://celestrak.com/NORAD/elements/stations.txt"

response=requests.get(TLE_URL)
tle_data=response.text.splitlines()

name=tle_data[0]
line1=tle_data[1]
line2=tle_data[2]

print("Name:", name)
print("Line 1:",line1)
print("Line 2:",line2)