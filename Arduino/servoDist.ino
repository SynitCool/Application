#include <Servo.h>

Servo servo;

const int echoPin = A0;

const int triggerPin = 13;

void setup() {
  // put your setup code here, to run once:

  pinMode(echoPin, INPUT);

  pinMode(triggerPin, OUTPUT);

  servo.attach(11);
}

void loop() {
  // put your main code here, to run repeatedly:
  turnOnTrigUlt();

  int dist = distanceInp();

  if (dist < 10) greetServo();

  delay(1000);
}

void greetServo() {
  servo.write(0);
  delay(100);
  
  servo.write(180);              
  delay(150);
  servo.write(0);
}

int distanceInp() {
  long duration = pulseIn(echoPin, HIGH);
  return duration * 0.034 / 2;
}

void turnOnTrigUlt() {
  digitalWrite(triggerPin, LOW);  
  delayMicroseconds(2); 
  digitalWrite(triggerPin, HIGH); 
  delayMicroseconds(10);
  digitalWrite(triggerPin, LOW);
}

