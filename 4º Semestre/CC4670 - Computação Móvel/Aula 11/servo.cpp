#include <Servo.h>

int pot = 0;

Servo servo1;

void setup(){
    servo1.attach(3);
    pinMode(A5, INPUT);
    Serial.begin(9600);
}

void loop(){
    pot = analogRead(A5):
    servo1.write(map(pot, 0, 1023, 0, 180));
    Serial.println("Angulo = " + String(map(pot, 0, 1023, 0, 180));            
}
