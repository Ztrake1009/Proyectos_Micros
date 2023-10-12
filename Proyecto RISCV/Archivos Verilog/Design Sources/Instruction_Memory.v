`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 08.10.2023 14:17:16
// Design Name: 
// Module Name: Instruction_Memory
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


module Instruction_Memory(
    input CLK, RST, //Reloj del sistema y el Reset
    input [31:0] Dir, //Direccion de la instruccion
    output reg [31:0] Inst //Instruccion en la direccion
    );
    
    reg[31:0] mem[255:0]; //Variable interna para el banco de memoria de 256 espacios
    
    //Lectura del archivo txt con las instrucciones
    always @(*) begin
        $readmemh("C:/Proyecto_RISCV_VIVADO/Proyecto/Instrucciones.txt", mem, 0);
        Inst = mem[Dir];
    end
    
endmodule