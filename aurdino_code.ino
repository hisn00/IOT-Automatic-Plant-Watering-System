// Arduino Code to Read Temperature and Control Motor
#include <DHT.h>

#define DHTPIN 2      // Pin where the DHT sensor is connected
#define DHTTYPE DHT11 // DHT 11 sensor type
#define MOTOR_PIN 8   // Pin to control the motor

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600); // Initialize Serial Monitor
  dht.begin();        // Start DHT sensor
  pinMode(MOTOR_PIN, OUTPUT); // Set motor pin as output
}

void loop() {
  float temp = dht.readTemperature(); // Read temperature

  // Check if sensor reading is valid
  if (isnan(temp)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }

  Serial.print("Temperature: ");
  Serial.print(temp);
  Serial.println(" *C");

  // Motor control based on temperature
  if (temp > 30.0) {
    digitalWrite(MOTOR_PIN, HIGH); // Turn on motor
    Serial.println("Motor ON");
  } else {
    digitalWrite(MOTOR_PIN, LOW); // Turn off motor
    Serial.println("Motor OFF");
  }

  delay(2000); // Wait 2 seconds before next reading
}


