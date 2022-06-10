#include<Servo.h>

int getIntegerFromSerial(){
  int n=0;
  while(1){
    if(Serial.available()<=0)
      continue;
    char readChar=Serial.read();
    if(readChar=='\n'){
      return n;
    }
    n*=10;
    unsigned int l=readChar-'0';
    n+=l;
  }
}

Servo servo;

void setup() {
  // put your setup code here, to run once:
  servo.attach(11,500,2400);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  servo.write(getIntegerFromSerial());
}
