`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 11.10.2023 18:02:37
// Design Name: 
// Module Name: PCplus4
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


module PCplus4(
    input [31:0] PC, //PC de entrada
    output reg [31:0] Next_PC //PC + 4 de salida 
    );
    
    always@(*) //Siempre que haya un cambio 
        Next_PC = PC + 32'd4; //Se le suma 4 a PC para avanzar la siguiente instruccion 
endmodule
