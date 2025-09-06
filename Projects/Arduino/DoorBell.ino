const int buttonPin = A4;    // the number of the pushbutton pin
const int buzzerPin = 4;     // the number of the buzzer pin
const int redPin = 11;       // the number of the red LED pin
const int bluePin = 12;      // the number of the blue LED pin
const int greenPin = 13;     // the number of the green LED pin

int buttonState = HIGH;         // variable for reading the pushbutton status

void setup() {
  pinMode(buzzerPin, OUTPUT);
  pinMode(buttonPin, INPUT);
  pinMode(redPin, OUTPUT);
  pinMode(bluePin, OUTPUT);
  pinMode(greenPin, OUTPUT);
}

void loop() {
  buttonState = digitalRead(buttonPin);

  if (buttonState == LOW) {
    // Play tone
    tone(buzzerPin, 2000);
    delay(500);
    noTone(buzzerPin);

    // Flash RGB LED - simple example with red color
    digitalWrite(redPin, HIGH);   // Turn RED LED on
    delay(250);                   // Wait for 250ms
    digitalWrite(redPin, LOW);    // Turn RED LED off
    digitalWrite(greenPin, HIGH); // Turn GREEN LED on
    delay(250);                   // Wait for 250ms
    digitalWrite(greenPin, LOW);  // Turn GREEN LED off
    digitalWrite(bluePin, HIGH);  // Turn BLUE LED on
    delay(250);                   // Wait for 250ms
    digitalWrite(bluePin, LOW);   // Turn BLUE LED off
  }
}
