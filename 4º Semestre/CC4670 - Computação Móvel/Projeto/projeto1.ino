#include <LiquidCrystal.h>

//Entradas LCD
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);


//Entradas de botões
int doo = A0; //0
int re = A1; //1
int mi = A2; //2
int fa = A3; //3
int sol = A4; //4
int la = A5; //5
int si = 7; //6

//Entrada Som 
int buzzer = 8;

//Entrada Leds
int led_verde = 9;
int led_vermelho = 10;

int i=0;
int j = 0;
int nota = 9;

//Brilha Brilha Estrelinha

int music[] = {0,0,4,4,5,5,4,4,3,3,2,2,1,1,0,0};//15


//Define Output e Input
void setup() {
  pinMode(doo, INPUT);
  pinMode(re, INPUT);
  pinMode(mi, INPUT);
  pinMode(fa, INPUT);
  pinMode(sol, INPUT);
  pinMode(la, INPUT);
  pinMode(si, INPUT);
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(11, OUTPUT);
  pinMode(12, OUTPUT);
  pinMode(buzzer, OUTPUT);
  Serial.begin(9600);
  
  //Mensagem de Início
  lcd.begin(16, 2);
  lcd.print("Piano Digital");
  for(int i = 0; i < 16; i++){
    delay(100);
    lcd.scrollDisplayRight();
  }
  delay(50);
  lcd.clear();
  lcd.print("Comece!!!");
}

void loop() {
  	//Inicialização dos botões para o código
	int buttonStatedo = 0;
    int buttonStatere = 0;
    int buttonStatemi = 0;
    int buttonStatefa = 0;
    int buttonStatesol = 0;
    int buttonStatela = 0;
    int buttonStatesi = 0;
  
    buttonStatedo = digitalRead(doo);
    buttonStatere = digitalRead(re);
    buttonStatemi = digitalRead(mi);
    buttonStatefa = digitalRead(fa);
    buttonStatesol = digitalRead(sol);
    buttonStatela = digitalRead(la);
    buttonStatesi = digitalRead(si);
  
	
  	//Condições das teclas
      if (buttonStatedo == HIGH) {
        tone(buzzer, 262); //Dó
        delay(100);
        noTone(buzzer);
        tone(buzzer, 262); //Dó
        delay(100);
        noTone(buzzer);
        nota = 0;
        Serial.println(nota);
        lcd.clear();
        lcd.setCursor(4, 0);
        lcd.print("Nota:");
        lcd.setCursor(10, 0);
        lcd.print("C");
        delay(50);
        buttonStatedo = LOW;
      }

      if (buttonStatere == HIGH) {
        tone(buzzer, 294); //Ré
        delay(100);
        noTone(buzzer);
        tone(buzzer, 294); //Ré
        delay(100);
        noTone(buzzer);
        nota = 1;
        digitalWrite(0, HIGH);
        digitalWrite(0, LOW);
        Serial.println(nota);
        lcd.clear();
        lcd.setCursor(4, 0);
        lcd.print("Nota:");
        lcd.setCursor(10, 0);
        lcd.print("D");
        delay(50);
        buttonStatere  = LOW;
      }

      if (buttonStatemi == HIGH) {
        tone(buzzer, 330); //mi
        delay(100);
        noTone(buzzer);
        tone(buzzer, 330); //mi
        delay(100);
        noTone(buzzer);
        nota = 2;
        Serial.println(nota);
        lcd.clear();
        lcd.setCursor(4, 0);
        lcd.print("Nota:");
        lcd.setCursor(10, 0);
        lcd.print("E");
        delay(50);
        buttonStatemi = LOW;
      }
      if (buttonStatefa == HIGH) {
        tone(buzzer, 349); //fá
        delay(100);
        noTone(buzzer);
        tone(buzzer, 349); //fá
        delay(100);
        noTone(buzzer);
        nota = 3;
        Serial.println(nota);
        lcd.clear();
        lcd.setCursor(4, 0);
        lcd.print("Nota:");
        lcd.setCursor(10, 0);
        lcd.print("F");
        delay(50);
        buttonStatefa = LOW;
      }

      if (buttonStatesol == HIGH) {
        tone(buzzer, 392); //sol 
        delay(100);
        noTone(buzzer);
        tone(buzzer, 392); //sol 
        delay(100);
        noTone(buzzer);
        nota = 4;
        Serial.println(nota);
        lcd.clear();
        lcd.setCursor(4, 0);
        lcd.print("Nota:");
        lcd.setCursor(10, 0);
        lcd.print("G");
        delay(50);
        buttonStatesol = LOW;
      }

      if (buttonStatela == HIGH) {
        tone(buzzer, 440); //la
        delay(100);
        noTone(buzzer);
        tone(buzzer, 440); //la
        delay(100);
        noTone(buzzer);
        nota = 5;
        Serial.println(nota);
        lcd.clear();
        lcd.setCursor(4, 0);
        lcd.print("Nota:");
        lcd.setCursor(10, 0);
        lcd.print("A");
        delay(50);
        buttonStatela = LOW;
      }

      if (buttonStatesi == HIGH) {
        tone(buzzer, 494); //si
        delay(100);
        noTone(buzzer);
        tone(buzzer, 494); //si
        delay(100);
        noTone(buzzer);
        nota = 6;
        Serial.println(nota);
        lcd.clear();
        lcd.setCursor(4, 0);
        lcd.print("Nota:");
        lcd.setCursor(10, 0);
        lcd.print("B");
        delay(50);
        buttonStatesi = LOW;
      }
      
  	  //Condição de acerto
      if(music[j]==nota){
        digitalWrite(led_vermelho,LOW);
        digitalWrite(led_verde,HIGH);
        delay(300);
        digitalWrite(led_verde,LOW);
        delay(400);
        lcd.clear();
        lcd.setCursor(2, 0);
        lcd.print("Proxima Nota");
        j++;
      }
  	  //Condição de Erro!!!
      else{
        digitalWrite(led_verde,LOW);
        digitalWrite(led_vermelho,HIGH);
      }
  	  //Condição de Final
  	  if(j>15){
  		lcd.clear();
        lcd.setCursor(4, 0);
        lcd.print("Parabens!!!");
        digitalWrite(led_verde,HIGH);
        digitalWrite(led_vermelho,LOW);
        delay(5000);
        j=0;
 	  }	
      
  delay(100);
}
 