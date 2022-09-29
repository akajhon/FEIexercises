// C++ code
//

float tempo, dist;

void setup()
{
  pinMode(3, INPUT);
  pinMode(2, OUTPUT);
  Serial.begin(9600);
}

void loop()
{
  digitalWrite(2, LOW);
  delayMicroseconds(2);
  digitalWrite(2, HIGH);
  delayMicroseconds(10);
  tempo = pulseIn(3, HIGH);
  if(tempo != 0){
  	Serial.println("[+] Tempo = " + String(tempo/1000)+ " segundos");
  	dist = 170 * (tempo/1000000);
  	Serial.println("[+] Distancia = " + String(dist) + " metros" +"\n*****************************");
  	delay(100);
  }
}
