// C++ code
//
void setup()
{
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(1, INPUT);
  pinMode(A1, INPUT);
}

void loop()
{
  int pot = analogRead(1);
  int tempo = map(pot, 0, 1023, 3000, 10000);
 
  if(digitalRead(1) == LOW) {
    digitalWrite(4,HIGH);
    digitalWrite(5,LOW);
    digitalWrite(6,LOW);
    digitalWrite(3,HIGH);
    digitalWrite(2,LOW);
  }
  else{
    digitalWrite(4,LOW);
    digitalWrite(5,HIGH);
    delay(3000);
    digitalWrite(5,LOW);
    digitalWrite(6,HIGH);
    digitalWrite(3,LOW);
    digitalWrite(2,HIGH);
    delay(tempo);
    digitalWrite(2, LOW);
    digitalWrite(3, HIGH);
    delay(500);
    digitalWrite(3, LOW);
    delay(500);
    digitalWrite(3, HIGH);
    delay(500);
    digitalWrite(3, LOW);
    delay(500);
  }
}
