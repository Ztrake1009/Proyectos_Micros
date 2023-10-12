`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 08.10.2023 21:12:52
// Design Name: 
// Module Name: Extend_20to32_TB
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


module Extend_20to32_TB(
    );
    //Inputs
    reg [19:0] Extender;  //Entrada de 20 bits
    
    //Outputs
    wire [31:0] Extendido; //Salida de 32 bits
    
    //Instantiate
    //Llamado de variables en el modulo del testbench correspondiente
    Extend_20to32 UUT(
    .Extender(Extender),
    .Extendido(Extendido)
    );
    
    //Stimulus
    initial begin
        Extender = 20'd0;
        #100
        Extender = 20'd69; //Prueba con el numero 69
        #100
        Extender = 20'd1048574; //Prueba con el numero 1048574
        #100
        Extender = 20'd250; //Prueba con el numero 250
        #100
        Extender = 20'h0000b; //Prueba con el numero 0000b en hexadecimal 
        #100
        $finish;
    end
    
endmodule