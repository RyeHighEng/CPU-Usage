import psutil
import serial
import datetime
import time


ser = serial.Serial("COM3",baudrate=9600, timeout=1) # Make sure this is 9600 or else it won't be able to read it on the arduino.
# print(ser.name)

study = True   
while study is True:
   
    now = datetime.datetime.now()
    curr_time = str(now.strftime("%H:%M:%S"))
    cpu= str(psutil.cpu_percent(interval=1)) + "% "
    # mem = psutil.virtual_memory().percent
    # psutil.virtual_memory().percent
    ser.write(cpu.encode('ascii'))
    # print(f"Serial Buffer: {ser.readline()}")
    time.sleep(1)
    ser.reset_input_buffer()
    print("CPU Usage: ", cpu, "%")
    # time.sleep(2)

    if curr_time < '23:30:00':
        study = True
    else:
        study = False
    

