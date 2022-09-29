
//Pisca o LED

void setup (){
	pinMode(13, OUTPUT);:
}

void loop (){
	// 5V no pino 13:
	digitalWrite(13, HIGH); //Acende o LED
	delay(1000); //Apaga 1 segundo

	// 0V no prino 13;
	digitalWrite(13, LOW); //Apaga o LED
	delay(1000);
}

//digitalWrite(num, HIGH/LOW)
//pinMode(num, OUTPUT/INPUT)

