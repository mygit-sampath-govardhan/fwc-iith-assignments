#include <Arduino.h>

void disp_7447(int C, int B, int A)                   \\3*8 decoder
{
  digitalWrite(2, A); 
  digitalWrite(3, B); 
  digitalWrite(4, C); 
}
void setup() {
    pinMode(2, OUTPUT);  
    pinMode(3, OUTPUT);
    pinMode(4, OUTPUT);
}
void loop() {
disp_7447(1,1,0);  
}

