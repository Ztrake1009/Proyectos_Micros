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
Variable WD: Write Data, info a escribir en la dirección de memoria dada.
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
    output [31:0] RD //Datos leidos
    );
    
    reg [31:0] RAM [65535:0]; //Variable Interna, Memoria de acceso aleatorio de 65536 espacios con 32 bits para data
    integer i; //Contadores y offset
    integer file_ad; //Variable para abrir el archivo
    
    initial begin //Inicializando las Memorias 
        //Se definen los espacions de memoria desde 
        for (i=0; i<65535; i=i+1)begin 
            RAM[i] = 0;
        end
    end 

    initial begin 
        file_ad = $fopen("MEM_DUMP.txt","w"); //Se abre el archivo de texto
    end

    //Escritura
    always @(posedge CLK) //Siempre que haya un cambio en el Clock
        if (MemWrite == 1'b1)begin //Señal control de escritura
            RAM [Address] <= WD; //Se escribe la Write Data en el espacio Address
        end 


    //Reset
    always@(negedge RST) //Si se da un reset, se reinician en 0 todas las direcciones de memoria
    begin
        if (!RST) begin
            for (i = 0; i < 65535; i = i + 1) begin
                RAM[i] <= 0;
            end
        end
    end

    //Lectura
    assign RD = RAM[Address];
    initial begin //Se escribe el Dump de Memoria
        #800
        for (i=0; i<65535; i=i+1) begin
            $fdisplay(file_ad, "%h", i,"  ", RAM[i]); 
        end
    end
endmodule
