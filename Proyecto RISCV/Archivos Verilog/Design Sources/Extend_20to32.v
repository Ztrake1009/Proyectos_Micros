`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 08.10.2023 21:11:00
// Design Name: 
// Module Name: Extend_20to32
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


module Extend_20to32(
    input [19:0] Extender, //Entrada de 20 bits
    output [31:0] Extendido //Salida de 32 bits
    );
    
    //Concatena 12 ceros a la entrada dejando la entrada a la derecha
    assign Extendido = {{12{Extender[19]}},Extender};
endmodule
