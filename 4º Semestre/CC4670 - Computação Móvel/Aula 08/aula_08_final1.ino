// C++ code
//

int pot = 0;

void setup(){
  pinMode(2, INPUT);
  pinMode(A0, INPUT);
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(9, OUTPUT);
  Serial.begin(9600);
}

void loop(){
  pot = analogRead(A0);
  analogWrite(9,pot / 4);
  if(digitalRead(2) == HIGH){
    digitalWrite(3, HIGH);
    digitalWrite(4, LOW);
  }else{
    digitalWrite(3, LOW);
    digitalWrite(4, HIGH);
  }
  Serial.println(pot);
}