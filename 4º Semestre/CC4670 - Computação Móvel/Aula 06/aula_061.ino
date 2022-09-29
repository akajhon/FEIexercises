// C++ code
//

int buzzer = 10;
float tempo = 0;
float distancia;
int led_verde = 12;
int led_vermelho = 13;

void setup()
{
  pinMode(13, OUTPUT);
  pinMode(12, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(2, INPUT);
}

void loop()
{
  digitalWrite(3, HIGH);
  delayMicroseconds(2); 
  digitalWrite(3, LOW);
  delayMicroseconds(10); 
  tempo = pulseIn(2, HIGH);
  distancia = tempo/1000000 * 170 * 100;
  delay(10);
  
  if(distancia <= 250){
    digitalWrite(led_vermelho, HIGH);
    digitalWrite(led_verde, LOW);
    tone(buzzer, 262); //Dó
    delay(200);
    noTone(buzzer);
    tone(buzzer, 294); //Ré
    delay(200);
    noTone(buzzer);
    tone(buzzer, 330); //Mi
    delay(200);
    noTone(buzzer);
    tone(buzzer, 349); //Fá
    delay(200);
    noTone(buzzer);
    delay(200);
  }
  else{
    digitalWrite(led_vermelho, LOW);
    digitalWrite(led_verde, HIGH);
  }
}