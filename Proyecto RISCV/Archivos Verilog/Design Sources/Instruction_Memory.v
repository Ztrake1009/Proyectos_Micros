`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
/*

Funcionalidad:
En este bloque se espera que se lea correctamente cada instruccion a realizar,
estas intrucciones provienen de un archivo txt con cada instruccion en hexadecimal.

Entradas:
Variable CLK (Reloj del sistema).
Variable RST (Señal de reset).
Variable PC (Direccion de la instruccion que se lee en ese momento).

Salidas:
Variable Inst (Sale la instruccion que se lea en la direccion especificada).

Razon:
Se crea para poder observar las instrucciones que debe realizar la microarquitectura diseñada.

*/
//////////////////////////////////////////////////////////////////////////////////


module Instruction_Memory(
    input CLK, RST, //Reloj del sistema y el Reset
    input [31:0] PC, //Direccion de la instruccion
    output reg [31:0] Inst //Instruccion en la direccion
    );
    
    reg[31:0] mem[255:0]; //Variable interna para el banco de memoria de 256 espacios
    
    //Lectura del archivo txt con las instrucciones
    always @(*) begin
        $readmemh("C:/Proyecto_RISCV_VIVADO/Proyecto/Instrucciones.txt", mem, 0);
        Inst = mem[PC];
    end
endmodule