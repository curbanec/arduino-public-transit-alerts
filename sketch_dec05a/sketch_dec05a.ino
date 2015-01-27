/*
 *Christopher Urbanec 9/22/2014
 *University of Illinois at Urbana-Champaign
 *TSM 435 Lab
 *uC2-Switch_Input Code
 
 */

#define SWO 8 /* dont need semi colons create symbol that is worth the number 8*/
#define LED 13 /* Ints take 8 bits of space*/

bool ledstate = LOW; /* LOW is a possible value of a boolean. LOW HIGH are equivalent to TRUE FALSE */



void setup(){ /*on float, char, void loops are simply functions that don't take a parameter*/ 
pinMode (SWO, INPUT_PULLUP); /*input, output, input_pullup= deploy an internal resistore inside arduino. INPUT_PULLUP uses internal pullup resistors and inverts behavior to HIGH means sensor is off*/
pinMode (LED, OUTPUT); /* ! is the not operator. takes a boolean value and flips it around. If bool, flip bool and then move one. */
}
void loop () { 
  if (digitalRead (SWO)==LOW){ // digitalRead takes one parameter, a pin number. it returns HIGH or LOW
    delay(200); //delay signal by 200ms
    if (digitalRead(SWO)==LOW){ //this if statement is set up to help make the function of blinking run smoother. 
      ledstate= !ledstate; //if current LED state at this point is not LOW, then change it to != or "not equal to" aka switch it to HIGH
    }                      // I think the key here is that if state is LOW, it doesent have enough voltage to turn on LED, but HIGH state provides 5V, which is enough
  }
  digitalWrite(LED, ledstate); //dWrite takes pin and value as a parameter. In this case, the else statement sets to HIGH
}
/*switch de-bouncing* two ways to solve. First is a hardware solution as a capacitor*/

