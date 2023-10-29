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

Razon:
Se utiliza debido a que RISCV se maneja con 32 bits, por lo que es necesario una extension.

*/
//////////////////////////////////////////////////////////////////////////////////


module Extend_12to32(
    input [11:0] Extender, //Entrada de 12 bits
    output [31:0] Extendido //Salida de 32 bits
    );

    reg [19:0] Relleno; //Variable interna, sirve para rellenar la palabra segun si el numero es positivo o negativo.
    
    //Se revisa el signo del numero a extender    
    wire Signo;
    assign Signo = Extender[11];
    
    //Variable a utilizar para llenar con ceros la salida
    always @(*) begin
        //Si es un numero positivo, lo rellena con ceros
        if (Signo == 0) begin
            Relleno <= 20'h00000;
        end
        //Si es un numero negativo, lo rellena con unos
        else if (Signo == 1) begin
            Relleno <= 20'hFFFFF;
        end
    end
    
    //Concatena 20 ceros a la entrada dejando la entrada a la derecha
    assign Extendido = {Relleno,Extender};
endmodule
