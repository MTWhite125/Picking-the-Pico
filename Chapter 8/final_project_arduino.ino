#include <Wire.h>
#define I2C_ADDRESS 0x08
volatile bool commandReceived = false;
volatile byte command = 0;

int greenLed = 2;
int redLed = 3;
 
void receiveEvent(int numBytes) {
  if (Wire.available()) {
    command = Wire.read();
    commandReceived = true;
  }
}
//command 1
void turnOnRed(){
  digitalWrite(redLed, HIGH);
  digitalWrite(greenLed, LOW);
}  
//command 2
void turnOnGreen(){
  digitalWrite(redLed, LOW);
  digitalWrite(greenLed, HIGH);
}
//commmand 3
void flashGreen(){
  for (int i = 0; i != 10; i++){
    digitalWrite(greenLed, HIGH);
    delay(1000);
    digitalWrite(greenLed, LOW);
    delay(1000);
  }
  digitalWrite(greenLed, LOW);//make sure LED is off
}
//command 4
void flashRed(){
  for (int i = 0; i != 10; i++){
    digitalWrite(redLed, HIGH);
    delay(1000);
    digitalWrite(redLed, LOW);
    delay(1000);
  }
  digitalWrite(redLed, LOW);//make sure LED is off
}
//command 5
void turnOnBoth(){
  digitalWrite(redLed, HIGH);
  digitalWrite(greenLed, HIGH);
}
//command 6
void turnOffBoth(){
  digitalWrite(redLed, LOW);
  digitalWrite(greenLed, LOW);
}
//command 7
void altFlash(){
  for (int i = 0; i != 10; i++){
    digitalWrite(greenLed, HIGH);
    digitalWrite(redLed, LOW);
    delay(1000);
    digitalWrite(greenLed, LOW);
    digitalWrite(redLed, HIGH);
    delay(1000);
  }
  turnOffBoth();
}
void setup() {
  Wire.begin(I2C_ADDRESS);
  Wire.onReceive(receiveEvent);

  //set LEDs
  pinMode(greenLed, OUTPUT);
  pinMode(redLed, OUTPUT);
}                                                         
void loop() {
  // Do nothing until Pico sends something
  if (!commandReceived) {
    return;
  }
 
  switch(command){
    case 1:
      turnOnRed();
      break;
    case 2:
      turnOnGreen();
      break;
    case 3:
      flashGreen();
      break;
    case 4:
      flashRed();
      break;
    case 5:
      turnOnBoth();
      break;
    case 6:
      turnOffBoth();
      break;
    case 7:
      altFlash();
      break;
  }
  commandReceived = false;
}
