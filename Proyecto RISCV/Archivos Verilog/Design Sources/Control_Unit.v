`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
/*

Funcionalidad:
En este bloque se espera controlar todas señales que indican a los modulos
que operaciones realizar segun el formato de la instruccion.

Entradas:
Variable Func_Siete (Variable que diferencia entre ADD y SUB para instrucciones tipo R).
Variable Opcode (Variable que identifica el formato de la instruccion a realizar).
Variable Func_Tres (Variable que diferencia que operacion realizar en un mismo formato de instrucciones).

Salidas:
Variable Reg_Write (Salida para habilitar la escritura en registro destino).
Variable ALUControl (Salida para seleccionar la operacion a realizar por la ALU).
Variable MemWrite (Salida para habilitar la escritura en memoria).
Variable WDSrc (Salida para activar el MUX que controla si se hacen operaciones tipo U o las otras).
Variable ImmReg (Salida para activar el MUX que controla si se hacen operaciones tipo S o tipo I).
Variable ALUSrc (Salida para activar el MUX que controla si se hacen operaciones tipo S-I o tipo R).
Variable MemToReg (Salida para activar el MUX que controla si se hacen loaders o las otras operaciones).

Razon:
Se crea para indicarle a los modulos que operaciones realizar segun el formato de cada instruccion.

*/
//////////////////////////////////////////////////////////////////////////////////


module Control_Unit(
    input [6:0] Funct_Siete, Opcode, //Funct7 y Opcode necesarios para determinar las operaciones a realizar
    input [2:0] Funct_Tres, //Funct3 para seleccionar la operacion
    output reg RegWrite, //Salida para habilitar la escritura en registro destino
    output reg [2:0] ALUControl, //Salida para seleccionar la operacion a realizar por la ALU
    output reg MemWrite, //Salida para habilitar la escritura en memoria
    output reg WDSrc, //Salida para activar el MUX que controla si se hacen operaciones tipo U o las otras
    output reg ImmReg, //Salida para activar el MUX que controla si se hacen operaciones tipo S o tipo I
    output reg ALUSrc, //Salida para activar el MUX que controla si se hacen operaciones tipo S-I o tipo R
    output reg MemToReg //Salida para activar el MUX que controla si se hacen loaders o las otras operaciones
    );
    
    always @(*) begin //Siempre que haya un cambio
        case(Opcode)
        
            //Instrucciones Formato R
            7'b0110011:
            begin
                //Se definen las salidas necesarias para una instruccion tipo R
                RegWrite = 1'b1;
                MemWrite = 1'b0;
                WDSrc = 1'b1;
                ALUSrc = 1'b1;
                MemToReg = 1'b0;
                
                //En caso de que sea una suma o resta
                if (Funct_Tres == 3'b000) begin
                    if (Funct_Siete == 7'b0000000) begin
                        ALUControl = 3'b000; //Se le indica a la ALU que realice una suma
                    end
                    else if (Funct_Siete == 7'b0100000) begin
                        ALUControl = 3'b001; //Se le indica a la ALU que realice una resta
                    end
                end
                
                //En caso de que sea una AND
                else if (Funct_Tres == 3'b111) begin
                    ALUControl = 3'b010; //Se le indica a la ALU que realice una AND
                end
                
                //En caso de que sea una XOR
                else if (Funct_Tres == 3'b100) begin
                    ALUControl = 3'b011; //Se le indica a la ALU que realice una XOR
                end
                
                //En caso de que sea un SLL (Logical Shift Left)
                else if (Funct_Tres == 3'b001) begin
                    ALUControl = 3'b100; //Se le indica a la ALU que realice un SLL
                end
            end
            
            //Instrucciones Formato S
            7'b0100011:
            begin
                //Se definen las salidas necesarias para una instruccion tipo S
                RegWrite = 1'b1;
                ALUControl = 3'b000;
                MemWrite = 1'b0;
                WDSrc = 1'b1;
                ImmReg = 1'b1;
                ALUSrc = 1'b0;
                MemToReg = 1'b0;
            end
            
            //Instrucciones Formato U
            7'b0110111:
            begin
                //Se definen las salidas necesarias para una instruccion tipo S
                RegWrite = 1'b1;
                MemWrite = 1'b0;
                WDSrc = 1'b0;
                MemToReg = 1'b0;
            end
            
            //Instrucciones Formato I, ADDI y LI
            7'b0100011:
            begin
                //Se definen las salidas necesarias para una instruccion tipo I para ADDI y LI
                RegWrite = 1'b1;
                ALUControl = 3'b000;
                MemWrite = 1'b0;
                WDSrc = 1'b1;
                ImmReg = 1'b0;
                ALUSrc = 1'b0;
                MemToReg = 1'b0;
            end
            
            //Instrucciones Formato I, LW
            7'b0100011:
            begin
                //Se definen las salidas necesarias para una instruccion tipo I para LW
                RegWrite = 1'b1;
                ALUControl = 3'b000;
                MemWrite = 1'b1;
                WDSrc = 1'b1;
                ImmReg = 1'b0;
                ALUSrc = 1'b0;
                MemToReg = 1'b1;
            end
        endcase
    end
endmodule
