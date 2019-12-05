import calculate_collect_time
import matplotlib.pyplot as plt
import numpy as np

interval_list = calculate_collect_time.get_interval_time()
first_arrive_list = calculate_collect_time.get_first_arrive_time()

predict_arrive_time = []
arrive_count_bus = []
arrive_count_time = [0]*len(first_arrive_list[0])
    
for i in range(len(interval_list)):
    temp = []
    for j in range(len(first_arrive_list[i])):
        time = first_arrive_list[i][j]
        temp.append(first_arrive_list[i][j])
        cnt = 0
        while True:
            cnt = cnt + 1
            if interval_list[i]*cnt >= 15:
                break
            time += interval_list[i]
            temp.append(time)
    predict_arrive_time.append(temp)


for i in range(len(predict_arrive_time)):
    count = 0
    for j in range(len(predict_arrive_time[i])):
        time = predict_arrive_time[i][j]

        if time//60 == 8 and 45 <= time%60 <= 59:
            count = count + 1
            arrive_count_time[0] += 1
        elif time//60 == 10 and 15 <= time%60 <= 29:
            count = count + 1
            arrive_count_time[1] += 1
        elif time//60 == 11 and 45 <= time%60 <= 59:
            count = count + 1
            arrive_count_time[2] += 1
        elif time//60 == 13 and 15 <= time%60 <= 29:
            count = count + 1
            arrive_count_time[3] += 1
        elif time//60 == 14 and 45 <= time%60 <= 59:
            count = count + 1
            arrive_count_time[4] += 1
        elif time//60 == 16 and 15 <= time%60 <= 29:
            count = count + 1
            arrive_count_time[5] += 1
    arrive_count_bus.append(count)

print(arrive_count_bus)
print(arrive_count_time)


bus_info = ['5100', '9', '7000', '1112', '1560', 'M5107']
rest_info = ['8:45', '10:15', '11:45', '13:15', '14:45', '16:15']

opacity = 0.4
bar_width = 0.5

plt.xlabel('Bus')
plt.ylabel('Arrive Count')
plt.title('Each Bus Arrive Count at Resttime')

plt.xticks([i+0.5 for i in range(len(bus_info))], bus_info)
bar = plt.bar(np.arange(len(arrive_count_bus)) + bar_width, arrive_count_bus, bar_width, color='blue')

for rect in bar:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width()/2.0, height, '%d' % int(height), ha='center', va='bottom') 

plt.show()

plt.xlabel('Rest Time')
plt.ylabel('Arrive Count')
plt.title('Arrive Count at Resttime')

plt.xticks([i+0.5 for i in range(len(rest_info))], rest_info)
bar = plt.bar(np.arange(len(arrive_count_time)) + bar_width, arrive_count_time, bar_width, color='orange')

for rect in bar:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width()/2.0, height, '%d' % int(height), ha='center', va='bottom') 

plt.show()
