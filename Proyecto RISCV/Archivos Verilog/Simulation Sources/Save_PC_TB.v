`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
/*

Objetivo:
En este TestBench se espera simular correctamente la actualizacion del PC
anterior al nuevo PC.

*/  
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
        
        PC_In = 32'h0; //Se define que el PC de entrada es 32'h0
        CLK = 0;
        //Resultado esperado: PC_Out = 32'hXXXXXXXX (no interesa el PC anterior porque no se ha usado el CLK)
        #100
        CLK = 1;
        //Resultado esperado: PC_Out = 32'h00000000
        
        #100
        PC_In = 32'h4; //Se define que el PC de entrada es 32'h4
        CLK = 0;
        //Resultado esperado: PC_Out = 32'h00000000
        #100
        CLK = 1;
        //Resultado esperado: PC_Out = 32'h00000004
        
        #100
        PC_In = 32'h8; //Se define que el PC de entrada es 32'h8
        CLK = 0;
        //Resultado esperado: PC_Out = 32'h00000004
        #100
        CLK = 1;
        //Resultado esperado: PC_Out = 32'h00000008
        
        #100
        PC_In = 32'hc; //Se define que el PC de entrada es 32'hc
        CLK = 0;
        //Resultado esperado: PC_Out = 32'h00000008
        #100
        CLK = 1;
        //Resultado esperado: PC_Out = 32'h0000000C
        
        #100
        $finish;
    end
endmodule
