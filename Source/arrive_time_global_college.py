from bs4 import BeautifulSoup
from datetime import datetime
import urllib.request

API_KEY = "tSmCWfqzpKOoTFbjKnZdt%2BhrOLxUIM1L4H9pC6sl1E1mCz4SsW4kkTbSMD8deZYJdRQkHXpXmk6Az2are2xSrg%3D%3D"
stationId = 0

file = open('get_station_id.csv', 'r')

station_data = file.readlines()

for item in station_data:
    item.strip()
    temp = item.split(',')

    if temp[0] == '외국어대학':
        stationId = int(temp[1])
        break
file.close()

file = open('convert_name_to_id.csv', 'r')
route_item = []
route_data = file.readlines()

for item in route_data:
    line = item.strip()
    temp = line.split(',')
    if temp[0] == '5100':
        route_item.append(temp[1])
    elif temp[0] == '1112':
        route_item.append(temp[1])
    elif temp[0] == '9':
        route_item.append(temp[1])
    elif temp[0] == '7000':
        route_item.append(temp[1])
file.close()

url = "http://openapi.gbis.go.kr/ws/rest/busarrivalservice/station?serviceKey={0}&stationId={1}".format(API_KEY, stationId)

request = urllib.request.urlopen(url)
xml = request.read()
soup = BeautifulSoup(xml, 'html.parser')

data = soup.find_all('busarrivallist')

now = datetime.now()

busId = []
remainTime = []
arrivalTime = []
arrivalInfo = dict()

for item in data:
    temp = []
    if item.find("routeid").text in route_item:
        busId.append(int(item.find("routeid").text))
        temp.append(int(item.find("predicttime1").text))
        temp.append(int(item.find("predicttime2").text))
        remainTime.append(temp)

for i in range(len(busId)):
    temp = []
    for j in range(2):
        minute = now.minute + remainTime[i][j]
        hour = now.hour
        if minute >= 60:
            hour += 1
            minute -= 60
        temp.append('%d:%d' %(hour, minute))
    arrivalTime.append(temp)

for i in range(len(busId)):
    arrivalInfo[busId[i]] = arrivalTime[i]

for b_id, time in arrivalInfo.items():
    print(b_id, time)


file = open('arrive_time.csv', 'a')

if now.hour == 8:
    file.write('%d-%d-%d' %(now.year, now.month, now.day))
    file.write('\n')

for i in range(len(arrivalTime)):
    file.write(",")
    file.write(str(arrivalTime[i][0]))
file.close()

