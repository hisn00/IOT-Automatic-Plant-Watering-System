
# IoT Automatic Plant Watering System

This project demonstrates an IoT-based automatic plant watering system using a soil moisture sensor and a relay module to control a water pump. The system checks the soil moisture levels and activates the pump when the soil is dry, ensuring the plant is watered automatically.

## Components Used:
- **Arduino Uno**
- **Soil Moisture Sensor**
- **Relay Module**
- **Water Pump**
- **Jumper wires**
- **Breadboard**
- **Power Source**

## How It Works:
1. The **soil moisture sensor** is placed in the soil to measure its moisture content.
2. The sensor's value is read by the **Arduino Uno**.
3. If the moisture level is below a threshold (indicating dry soil), the **relay module** is triggered to turn on the water pump, watering the plant.
4. Once the soil reaches a sufficient moisture level, the water pump is turned off.

## Circuit Diagram:
You can view the complete circuit diagram and simulation in **Tinkercad**. The soil moisture sensor is connected to an analog input pin, and the relay module is connected to a digital pin on the Arduino.

## How to Use:
1. Clone this repository to your local machine or directly download the files.
2. Open the `plant_watering.ino` file in the **Arduino IDE**.
3. Connect your **Arduino board** and upload the code.
4. Set up the hardware according to the circuit diagram in the Tinkercad simulation or physical setup.
5. Monitor the watering system's behavior based on the moisture level.

## License:
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments:
- Inspired by IoT and automation projects.
- Tinkercad for the circuit simulation.
- Arduino for making DIY electronics easy and fun.




