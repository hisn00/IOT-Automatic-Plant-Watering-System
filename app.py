import tkinter as tk
import serial
import time

# Initialize the GUI
root = tk.Tk()
root.title("Temperature and Motor Control")
root.geometry("400x300")

# Create labels and progress bars
temp_label = tk.Label(root, text="Temperature: -- °C", font=("Arial", 14))
temp_label.pack(pady=20)

motor_label = tk.Label(root, text="Motor Status: OFF", font=("Arial", 14), fg="red")
motor_label.pack(pady=10)

# Serial connection (replace COM3 with your Tinkercad virtual port)
try:
    ser = serial.Serial('COM3', 9600, timeout=1)
    time.sleep(2)  # Allow time for the connection to establish
except:
    ser = None
    temp_label.config(text="Serial Connection Failed", fg="red")

# Update function
def update_gui():
    if ser:
        ser.write(b"r")  # Send a command to Arduino if needed
        data = ser.readline().decode().strip()

        if data:
            try:
                temp, motor_status = data.split(",")
                temp_label.config(text=f"Temperature: {temp} °C")
                
                if motor_status == "ON":
                    motor_label.config(text="Motor Status: ON", fg="green")
                else:
                    motor_label.config(text="Motor Status: OFF", fg="red")
            except:
                pass

    root.after(1000, update_gui)

# Start updating the GUI
update_gui()

# Run the GUI loop
root.mainloop()


