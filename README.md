# IoT Automatic Plant Watering System

This project demonstrates a smart IoT-based automatic plant watering system that ensures your plants stay hydrated, even when you're away! By utilizing sensors, the system detects soil moisture levels and activates a DC motor to water the plant as needed. The system is powered by an Arduino and is simulated in Tinkercad, allowing for easy testing and modification.

---

### Components Used:

- Arduino Uno: The heart of the system, reading sensor data and controlling the motor.
- Soil Moisture Sensor: Detects the moisture level in the soil, signaling when the plant needs watering.
- TMP36 Temperature Sensor: Measures the temperature of the environment to monitor plant conditions.
- DC Motor: Simulates a water pump, activated when the soil moisture is below the threshold.
- Relay: Acts as a switch to control the DC motor.
- Breadboard & Jumper Wires: Used to connect the components.
- Tinkercad: Used for simulating the entire circuit virtually.

---

### Project Overview:

The IoT Automatic Plant Watering System is designed to monitor the soil moisture level of your plant. It uses a soil moisture sensor to measure how dry or wet the soil is. If the soil is dry, a relay is triggered to power the DC motor (acting as a water pump), watering the plant for a set time.

In addition, the TMP36 temperature sensor is included to monitor environmental conditions. The system ensures the plant gets optimal care by detecting both moisture and temperature levels.

---

### Working:

1. The Soil Moisture Sensor constantly reads the soil's moisture level. If the moisture level is below a predefined threshold, the system activates the DC Motor (simulating watering).
2. The TMP36 Temperature Sensor tracks the temperature of the surrounding environment, offering insights into the plant's climate.
3. The system continuously monitors soil moisture and temperature, keeping your plant happy and healthy!

---

### Code Breakdown:

#### Arduino Code
The Arduino code:
- Reads the soil moisture and temperature sensor data.
- Activates the DC motor when the moisture level is below the threshold.
- Controls the relay to switch the motor on and off.
- Sends data to the Python program for real-time monitoring.

#### Python Code (Tkinter Interface)
The Python code:
- Creates a simple GUI with Tkinter to display real-time soil moisture and temperature data.
- Communicates with the Arduino over serial to receive sensor data.
- Updates the GUI every 2 seconds to reflect the latest data from the sensors.

---

### Setup Instructions:

1. Install Required Software:
   - Install the Arduino IDE to upload the Arduino code.
   - Install Python 3 and the PySerial library to communicate with the Arduino.
    
     pip install pyserial
     
2. Hardware Setup (Tinkercad Simulation):
   - Open Tinkercad and simulate the wiring of the components:
     - Connect the Soil Moisture Sensor to the Arduino.
     - Connect the TMP36 Temperature Sensor to the Arduino.
     - Wire the DC Motor and Relay to the Arduino for controlling the watering.
     - Ensure all components are connected as shown in the circuit diagram.

3. Upload the Arduino Code:
   - Open the Arduino IDE, paste the provided code, and upload it to the Arduino board.

4. Run the Python Script:
   - Run the Python script to monitor real-time soil moisture and temperature data via the GUI.
   `bash
   python water_plant_system.py


---

Screenshots and Visuals:

Tinkercad Simulation:! Description: This screenshot showcases the wiring and components used in the Tinkercad simulation. It includes the Arduino Uno, soil moisture sensor, TMP36 temperature sensor, relay and DC motor providing a visual representation of how everything is connected.

https://github.com/hisn00/IOT-Automatic-Plant-Watering-System/blob/main/Tinkercad%20Simulation.png?raw=true


Circuit Diagram:! Description: This screenshot shows the Tinkercad simulation of the automatic plant watering system. The Arduino Uno is connected to the soil moisture sensor, temperature sensor, and DC motor, which represents the water pump. The system is monitoring the soil moisture and is ready to activate the DC motor when the moisture level is low.

https://github.com/hisn00/IOT-Automatic-Plant-Watering-System/blob/main/Components.png?raw=true




---

Features & Improvements:

Real-Time Monitoring: Display real-time soil moisture and temperature data on a GUI interface.

Automatic Watering: The system waters the plant only when the soil moisture level is below the required threshold.

Energy Efficient: The system ensures minimal energy usage by only activating the motor when necessary.

Temperature Awareness: The TMP36 Temperature Sensor helps in monitoring the temperature, ensuring optimal environmental conditions for the plant.

Customizable Thresholds: Adjust the moisture and temperature thresholds to suit different plant types.

Remote Notifications (Future Work): Implement a notification system to alert the user when watering is required or the temperature is too high/low.



---

Future Improvements:

Smart Notifications: Send alerts to your phone when the soil is dry or the temperature is too high/low.

Watering Schedule: Implement a timer to water plants at regular intervals.

Web Dashboard: Create a web-based dashboard to monitor your plants remotely.

Machine Learning: Integrate machine learning to adjust watering frequency based on historical data.



---

License:

This project is licensed under the MIT License - see the LICENSE file for details.

---

Feel free to copy and paste this Markdown code directly into your GitHub repository's README.md file. This version includes the correct Markdown syntax, headings, and other formatting elements.
