`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
/*

Funcionalidad:
En este bloque se espera que entren dos variables y segun un
selector se obtiene a la salida alguna de estas dos variables.

Entradas:
Variable Num_A (Entrada A).
Variable Num_B (Entrada B).
Variable Selector (Utilizado para seleccionar entre alguna de las dos entradas).

Salidas:
Variable Out_Mux (Sale la entrada A o la B según el selector usado).

Razon:
Se crea para poder seleccionar entre las distintas instrucciones a realizar,
por ejemplo, un mux se va a utilizar para seleccionar entre operaciones tipo S y tipo I.

*/
//////////////////////////////////////////////////////////////////////////////////


module Mux_2to1(
    input [31:0] Num_A, //Opcion 1 del mux
    input [31:0] Num_B, //Opcion 2 del mux
    input Selector, //Senal encargada de elegir la opcion 1 o 2
    output reg [31:0] Out_Mux //Salida del mux
    );
    
    always @ (*) begin //Siempre que haya un cmabio en las entradas 
        case (Selector)  
            1'd0 : Out_Mux <= Num_A; //Si el selector esta en 0 selecciona la opcion 1 
            1'd1 : Out_Mux <= Num_B; //Si el selector esta en 1 selecciona la opcion 2 
        default : Out_Mux <=32'b0; //Caso default la salida es cero 
        endcase
     end
endmodule