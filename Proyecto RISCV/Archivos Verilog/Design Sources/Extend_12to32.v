`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 08.10.2023 20:59:11
// Design Name: 
// Module Name: Extend_12to32
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


module Extend_12to32(
    input [11:0] Extender, //Entrada de 12 bits
    output [31:0] Extendido //Salida de 32 bits
    );
    
    //Concatena 20 ceros a la entrada dejando la entrada a la derecha
    assign Extendido = {{20{Extender[11]}},Extender};
endmodule
