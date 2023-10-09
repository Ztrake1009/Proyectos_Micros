`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 08.10.2023 21:46:02
// Design Name: 
// Module Name: Mux_2to1
// Project Name: 
// Target Devices: 
// Tool Versions: 
// Description: 
// 
// Dependencies: 
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
//////////////////////////////////////////////////////////////////////////////////


module Mux_2to1(
    input [31:0] Num_A, //Opcion 1 del mux
    input [31:0] Num_B, //Opcion 2 del mux
    input Selector, //Senal encargada de elegir la opcion 1 o 2
    output reg [31:0] OutMux //Salida del mux 
    );
    
    always @ (*) begin //siempre que haya un cmabio en las entradas 
        case (Selector)  
            1'd0 : OutMux <= Num_A; //Si el selector esta en 0 selecciona la opcion 1 
            1'd1 : OutMux <= Num_B; //Si el selector esta en 1 selecciona la opcion 2 
            default : OutMux <=32'b0; //Caso default la salida es cero 
        endcase
     end
endmodule