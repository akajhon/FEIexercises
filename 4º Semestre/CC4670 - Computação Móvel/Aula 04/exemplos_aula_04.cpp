// C++ code
/*
void setup()
{
  pinMode(3, OUTPUT);
  pinMode(A0, INPUT);
  Serial.begin(9600); //9600 bits por segundo
}

void loop()
{
  int pot = analogRead(0);
  Serial.println(pot);
  digitalWrite(3, HIGH);
  delay(pot);
  digitalWrite(3, LOW);
  delay(pot);
}
*/

// C++ code
/*
void setup()
{
  pinMode(3, OUTPUT);
  pinMode(A0, INPUT);
  Serial.begin(9600); //9600 bits por segundo
}

void loop()
{
  int pot = analogRead(0);
  Serial.println(pot);
  //LED Delay Mínimo = 1s / LED Delay Máximo = 3s
  int tempo = map(pot, 0, 1023, 1000, 3000);
  digitalWrite(3, HIGH);
  delay(tempo);
  digitalWrite(3, LOW);
  delay(tempo);
}
*/
