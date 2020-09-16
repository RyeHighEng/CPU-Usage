import psutil
import serial
import datetime

ser = serial.Serial("COM3", 115200, timeout=1)
print(ser.name)
study = True   
while study is True:
    now = datetime.datetime.now()
    curr_time = str(now.strftime("%H:%M:%S"))
    cpu= int(psutil.cpu_percent(interval=1))
    # mem = psutil.virtual_memory().percent
    # psutil.virtual_memory().percent
    ser.write(cpu)
    print("CPU Usage: ", cpu, "%")

    if curr_time < '22:30:00':
        study = True
    else:
        study = False

