`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
/*

Funcionalidad:
En este bloque se crean 32 registros de proposito general con un tamano de 32 bits.

Entradas:
Variable CLK: Reloj del sistema.
Variable RST: Senal de Reset.
Variable A1: Registro por leer (Rs1).
Variable A2: Registro por leer (Rs2).
Variable A3: Direccion de registro para escribir (Rd).
Variable Wd: La informacion para escribir en un registro.
Variable RegWrite: Senal de control para saber cuando se debe escribir.

Salidas:
Variable RD1: Data que se leyo del registro (Rs1).
Variable RD2: Data que se leyo del registro (Rs2).

Razon:
Se crea para almacenar datos temporales, direcciones de memoria y
resultados intermedios durante la ejecucion de instrucciones.

*/
//////////////////////////////////////////////////////////////////////////////////


module Register_File(
    input CLK, //Clock
    input RST, //Reset
    input [4:0] A1, //Registro 1, Rs1
    input [4:0] A2, //Registro 2, Rs2
    input [4:0] A3, //Registro Destino, Rd
    input [31:0] WD, //Write Data
    input RegWrite, //Write Enable
    output reg [31:0] RD1, //Data del Registro, Rs1
    output reg [31:0] RD2 //Data del Registro, Rs2
    );
    
    reg [31:0] REGISTERS [31:0]; //Variable Interna, se usa para crear 32 registros de 32 bits
    
    //Inicializando los registros en 32'd0 (cero)
    integer i;
    initial begin 
        for (i=0; i<32; i=i+1) begin
            REGISTERS[i]=0;
        end
    end
    
    //Siempre que haya un cambio en las entradas A1 y A2, se lee la informacion en dichos registros
    always @(*) begin
        RD1 <= REGISTERS[A1];
        RD2 <= REGISTERS[A2];  
    end

    //Siempre que haya un flanco positivo del Clock se va a generar una escritura si el RegWrite esta activo o se active RST 
    always @(posedge CLK) begin 
        if (RST) begin //Si se activa el Reset (RST)
            //Reiniciando todos los registros en 0       
            for (i=0; i<32; i=i+1) begin
                REGISTERS[i]=0;
            end
         end
            
        if (RegWrite == 1'b1) begin //Senal control para realizar una escritura en un registro 
            if (A3 != 5'd0) begin //Se restringe escribir en el x0 porque siempre es cero.
                REGISTERS[A3] = WD;
            end
        end
    end    
endmodule
