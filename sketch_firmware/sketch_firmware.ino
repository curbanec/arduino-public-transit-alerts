#define LED 13

int bytez = 0; //for testing purposes for serial connection

void setup(){
Serial.begin(9600);
pinMode (LED, OUTPUT);
//Serial.write('1');


pinMode(9, OUTPUT);
beep(50);
beep(50);
beep(50);
delay(1000);



}
/*
I have kept this code here to show how I first tested the serial connection betweeen arduino and python code
void loop(){
if(Serial.available()>0){//send data only when you recieve data
  bytez=Serial.read();
  Serial.print("I recieved: ");
  Serial.println(bytez);
  digitalWrite(LED, HIGH);
  //delay(500);
  //digitalWrite(LED, LOW);
  //delay(500);
  //digitalWrite(LED, HIGH);
  //delay(500);
  //digitalWrite(LED, LOW);
  
  Serial.write('0k!'); 
  }//end if
}//end loop
*/

int x = 75;
//print prints the nymber
//write writes the value

void loop(){
  if(Serial.available()>0){
  char letter = Serial.read();
    if (letter=='1'){
      digitalWrite(LED, HIGH);
      //delay(500);
      //digitalWrite(LED,LOW);
      Serial.println("LED ON");
      Serial.print(letter);//prints 1
    }
    else if(letter=='0'){
      digitalWrite(LED, LOW);
      Serial.println("LED OFF");
    }
  
  if (letter=='15'){//the 15 is arbitrary, if I allocate 2 bytes vs 1 byte as i did before, the loop will run
  
  beep(200);//calling the beep function I have just written
  delay(1000);
   beep(200);
  delay(1000);
   beep(200);
  delay(1000);
  
  
  }
  
  }
}
void beep(unsigned char delayms){
  analogWrite(9, 20);      // Almost any value can be used except 0 and 255
                           // experiment to get the best tone
  delay(delayms);          // wait for a delayms ms
  analogWrite(9, 0);       // 0 turns it off
  delay(delayms);          // wait for a delayms ms   
}  
