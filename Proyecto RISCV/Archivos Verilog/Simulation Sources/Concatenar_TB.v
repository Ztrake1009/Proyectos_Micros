`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 08.10.2023 21:26:28
// Design Name: 
// Module Name: Concatenar_TB
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


module Concatenar_TB(
    );
    //Inputs
    reg [4:0] Num_A;  //Entrada de 5 bits
    reg [6:0] Num_B;  //Entrada de 7 bits
    
    //Outputs
    wire [11:0] Salida; //Salida de 32 bits
    
    //Instantiate
    //Llamado de variables en el modulo del testbench correspondiente
    Concatenar uut (
    .Num_A(Num_A),
    .Num_B(Num_B),
    .Salida(Salida)
    );
    
    //Stimulus
    initial begin
    Num_A = 5'd0;
    Num_B = 7'd0;
    #100
    Num_A = 5'd15;
    Num_B = 7'd87;
    #100
    Num_A = 5'd4;
    Num_B = 7'd127;
    #100
    $finish;
    end
endmodule
