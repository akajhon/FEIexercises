
int det, ldr;
int x = 500;

void setup()
{
  pinMode(A1, INPUT);
  pinMode(2, INPUT);
  pinMode(3, OUTPUT);
  Serial.begin(9600);
}

void loop()
{
  det = digitalRead(2);
  ldr = analogRead(A1);
  Serial.println("Nível do LDR = " + (String)ldr);
  if (det == 1 && ldr < 500){
  	digitalWrite(3, HIGH);
  	delay(2000);
  }
  else{
  	digitalWrite(3, LOW);
  }
  delay(500);
}
