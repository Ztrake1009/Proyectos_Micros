`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
/*

Objetivo:
En este bloque se espera simular correctamente la extension de
la palabra de 12 bits a 32 bits.

*/  
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
        //Resultado esperado: 32'h00000000
        
        #100
        Extender = 12'd45; //Prueba con el numero 45
        //Resultado esperado: 32'h0000002D
        
        #100
        Extender = 12'd2047; //Prueba con el numero 2047
        //Resultado esperado: 32'h000007FF
        
        #100
        Extender = 12'd250; //Prueba con el numero 250
        //Resultado esperado: 32'h000000FA
        
        #100
        $finish;
    end
endmodule
