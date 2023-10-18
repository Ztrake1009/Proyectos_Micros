`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
/*

Objetivo:
En este TestBench se espera simular correctamente el funcionamiento del bloque
Data Memory, asi como las funciones de lectura y escritura con diferentes direcciones.

*/ 
//////////////////////////////////////////////////////////////////////////////////


module Data_Memory_TB(
    );
    //Inputs
    reg CLK; //Clock
    reg RST; //Reset
    reg [31:0] Address; //Direccion de memoria con la que se trabaja 
    reg [31:0] WD; //Datos a escribir
    reg MemWrite; //Control de escritura

    
    //Outputs
    wire [31:0] RD; //Datos leidos
    
    //Instantiate
    //Llamado de variables en el modulo del testbench correspondiente
    Data_Memory UUT(
    .CLK(CLK),
    .RST(RST),
    .Address(Address),
    .WD(WD),
    .MemWrite(MemWrite),
    .RD(RD)
    );
    
    initial begin
        //Se inician todas las variables 
        CLK = 0; 
        RST = 1;
        //Toda la memoria esta en 0 por el RESET
        
        #100;
        RST = 0;
        
        //Se activa la escritura y se escribe 100 en la direccion FFD0
        MemWrite = 1;
        WD = 32'd100;
        Address = 32'hFFD0;
        /*
        Resultado esperado:
        RD = 32'd100
        */
    
        #100;    
        //Se desactiva la escritura y se intenta escribir 135 en FFD0
        MemWrite = 0; 
        WD = 32'd135;
        /*
        Resultado esperado:
        No se espera ningun cambio
        RD = 32'd100
        */
        
        #100;
        $finish;
    end
    always #20 CLK = ~CLK;
endmodule
