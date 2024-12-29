
import tkinter as tk
import serial
import time

# Setup serial communication (adjust the port and baudrate as per your setup)
arduino = serial.Serial('COM3', 9600)  # Replace 'COM3' with the correct port (Windows) or '/dev/ttyUSB0' (Linux)
time.sleep(2)  # Give time for the Arduino to initialize

# Function to update sensor values from Arduino
def update_sensor_data():
    arduino_data = arduino.readline().decode('utf-8').strip()  # Read data from Arduino
    sensor_data.set(arduino_data)  # Update the label with the data from Arduino
    root.after(2000, update_sensor_data)  # Update every 2 seconds

# Create the main window
root = tk.Tk()
root.title("IoT Automatic Plant Watering System")

# Create a label to display sensor data
sensor_data = tk.StringVar()
label = tk.Label(root, textvariable=sensor_data, font=("Arial", 14), padx=20, pady=20)
label.pack()

# Start the sensor data update function
update_sensor_data()

# Run the Tkinter event loop
root.mainloop()
