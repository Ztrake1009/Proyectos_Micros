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
    
    //Variable a utilizar para llenar con ceros la salida
    reg[11:0] Ceros = 12'h000;
    
    //Toma la entrada y la posiciona en los 20 bits más significativos de la salida
    //Luego adjunta a los 12 bits menos significativos ceros
    assign Extendido = {Extender,Ceros};
endmodule
