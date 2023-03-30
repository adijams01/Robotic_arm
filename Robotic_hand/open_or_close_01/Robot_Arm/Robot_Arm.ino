#include <Servo.h>

#define numOfValsRec 5
#define digitsPerValRec 1



int receivedarray[numOfValsRec];
int stringLength=numOfValsRec*digitsPerValRec+1;
int counter=0;
bool counterStart=false;
char recievedString[5];

void setup() {
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);


}

void receiveData() {
  while(Serial.available()){
    char c = Serial.read();
    if (c=='$'){
      counterStart = true;

    }
    if (counterStart){
      
       if (counter<stringLength){
     receivedarray[counter]=int(c);
     counter++;
       }
       else{
        counter=0;
        counterStart=false;
       }
    }
  // Serial.println("work");      // print a message over serial
  // Serial.println(c);      // print a message over serial
  
  }
}
void loop() {
  receiveData();
  // Serial.println(receivedarray[0]);      // print a message over serial
  // Serial.println(receivedarray[1]);      // print a message over serial
  // Serial.println(receivedarray[2]);      // print a message over serial
  if (receivedarray[1]==49){
      digitalWrite(LED_BUILTIN, HIGH);  // turn on the LED
      // Serial.println("LED ON");      // print a message over serial

      delay(1000);
  }
  else{
      digitalWrite(LED_BUILTIN, LOW);  // turn on the LED
      // Serial.println("LED OFF");      // print a message over serial

  }
  receivedarray[0]=0;
  receivedarray[1]=0;
      // delay(5000);
  // digitalWrite(LED_BUILTIN, LOW);  // turn on the LED
}