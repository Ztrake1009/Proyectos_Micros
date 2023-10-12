`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 11.10.2023 18:06:47
// Design Name: 
// Module Name: PCplus4_TB
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


module PCplus4_TB(
    );
    //Inputs
    reg [31:0] PC; //PC de entrada
    
    //Outputs
    wire [31:0] Next_PC; //PC + 4 de salida
    
    //Instantiate
    //Llamado de variables en el modulo del testbench correspondiente
    PCplus4 UUT(
    .PC(PC),
    .Next_PC(Next_PC)
    );
    
    //Stimulus
    //Se declaran diferentes instrucciones entrantes
    initial begin
        PC = 32'h0;
        #100
        PC = 32'h4;
        #100
        PC = 32'h8;
        #100
        PC = 32'hc;
        #100
        PC = 32'h10;
        #100
        $finish;
    end
    
endmodule
