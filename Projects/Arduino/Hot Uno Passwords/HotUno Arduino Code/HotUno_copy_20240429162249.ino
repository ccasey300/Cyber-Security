#include <LiquidCrystal.h>
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

int flameSensorPin = A5;
int sensorValue = 0;  // variable to store the value read from the sensor
int buttonPin = 7;
int buttonState = 0;  // variable to store the button state
int lastButtonState = 0;  // variable to store the last button state
bool flameAccess = false;  // Access control based on flame detection
int passwordIndex = 0;  // Index to track the current password

// Array to hold the passwords
const char* passwords[] = {"Reddit - hsdhUWjc23", "Gmail - sgdhd2eBB", "Important:", "CEO is hot", "Flaming hot!"};
int numPasswords = sizeof(passwords) / sizeof(passwords[0]);

void setup() {
  lcd.begin(16, 2);
  // Initialize the serial communication at 9600 bps
  Serial.begin(9600);
  // Set the button pin as input
  pinMode(buttonPin, INPUT);
}

void loop() {
  // Read the analog value from the flame sensor
  sensorValue = analogRead(flameSensorPin);

  // Print the sensor value to the serial monitor
  Serial.print("Sensor Value: ");
  Serial.println(sensorValue);

  // Update access status based on flame sensor
  if (sensorValue < 100) {  // Flame detected
    flameAccess = true;
  }

  // Read the state of the button
  buttonState = digitalRead(buttonPin);

  // If flame access granted, allow scrolling through passwords
  if (flameAccess) {
    if (buttonState == HIGH && lastButtonState == LOW) {
      lcd.clear();
      lcd.setCursor(0, 0);
      lcd.print("Flame Detected!");
      lcd.setCursor(0, 1);
      lcd.print(passwords[passwordIndex]);
      passwordIndex = (passwordIndex + 1) % numPasswords;  // Move to next password
    }
  } else {
    // If no flame detected initially, show neutral message
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("Not suspicious...");
  }

  // Update the last button state
  lastButtonState = buttonState;

  // Delay to help with button debounce
  delay(200);
}
