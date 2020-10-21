import serial, time

myESP32 = serial.Serial('COM4', 9600)
time.sleep(2)

while True:
    datos = myESP32.readline().decode('ascii').strip()
    print(datos)