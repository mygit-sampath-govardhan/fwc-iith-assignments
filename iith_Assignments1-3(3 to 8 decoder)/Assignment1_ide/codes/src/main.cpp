
#include <Arduino.h>
int X,Y,Z;
int A,B,C,D,E,F,G,H;
void disp_7447(int H, int G, int F, int E, int D,int C, int B, int A)
{
  digitalWrite(2, A); 
  digitalWrite(3, B); 
  digitalWrite(4, C); 
  digitalWrite(5, D); 
  digitalWrite(6, E); 
  digitalWrite(7, F); 
  digitalWrite(8, G); 
  digitalWrite(9, H);  

}
void setup() {
    pinMode(2, OUTPUT);  
    pinMode(3, OUTPUT);
    pinMode(4, OUTPUT);
    pinMode(5, OUTPUT);  
    pinMode(6, OUTPUT);
    pinMode(7, OUTPUT);
    pinMode(8, OUTPUT);  
    pinMode(9, OUTPUT);
    pinMode(10, INPUT);
    pinMode(11, INPUT);  
    pinMode(12, INPUT);}

void loop() {
X=digitalRead(10);
Y=digitalRead(11);
Z=digitalRead(12);

A= !X&&!Y&&!Z;
B= !X&&!Y&&Z;
C= !X&&Y&&!Z;
D= !X&&Y&&Z;
E= X&&!Y&&!Z;
F= X&&!Y&&Z;
G= X&&Y&&!Z;
H= X&&Y&&Z;

disp_7447(A,B,C,D,E,F,G,H);  
}


