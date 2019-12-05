def get_interval_time():
    diff_time_list = []
    count = 0
    
    file = open('time_diff.csv', 'r')
    collect_data = file.readline()

    bus_name = collect_data.strip().split(',')
    bus_name.remove('')

    collect_data = file.readlines()

    for item in collect_data:
        temp = []
        if '2019' in item:
            continue
        else:
            temp = item.strip().split(',')
            for j in range(1,len(temp)):
                if len(diff_time_list) < 6:
                    diff_time_list.append(int(temp[j]))
                else:
                    diff_time_list[j-1] += int(temp[j])
            count = count + 1
            
    for i in range(len(diff_time_list)):
        diff_time_list[i] = diff_time_list[i] // count

    file.close()

    return diff_time_list
    

def get_first_arrive_time():
    arrive_in_resttime = []
    count = 0
    
    file = open('arrive_time.csv', 'r')

    collect_data = file.readline()
    collect_data = file.readlines()

    for item in collect_data:
        temp = []
        if '2019' in item:
            count = count + 1
            continue
        else:
            temp = item.strip().split(',')
            for j in range(1,len(temp)):
                time = temp[j].split(':')
                v_time = int(time[0])*60 + int(time[1])

                if v_time < 600:
                    if len(arrive_in_resttime) < 6:
                        arrive_in_resttime.append([v_time])
                    else:
                        arrive_in_resttime[j-1][0] += v_time
                elif 600 <= v_time < 660:
                    if len(arrive_in_resttime[j-1]) == 1:
                        arrive_in_resttime[j-1].append(v_time)
                    else:
                        arrive_in_resttime[j-1][1] += v_time
                elif 660 <= v_time < 780:
                    if len(arrive_in_resttime[j-1]) == 2:
                        arrive_in_resttime[j-1].append(v_time)
                    else:
                        arrive_in_resttime[j-1][2] += v_time
                elif 780 <= v_time < 840:
                    if len(arrive_in_resttime[j-1]) == 3:
                        arrive_in_resttime[j-1].append(v_time)
                    else:
                        arrive_in_resttime[j-1][3] += v_time
                elif 840 <= v_time < 960:
                    if len(arrive_in_resttime[j-1]) == 4:
                        arrive_in_resttime[j-1].append(v_time)
                    else:
                        arrive_in_resttime[j-1][4] += v_time
                elif 960 <= v_time < 1020:
                    if len(arrive_in_resttime[j-1]) == 5:
                        arrive_in_resttime[j-1].append(v_time)
                    else:
                        arrive_in_resttime[j-1][5] += v_time


    for i in range(len(arrive_in_resttime)):
        for j in range(len(arrive_in_resttime[i])):
            arrive_in_resttime[i][j] //= count
            
    file.close()

    return arrive_in_resttime
