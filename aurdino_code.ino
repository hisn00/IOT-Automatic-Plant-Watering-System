#include <DHT.h>

#define DHTPIN 2      
#define DHTTYPE DHT11
#define MOTOR_PIN 8  

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600); 
  dht.begin();        
  pinMode(MOTOR_PIN, OUTPUT);
}

void loop() {
  float temp = dht.readTemperature();

  if (isnan(temp)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }

  Serial.print("Temperature: ");
  Serial.print(temp);
  Serial.println(" *C");

  if (temp > 30.0) {
    digitalWrite(MOTOR_PIN, HIGH);
    Serial.println("Motor ON");
  } else {
    digitalWrite(MOTOR_PIN, LOW); 
    Serial.println("Motor OFF");
  }

  delay(2000);


