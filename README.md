
# IoT Automatic Plant Watering System

This project demonstrates an IoT-based automatic plant watering system that uses sensors to monitor soil moisture and temperature. The system waters the plant when the soil moisture is low, ensuring the plant receives optimal care. The project includes both Arduino and Python code, which communicate through serial communication.

## Components Used:
- **Arduino Uno**
- **Soil Moisture Sensor**
- **TMP36 Temperature Sensor**
- **Water Pump**
- **Relay**
- **Jumper wires**
- **Breadboard**

## Project Overview:
The automatic plant watering system automatically detects when the soil is dry and activates a water pump to water the plant. The system uses a soil moisture sensor to measure the moisture level of the soil. If the moisture level falls below a certain threshold, the water pump is turned on to water the plant. The system also measures the temperature with a TMP36 temperature sensor, providing an additional environmental metric.

## Code Breakdown:

### Arduino Code

The Arduino code is responsible for reading the soil moisture and temperature data from the sensors and controlling the water pump based on the soil moisture level. The system uses the following components:

- **Soil Moisture Sensor**: Measures the moisture level of the soil to determine whether the plant needs watering.
- **TMP36 Temperature Sensor**: Measures the temperature of the environment to monitor the conditions.
- **Water Pump**: Activated when the soil moisture falls below a certain threshold, watering the plant.

### Working:
1. The **soil moisture sensor** provides an analog signal, which is read by the Arduino. If the moisture value is below the set threshold (indicating dry soil), the water pump is activated for a specified time (10 seconds).
2. The **TMP36 temperature sensor** provides data about the surrounding temperature, which is useful for monitoring environmental conditions.
3. The data (soil moisture level and temperature) is continuously monitored, and the system will water the plant whenever necessary.

**Usage**:
- Upload the code to an Arduino board and connect the soil moisture sensor, temperature sensor, and water pump according to the circuit diagram.
- Use the Arduino IDE to compile and upload the code.

### Python Code (Tkinter Interface)

The Python code is used to create a graphical user interface (GUI) that allows real-time monitoring of the soil moisture and temperature data from the sensors. It communicates with the Arduino board through serial communication to display sensor readings.

### Working:
1. The Python script uses the **Tkinter** library to create a GUI window, where the sensor data (soil moisture and temperature) is displayed.
2. It establishes a serial connection with the Arduino, reads the data sent from the Arduino, and updates the displayed values every 2 seconds.
3. The **Tkinter GUI** displays the soil moisture level and temperature in a user-friendly format.

**Usage**:
- Install the required libraries by running the following command:
  ```bash
  pip install pyserial





