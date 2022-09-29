//Aluno - João Pedro Rosa Cezarino
//R.A - 22.120.021-5
//Link do projeto:https://www.tinkercad.com/things/h0pR5FW1uIy 

#include <LiquidCrystal.h>

LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

int pot = 0;

void setup() {
  pinMode(10, OUTPUT);
  pinMode(A0, INPUT);
  lcd.begin(16, 2);
  lcd.print("Contador de RPM");
  for(int i = 0; i < 16; i++){
    delay(200);
    lcd.scrollDisplayRight();
  }
  delay(400);
}

void loop() {
  pot = analogRead(A0); 
  analogWrite(10, pot/4);
  int rpm = map(pot, 0, 1023, 0, 22356);
  // 22356 é o maior valor de RPM do Motor
  
  lcd.clear();
  lcd.setCursor(4, 0);
  lcd.print(rpm);
  lcd.setCursor(11, 0);
  lcd.print("RPM");
  delay(150);
}
  
  
 
