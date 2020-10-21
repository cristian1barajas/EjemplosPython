import serial # pip install pyserial

ser = serial.Serial('COM4')  # open serial port
print(ser.name)         # check which port was really used
ser.write(b'hello')     # write a string
ser.close()             # close port