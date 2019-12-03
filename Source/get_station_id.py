from bs4 import BeautifulSoup
import urllib.request

API_KEY = "tSmCWfqzpKOoTFbjKnZdt%2BhrOLxUIM1L4H9pC6sl1E1mCz4SsW4kkTbSMD8deZYJdRQkHXpXmk6Az2are2xSrg%3D%3D"

# 정류소 정보를 얻기 위해서는 노선 ID가 필요하므로 이를 open
file = open('convert_name_to_id.csv', 'r')
data = file.readlines()
busId = 0
stationDict = dict()

# 경희대정문, 외국어 대학을 모두 지나는 버스 중 하나를 선택 (여기서는 5100번 버스)
for item in data:
    item.strip()
    if '5100' in item:
        temp = item.split(',')
        busId = int(temp[1])
        break
file.close()

# 경유하는 정류소 ID를 획득하기 위해 노선정보 조회 서비스 API 사용
url = "http://openapi.gbis.go.kr/ws/rest/busrouteservice/station?serviceKey={0}&routeId={1}".format(API_KEY, busId)

# 요청을 받은 후 이를 파싱하기 위해 BeautifulSoup 모듈 사용
request = urllib.request.urlopen(url)
xml = request.read()
soup = BeautifulSoup(xml, 'html.parser')

station_data = soup.find_all('busroutestationlist')

# 정류소의 ID를 dictionary에 넣기 위해 수행하는 반복문
for item in station_data:
    if item.find("stationname").text == "경희대정문":
        stationDict["경희대정문"] = int(item.find("stationid").text)
    elif item.find("stationname").text == "외국어대학":
        stationDict["외국어대학"] = int(item.find("stationid").text)

# 받아온 dictionary를 파일에 쓰기
file = open('get_station_id.csv', 'w')

for s_name, s_id in stationDict.items():
    file.write(s_name)
    file.write(',')
    file.write(str(s_id))
    file.write('\n')

file.close()
