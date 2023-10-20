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
        RST = 0;
        CLK = 0;
        
        #10
        RST = 1;
        //Toda la memoria esta en 0 por el RESET
        
        #10
        RST = 0;
        
        //Se activa la escritura y se escribe 14 en la direccion FFE8
        MemWrite = 1;
        WD = 32'd14;
        Address = 32'hFFE8;
        /*
        Resultado esperado:
        RD = 32'd14
        */
        
        #10;    
        //Se activa la escritura y se escribe 7 en la direccion FFE4
        MemWrite = 1;
        WD = 32'd7;
        Address = 32'hFFE4;
        /*
        Resultado esperado:
        RD = 32'd7
        */
        
        #10;    
        //Se desactiva la escritura y se lee la direccion FFE8
        MemWrite = 0;
        Address = 32'hFFE8;
        /*
        Resultado esperado:
        RD = 32'd14
        */
        
        #10;    
        //Se desactiva la escritura y se lee la direccion FFE4
        MemWrite = 0;
        Address = 32'hFFE4;
        /*
        Resultado esperado:
        RD = 32'd7
        */
        
        #10;
        $finish;
    end
    always #5 CLK = ~CLK;
endmodule
