`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
/*

Funcionalidad:
En este bloque se espera extender una entrada de 20 bits a 32 bits,
para esto se rellena con ceros a la derecha.

Entradas:
Variable Extender (Entrada de 20 bits).

Salidas:
Variable Extendido (Sale la entrada de 20 bits extendida a 32 bits).

Razon:
Se utiliza debido a que RISCV se maneja con 32 bits, por lo que es necesario una extension,
sin embargo, este bloque solo es necesario para instrucciones tipo U, entre las operaciones a realizar
solo se encuentra una LUI, la cual debido a que guarda los 20 bits a la izquierda, entonces la extensión
se debe realizar hacia la derecha.

*/
//////////////////////////////////////////////////////////////////////////////////


module Extend_20to32(
    input [19:0] Extender, //Entrada de 20 bits
    output [31:0] Extendido //Salida de 32 bits
    );
    
    //Variable a utilizar para llenar con ceros la salida
    reg[11:0] Ceros = 12'h000;
    
    //Toma la entrada y la posiciona en los 20 bits más significativos de la salida
    //Luego adjunta a los 12 bits menos significativos ceros
    assign Extendido = {Extender,Ceros};
endmodule
