`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
/*

Funcionalidad:
En este bloque se espera guardar el nuevo PC segun lo que se retorno de
la suma del anterior PC mas 4 en el modulo PCplus4.

Entradas:
Variable CLK (Reloj del sistema).
Variable RST (Senal de reset).
Variable PC_In (Nuevo PC a guardar en el PC general).

Salidas:
Variable PC_Out (Sale el nuevo PC guardado como general).

Razon:
Se crea para poder actualizar y almacenar el nuevo PC a utilizar por la microarquitectura.

*/
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
