import serial

# Adjust this to your Arduino's serial port name and baud rate
ser = serial.Serial('COM3', 2400)

try:
    while True:
        # Read a line from serial
        line = ser.readline().decode('utf-8').strip()

        # Convert the comma-separated string to a list of integers
        data = list(map(int, line.split(',')))

        # Print the entire array
        print(data)

except KeyboardInterrupt:
    print("Exiting...")
    ser.close()

'''

Test Result: The Python script outputs [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], as intended.

'''