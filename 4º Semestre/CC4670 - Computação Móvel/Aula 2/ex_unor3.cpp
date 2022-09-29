void setup(){
	int ledVermelho = 13;
	pinMode(ledVermelho, OUTPUT);
	int ledAmarelo = 12;
	pinMode(ledAmarelo, OUTPUT);
}

void loop(){
	digitalWrite(ledVermelho, HIGH);
	digitalWrite(ledAmarelo, LOW);
	delay(1000);
	digitalWrite(ledAmarelo, HIGH):
	digitalWrite(ledVermelho, LOW);
	delay(1000);
}


