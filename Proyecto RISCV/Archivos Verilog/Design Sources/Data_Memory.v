`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
/*

Funcionalidad:
En este bloque se crea la memoria de datos. Se utiliza para
almacenar datos durante la ejecucion del programa. La memoria
consiste en un array de datos de acceso aleatorio, en cualquier momento se puede
acceder a cualquier direccion de memoria. 

Entradas:
Variable Address: Es la direccion de memoria con la que se trabaja.
Variable WD: Write Data, info a escribir en la direccion de memoria dada.
Variable MemWrite: Senal de control para habiliar la escritura de datos en la memoria.
Variable CLK: Reloj del sistema.
Variable RST: Senal de Reset.

Salidas:
Variable RD: Data leida de la memoria en la direccion dada.

Razon:
Se crea para almacenar datos en la memoria volatil.

*/
//////////////////////////////////////////////////////////////////////////////////


module Data_Memory(
    input CLK, //Clock
    input RST, //Reset
    input [31:0] Address, //Direccion de memoria con la que se trabaja 
    input [31:0] WD, //Datos a escribir
    input MemWrite, //Control de escritura
    output reg [31:0] RD //Datos leidos
    );
    
    reg [31:0] RAM [255:0]; //Variable Interna, Memoria de acceso aleatorio de 256 espacios con 32 bits para data
    integer i; //Contador
    
    //Variable auxiliar para almacenar las direcciones
    wire [7:0] Dir;
    
    assign Dir = Address[7:0];
    
    //Inicializando las Memorias
    initial begin
        //Se definen los espacions de memoria en 0
        for (i=0; i<256; i=i+1) begin
            RAM[i] = 0;
        end
    end
    
    //Escritura
    always @(posedge CLK) begin //Siempre que haya un cambio en el Clock
        if (MemWrite) begin //Senal control de escritura
            RAM[Dir] <= WD; //Se escribe la Write Data en el espacio Address
        end
    end

    //Reset
    always @(negedge RST) begin //Si se da un reset, se reinician en 0 todas las direcciones de memoria
        if (!RST) begin
            for (i=0; i<256; i=i+1) begin
                RAM[i] <= 0;
            end
        end
    end

    //Lectura de los datos en la direccion indicada
    always @(*) begin
        RD <= RAM[Dir];
    end
endmodule
