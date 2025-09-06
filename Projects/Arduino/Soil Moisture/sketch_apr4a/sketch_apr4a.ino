#include <LiquidCrystal.h>  // include the LCD library

// LCD pins: (rs, enable, d4, d5, d6, d7)
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

#define sensorPin A0  // soil moisture sensor connected to analog pin A0

void setup() {
  Serial.begin(9600);      // Start Serial communication
  lcd.begin(16, 2);        // Initialize the LCD (16x2)
  lcd.print("Soil Moisture:"); // Display initial message
}

void loop() {
  int sensorValue = analogRead(sensorPin);

  // Based on your data
  const int dryValue = 1000;
  const int wetValue = 400;
  const int midValue = 569;

  // Map the sensor value to a % (reverse mapping since lower value = wetter)
  int moisturePercent = map(sensorValue, dryValue, wetValue, 0, 100);
  moisturePercent = constrain(moisturePercent, 0, 100);

  // Serial Output
  Serial.print("Analog output: ");
  Serial.print(sensorValue);
  Serial.print(" | Moisture: ");
  Serial.print(moisturePercent);
  Serial.println("%");

  // LCD Output
  lcd.setCursor(0, 1);
  lcd.print("Moisture: ");
  lcd.print(moisturePercent);
  lcd.print("%   "); // spaces clear old digits

  delay(1000);
}

