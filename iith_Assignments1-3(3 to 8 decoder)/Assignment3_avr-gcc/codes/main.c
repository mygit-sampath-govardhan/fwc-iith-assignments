

#include <avr/io.h>

#include <util/delay.h>

#include <stdbool.h>




int main (void)

{
DDRB = 0b00000000;
PORTB = 0b00011100;
DDRD = 0b11111100;
DDRB = 0b00000011;
while (1){
 int A,B,C,D,E,F,G,H;

 bool X,Y,Z;
 X = (PINB & (1<<PINB2)) == (1<<PINB2); 
 Y = (PINB & (1<<PINB3)) == (1<<PINB3);
 Z = (PINB & (1<<PINB4)) == (1<<PINB4);

H = ~X&~Y&~Z;
PORTD = ((H <<  PD2));
G = ~X&~Y&Z;
PORTD = ((G <<  PD3));  
F = ~X&Y&~Z;
PORTD = ((F <<  PD4));  
E = ~X&Y&Z;
PORTD = ((E <<  PD5));  
D = X&~Y&~Z;
PORTD = ((D <<  PD6));  
C = X&~Y&Z;
PORTD = ((C <<  PD7));  
B = X&Y&~Z;
PORTB = ((B <<  PB0));  
A = X&Y&Z;
PORTB = ((A <<  PB1));  

 }

        return 0;

}
