`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
/*

Funcionalidad:
En este bloque se espera ejecutar el funcionamiento de una ALU con
las operaciones de Suma, Resta, AND, XOR y desplazamiento a la izquierda.

Entradas:
Variable In_A (Operando A de la ALU).
Variable In_B (Operando B de la ALU).
Variable ALUControl (Señal para selecionar la operacion a realizar).

Salidas:
Variable Out_ALU (Sale la operacion realizada por la ALU).

Razon:
Se crea para poder realizar las operaciones que debe soportar la microarquitectura.

*/
//////////////////////////////////////////////////////////////////////////////////


module ALU_2to1(
    input [31:0] In_A, In_B, //Operandos de la ALU
    input [2:0] ALUControl, //Selector de operacion en la ALU   
    output reg [31:0] Out_ALU //Salida de la ALU
    );
    always @(*) begin //Siempre que haya un cambio
        case(ALUControl)
            3'b000: Out_ALU = In_A + In_B;  // 0: Se hace una Suma de los operandos
            3'b001: Out_ALU = In_A - In_B;  // 1: Se hace una Resta de los operandos
            3'b010: Out_ALU = In_A & In_B;  // 2: Se hace una AND con los operandos
            3'b011: Out_ALU = In_A ^ In_B;  // 3: Se hace una XOR con los operandos
            3'b100: Out_ALU = In_A << In_B; // 4: Se hace desplazamiento a la izquierda
        default: Out_ALU = 32'd0;  //Caso default, la salida de la ALU es cero
        endcase
    end
endmodule
