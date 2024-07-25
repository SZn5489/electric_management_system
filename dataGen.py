import random
def getTime(time):
    nowTimeStr = ""
    nowHour = time // 6
    nowMin = time % 6
    if nowHour < 10:
        nowTimeStr += "0" + str(nowHour)
    else:
        nowTimeStr += str(nowHour)
    nowTimeStr += ":"
    if nowMin == 0:
        nowTimeStr += "00"
    else:
        nowTimeStr += str(nowMin * 10)
    nowTimeStr += ":00"
    return nowTimeStr


file_path = "T:/electric_management_system/backend/src/main/resources/static/doc/electric.tbl"
with open(file_path, mode='w', encoding='utf-8') as file_obj:
    index = 1
    for i in range(1, 225):
        time = 0
        while time < 144 :
            date = "2023-04-01 " + getTime(time)
            nowStr = str(index) + "|" + str(i) + "|" + date
            for j in range(3):
                if random.random() < 0.01:
                    nowStr += "|" + "abnormal"
                else:
                    nowStr += "|" + "normal"
            nowStr += "\n"
            file_obj.write(nowStr)
            time += 1
            index += 1
