
.include "/home/sam-admin/iith/assembly/m328Pdef.inc"


  ldi r16,0b00111111
  out DDRB,r16
  
  
  ldi r31,0b11000000
  out DDRD,r31
  
ldi r18,0b00000001   ;x
ldi r19,0b00000001   ;y
ldi r20,0b00000001   ;z


ldi r17,0b00000001  ; used for compliment

;for A (R21)
mov r21,r18
mov r22,r19
mov r23,r20

and r21,r22
and r21,r23

;for B (R22)
mov r22,r18
mov r23,r19
mov r24,r20
eor r24,r17
and r22,r23
and r22,r24
lsl r22

;for C (R23)
mov r23,r18
mov r24,r19
mov r25,r20
eor r24,r17
and r23,r24
and r23,r25
lsl r23
lsl r23

;for D (R24)
mov r24,r18
mov r25,r19
mov r26,r20
eor r25,r17
eor r26,r17
and r24,r25
and r24,r26
lsl r24
lsl r24
lsl r24

;for E (R25)
mov r25,r18
mov r26,r19
mov r27,r20
eor r25,r17
and r25,r26
and r25,r27
lsl r25
lsl r25
lsl r25
lsl r25

;for F (R26)
mov r26,r18
mov r27,r19
mov r28,r20
eor r26,r17
eor r28,r17
and r26,r27
and r26,r28
lsl r26
lsl r26
lsl r26
lsl r26
lsl r26

;for G (R27)
mov r27,r18
mov r28,r19
mov r29,r20
eor r27,r17
eor r28,r17
and r27,r28
and r27,r29
lsl r27
lsl r27
lsl r27
lsl r27
lsl r27
lsl r27

;for H (R28)
mov r28,r18
mov r29,r19
mov r30,r20
eor r28,r17
eor r29,r17
eor r30,r17
and r28,r29
and r28,r30
lsl r28
lsl r28
lsl r28
lsl r28
lsl r28
lsl r28
lsl r28

;output on PORTB
or r21,r22
or r21,r23
or r21,r24
or r21,r25
or r21,r26
;or r21,r27
;or r21,r28
out PORTB,r21

;output on PORTD
mov r16,r27
mov r17,r28
or r16,r17

out PORTD,r16

Start:
rjmp Start

