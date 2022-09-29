
int gas;

void setup()
{
  pinMode(A0, INPUT);
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  Serial.begin(9600);
}

void loop()
{
  gas = analogRead(A0);
  Serial.println("Nível de Gas = " + (String)gas);
  delay(500);
  if(gas < 310){
  	digitalWrite(6, HIGH);
  	digitalWrite(5, LOW);
  	digitalWrite(4, LOW);
  	digitalWrite(3, LOW);
  	digitalWrite(2, LOW);
  }
  else if(gas < 410){
  	digitalWrite(6, LOW);
  	digitalWrite(5, HIGH);
  	digitalWrite(4, LOW);
  	digitalWrite(3, LOW);
  	digitalWrite(2, LOW);
  }
  else if(gas < 610){
  	digitalWrite(6, LOW);
  	digitalWrite(5, LOW);
  	digitalWrite(4, HIGH);
  	digitalWrite(3, LOW);
  	digitalWrite(2, LOW);
  }
  else{
  	digitalWrite(6, LOW);
  	digitalWrite(5, LOW);
  	digitalWrite(4, LOW);
  	digitalWrite(3, HIGH);
  	digitalWrite(2, HIGH);
  }
}
