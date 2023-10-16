`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
/*

Funcionalidad:
En este bloque se espera que según la señal de PC entrante
pueda salir un PC nuevo pero sumado con 4.


Entradas:
Variable PC (PC que se está utilizando en ese momento).

Salidas:
Variable Next_PC (Sale el nuevo PC pero con una suma de 4).

Razon:
Se crea para poder seguir a la nueva instruccion u operacion por realizar.

*/
//////////////////////////////////////////////////////////////////////////////////


module PCplus4(
    input [31:0] PC, //PC de entrada
    output reg [31:0] Next_PC //PC + 4 de salida 
    );
    
    always@(*) //Siempre que haya un cambio 
        Next_PC = PC + 32'd4; //Se le suma 4 a PC para avanzar la siguiente instruccion 
endmodule
