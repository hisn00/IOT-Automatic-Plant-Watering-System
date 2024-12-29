import tkinter as tk
import random
import time

# Create the main window
root = tk.Tk()
root.title("IoT Automatic Plant Watering System")

# Set the window size
root.geometry("400x300")

# Create labels for temperature, moisture, and watering status
temp_label = tk.Label(root, text="Temperature: -- °C", font=("Arial", 12))
temp_label.pack(pady=10)

moisture_label = tk.Label(root, text="Moisture Level: --%", font=("Arial", 12))
moisture_label.pack(pady=10)

status_label = tk.Label(root, text="Watering system is OFF", font=("Arial", 12))
status_label.pack(pady=20)

# Function to simulate reading from temperature and moisture sensors
def update_sensor_data():
    # Simulate temperature (20 to 30°C)
    temperature = random.randint(20, 30)
    
    # Simulate moisture (0 to 100%)
    moisture = random.randint(0, 100)
    
    # Update the labels with simulated data
    temp_label.config(text=f"Temperature: {temperature} °C")
    moisture_label.config(text=f"Moisture Level: {moisture}%")
    
    # Control the watering system based on simulated data
    if temperature > 25 and moisture < 30:
        status_label.config(text="Watering system is ON")
    else:
        status_label.config(text="Watering system is OFF")

    # Call the function again after 2 seconds to simulate real-time updates
    root.after(2000, update_sensor_data)

# Start the sensor data simulation
update_sensor_data()

# Start the Tkinter event loop
root.mainloop()