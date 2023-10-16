`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
/*

Funcionalidad:
En este bloque se espera extender una entrada de 12 bits a 32 bits, 
para esto se rellena con ceros a la izquierda.

Entradas:
Variable Extender (Entrada de 12 bits).

Salidas:
Variable Extendido (Sale la entrada de 12 bits extendida a 32 bits).

Razón:
Se utiliza debido a que RISCV se maneja con 32 bits, por lo que es necesario una extension.

*/
//////////////////////////////////////////////////////////////////////////////////


module Extend_12to32(
    input [11:0] Extender, //Entrada de 12 bits
    output [31:0] Extendido //Salida de 32 bits
    );
    
    //Variable a utilizar para llenar con ceros la salida
    reg[19:0] Ceros = 20'h00000;
    
    //Concatena 20 ceros a la entrada dejando la entrada a la derecha
    assign Extendido = {Ceros,Extender};
endmodule
