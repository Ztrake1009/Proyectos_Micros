`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 08.10.2023 21:01:51
// Design Name: 
// Module Name: Extend_12to32_TB
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


module Extend_12to32_TB(
    );
    //Inputs
    reg [11:0] Extender;  //Entrada de 12 bits
    
    //Outputs
    wire [31:0] Extendido; //Salida de 32 bits
    
    //Instantiate
    //Llamado de variables en el modulo del testbench correspondiente
    Extend_12to32 UUT(
    .Extender(Extender),
    .Extendido(Extendido)
    );
    
    //Stimulus
    initial begin
    Extender = 12'd0;
    #100
    Extender = 12'd45; //probamos extendiendo el numero 45
    #100
    Extender = 12'd2047; //probamos extendiendo el numero 2047
    #100
    Extender = 12'd250; //probamos extendiendo el numero 250
    #100
    $finish;
    end

endmodule
