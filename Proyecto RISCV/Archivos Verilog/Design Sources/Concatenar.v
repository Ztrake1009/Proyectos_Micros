`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 08.10.2023 21:22:18
// Design Name: 
// Module Name: Concatenar
// Project Name: 
// Target Devices: 
// Tool Versions: 
// Description: 
// 
// Dependencies: 
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
//////////////////////////////////////////////////////////////////////////////////


module Concatenar(
    input [4:0] Num_A, //Entrada 5 bits
    input [6:0] Num_B, //Entrada 7 bits
    output [11:0] Salida //Salida 32 bits
    );
    
    //Concatena las dos entradas
    assign Salida[11:0] = {Num_B[6:0],Num_A[4:0]};
endmodule
