from bs4 import BeautifulSoup
import urllib.request

API_KEY = "tSmCWfqzpKOoTFbjKnZdt%2BhrOLxUIM1L4H9pC6sl1E1mCz4SsW4kkTbSMD8deZYJdRQkHXpXmk6Az2are2xSrg%3D%3D"
routeName = ["5100", "9", "7000", "1112", "1560", "M5107"]

busdict = dict()

for i in range(len(routeName)): 
    url = "http://openapi.gbis.go.kr/ws/rest/busrouteservice?serviceKey={0}&keyword={1}".format(API_KEY, routeName[i])
    request = urllib.request.urlopen(url)
    xml = request.read()
    soup = BeautifulSoup(xml, 'html.parser')

    data = soup.find_all('busroutelist')

    for item in data:
        if '수원' in item.find('regionname').text and '용인' in item.find('regionname').text:
            busId = int(item.find("routeid").text)
            busdict[routeName[i]] = busId
            break

file = open('convert_name_to_id.csv', 'w')

for busid, busname in busdict.items():
    file.write(str(busid))
    file.write(",")
    file.write(str(busname))
    file.write('\n')

file.close()

file = open('arrive_time.csv', 'a')

for busname in busdict.keys():
    file.write(',')
    file.write(str(busname))

file.close()


file = open('time_diff.csv', 'a')

for busname in busdict.keys():
    file.write(',')
    file.write(str(busname))
file.close()
