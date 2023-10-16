`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
/*

Objetivo:
En este bloque se espera simular correctamente la extension de
la palabra de 20 bits a 32 bits obicando los 20 bits a la izquierda.

*/  
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
        //Resultado esperado: 32'h0000000
        
        #100
        Extender = 20'd69; //Prueba con el numero 69
        //Resultado esperado: 32'h00045000
        
        #100
        Extender = 20'd1048574; //Prueba con el numero 1048574
        //Resultado esperado: 32'hFFFFE000
        
        #100
        Extender = 20'd250; //Prueba con el numero 250
        //Resultado esperado: 32'h000FA000
        
        #100
        Extender = 20'h0000b; //Prueba con el numero 0000b en hexadecimal
        //Resultado esperado: 32'h0000B000
         
        #100
        $finish;
    end
endmodule
