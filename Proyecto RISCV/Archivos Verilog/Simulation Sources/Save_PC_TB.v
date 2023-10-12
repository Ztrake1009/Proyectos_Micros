`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 11.10.2023 19:01:09
// Design Name: 
// Module Name: Save_PC_TB
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


module Save_PC_TB(
    );
    //Inputs
    reg CLK, RST; //Reloj del sistema y el Reset
    reg [31:0] PC_In; //PC de entrada
    
    //Outputs
    wire [31:0] PC_Out; //PC de salida

    //Instantiate
    //Llamado de variables en el modulo del testbench correspondiente
    Save_PC UUT(
    .CLK(CLK),
    .RST(RST),
    .PC_In(PC_In),
    .PC_Out(PC_Out)
    );
    
    //Stimulus
    initial begin
        RST = 0;
        CLK = 0;
        
        PC_In = 32'h4; //Se define una instruccion entrante de prueba
        CLK = 0; 
        #100
        CLK = 1;     
        #100
        PC_In = 32'h8; //Se define una instruccion entrante de prueba
        CLK = 0; 
        #100
        CLK = 1;
        #100
        PC_In = 32'hc; //Se define una instruccion entrante de prueba
        CLK = 0; 
        #100
        CLK = 1;
        #100
        $finish;
    end
endmodule
