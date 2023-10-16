`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
/*

Objetivo:
En este bloque se espera simular correctamente la lectura de una nueva instruccion
segun el cambio en la direccion cada cierto tiempo.

*/  
//////////////////////////////////////////////////////////////////////////////////


module Instruction_Memory_TB(
    );
    
    //Inputs
    reg CLK = 0; //Reloj
    reg RST = 0; //Reset 
    reg[31:0] PC; //Direccion de la instruccion
        
    //Outputs
    wire[31:0] Inst; //Instruccion en la direccion
    
    //Instantiate
    //Llamado de variables en el modulo del testbench correspondiente
    Instruction_Memory UUT(
    .CLK(CLK),
    .RST(RST),
    .PC(PC), 
    .Inst(Inst)
    );
    
    //Stimulus
    initial begin
        CLK = 0;
        RST = 0;
        
        //Se revisan diferentes direcciones de memoria como prueba
        PC = 32'd0;
        //Resultado esperado: 32'hFD010113
        
        #100
        PC = 32'd4;
        //Resultado esperado: 32'h02812623
        
        #100
        PC = 32'd8;
        //Resultado esperado: 32'h03010413
        
        #100
        PC = 32'd12;
        //Resultado esperado: 32'h0000B7B7
        
        #100
        PC = 32'd16;
        //Resultado esperado: 32'hBCD78793
        
        #100
        PC = 32'd20;
        //Resultado esperado: 32'hFEF42623

        #100;
        $finish;
    end

    always #100 CLK = CLK + 1;
endmodule
