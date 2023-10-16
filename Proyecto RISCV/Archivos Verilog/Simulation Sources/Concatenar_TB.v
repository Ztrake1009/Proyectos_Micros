`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
/*

Objetivo:
En este bloque se espera simular correctamente la concatenacion
de dos entradas.

*/ 
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
    Concatenar UUT(
    .Num_A(Num_A),
    .Num_B(Num_B),
    .Salida(Salida)
    );
    
    //Stimulus
    initial begin
        //Prueba con los numeros 0 y 0
        Num_A = 5'd0; //5'b00000
        Num_B = 7'd0; //7'b0000000
        //Resultado esperado: 12'b000000000000
        
        #100
        //Prueba con los numeros 15 y 87
        Num_A = 5'd15; //5'b01111
        Num_B = 7'd87; //7'b1010111
        //Resultado esperado: 12'b101011101111

        #100        
        //Prueba con los numeros 4 y 127
        Num_A = 5'd4; //5'b00100
        Num_B = 7'd127; //7'b1111111
        //Resultado esperado: 12'b111111100100
        
        #100
        $finish;
    end
endmodule
