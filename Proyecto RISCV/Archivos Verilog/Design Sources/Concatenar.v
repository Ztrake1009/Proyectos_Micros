`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
/*

Funcionalidad:
En este bloque se espera que se combinen dos entradas distintas en una salida de
12 bits.

Entradas:
Variable Num_A (Entrada A de 5 bits).
Variable Num_B (Entrada B de 7 bits).

Salidas:
Variable Salida (Sale la concatenacion de las entradas A y B).

Razon:
Se crea para poder concatenar dos variables, este bloque se utiliza solamente
a la hora de seleccionar entre el uso de instrucciones tipo I o S.

*/
//////////////////////////////////////////////////////////////////////////////////


module Concatenar(
    input [4:0] Num_A, //Entrada 5 bits
    input [6:0] Num_B, //Entrada 7 bits
    output [11:0] Salida //Salida 32 bits
    );
    
    //Concatena las dos entradas
    assign Salida[11:0] = {Num_B[6:0],Num_A[4:0]};
endmodule
