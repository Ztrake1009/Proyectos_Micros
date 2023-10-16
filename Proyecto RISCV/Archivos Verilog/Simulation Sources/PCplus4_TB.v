`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
/*

Objetivo:
En este bloque se espera simular correctamente la suma de 4 al PC
para seguir con la siguiente instruccion.

*/  
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
        //Resultado esperado: 32'h00000004
        
        #100
        PC = 32'h4;
        //Resultado esperado: 32'h00000008
        
        #100
        PC = 32'h8;
        //Resultado esperado: 32'h0000000C
        
        #100
        PC = 32'hc;
        //Resultado esperado: 32'h00000010
        
        #100
        PC = 32'h10;
        //Resultado esperado: 32'h00000014
        
        #100
        $finish;
    end
endmodule
