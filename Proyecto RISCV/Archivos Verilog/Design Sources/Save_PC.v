`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 11.10.2023 18:55:28
// Design Name: 
// Module Name: Save_PC
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


module Save_PC(
    input  CLK, RST, //Reloj del sistema y el Reset
    input  [31:0] PC_In, //PC de entrada
    output [31:0] PC_Out //PC de salida
    );
    
    reg [31:0] PC_Reg; //Variale interna para almacenar el PC
    
    always @ (posedge CLK) //Siempre que haya un cambio en el clock
        if (RST) begin //Si se acciona el reset, la variable interna se vuelve cero
            PC_Reg <= 0;
        end
        else begin
            PC_Reg <= PC_In; //Si no se acciona el reset, la variable interna se convierte en el PC de entrada 
        end
        
    assign PC_Out = PC_Reg; //Se le asigna a la salida la variable interna
endmodule
