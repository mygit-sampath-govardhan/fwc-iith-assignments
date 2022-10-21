module helloworldfpga(

input  wire X,
input  wire Y,
input  wire Z,

output wire A,
output wire B,
output wire C,
output wire D,
output wire E,
output wire F,
output wire G,
output wire H

);


//Display Decoder
always @(*)
begin


A= !X&!Y&!Z;
B= !X&!Y&Z;
C= !X&Y&!Z;
D= !X&Y&Z;
E= X&!Y&!Z;
F= X&!Y&Z;
G= X&Y&!Z;
H= X&Y&Z;


end
endmodule
