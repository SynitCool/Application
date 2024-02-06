#include <Servo.h>

Servo servo;

const int echoPin = A0;
const int lightPin = 12;
const int triggerPin = 13;
const int buzzPin = 10;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

  pinMode(echoPin, INPUT);

  pinMode(triggerPin, OUTPUT);
  pinMode(lightPin, OUTPUT);
  pinMode(buzzPin, OUTPUT);

  servo.attach(11);
}

void loop() {
  // put your main code here, to run repeatedly:
  turnOnTrigUlt();

  int dist = distanceInp();

  if (dist < 200) {
    turnOnLight();
    greetServo();
    buzz();
  } else {
    backServo();
    turnOffLight();
  }

  Serial.print("Distance: "); 
  Serial.print(dist);  
  Serial.println(" cm");  
  delay(1000);
}

void buzz() {
  for (int i = 0; i <= 10; i++) {
    digitalWrite(buzzPin, HIGH);
    delayMicroseconds(10);
    digitalWrite(buzzPin, LOW);
  }
}

void turnOnLight() {
  digitalWrite(lightPin, HIGH);
  delay(1000);
}
void turnOffLight(){
  digitalWrite(lightPin, LOW);
  delay(1000);
}

void backServo() {
  servo.write(0);
  delay(1000);
}

void greetServo() {
  // for (int i = 0; i <= 180; i++) {
  //   servo.write(i); 
  //   delay(10);
  // }
  servo.write(0);
  delay(1000);
  servo.write(180);
  delay(1000);
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

