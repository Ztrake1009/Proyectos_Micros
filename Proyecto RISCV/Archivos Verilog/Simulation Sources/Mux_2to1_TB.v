`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 08.10.2023 21:52:14
// Design Name: 
// Module Name: Mux_2to1_TB
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
    

module Mux_2to1_TB(
    );
    //Inputs
    reg [31:0] Num_A, Num_B; //Opcion 1 y 2 del mux
    reg Selector; //Senal encargada de elegir la opcion 1 o 2
    
    //Outputs
    wire [31:0] OutMux; //salida del mux
    
    //Instantiate
    //Llamado de variables en el modulo del testbench correspondiente
    Mux_2to1 UUT(
    .Num_A(Num_A),
    .Num_B(Num_B),
    .Selector(Selector),
    .OutMux(OutMux)
    );
    
    //Stimulus
    initial begin
        //Se definen valores para las opciones 1 y 2
        Num_A = 32'd3000000;
        Num_B = 32'd4;
        Selector = 0; //Se selecciona la opcion 1
        #100
        Selector = 1; //Se selecciona la opcion 2
        #100
        
        //Se definen valores para las opciones 1 y 2
        Num_A = 32'd902;
        Num_B = 32'd5254513;
        Selector = 0; //Se selecciona la opcion 1
        #100
        Selector = 1; //Se selecciona la opcion 2
        #100
        $finish;
    end
endmodule
