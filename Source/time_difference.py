from bs4 import BeautifulSoup
from datetime import datetime
import urllib.request

API_KEY = "발급받은 API 키"
stationId1 = 228000710
stationId2 = 228000723

url1 = "http://openapi.gbis.go.kr/ws/rest/busarrivalservice/station?serviceKey={0}&stationId={1}".format(API_KEY, stationId1)
url2 = "http://openapi.gbis.go.kr/ws/rest/busarrivalservice/station?serviceKey={0}&stationId={1}".format(API_KEY, stationId2)

request1 = urllib.request.urlopen(url1)
xml1 = request1.read()
soup1 = BeautifulSoup(xml1, 'html.parser')

request2 = urllib.request.urlopen(url2)
xml2 = request2.read()
soup2 = BeautifulSoup(xml2, 'html.parser')

data1 = soup1.find_all('busarrivallist')
data2 = soup2.find_all('busarrivallist')
now = datetime.now()

current_time = '{0}:{1}'.format(now.hour, now.minute)

time_difference_list = []

for item in data1:
    time1 = int(item.find("predicttime1").text)
    time2 = int(item.find("predicttime2").text)
    difference = time1
    time_difference_list.append(difference)

for item in data2:
    if item.find("routeid").text == '234001243':
        time1 = int(item.find("predicttime1").text)
        time2 = int(item.find("predicttime2").text)
        difference = time1
        time_difference_list.append(difference)
    elif item.find("routeid").text == '234000884':
        time1 = int(item.find("predicttime1").text)
        time2 = int(item.find("predicttime2").text)
        difference = time1
        time_difference_list.append(difference)

file = open('time_diff.csv', 'a')

if now.hour == 8:
    file.write('%d-%d-%d' %(now.year, now.month, now.day))
    file.write('\n')

file.write(current_time)

for i in range(len(time_difference_list)):
    file.write(',')
    file.write(str(time_difference_list[i]))
file.write('\n')

file.close()
