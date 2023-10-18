`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
/*

Objetivo:
En este TestBench se espera simular correctamente el funcionamiento
del Control Unit, la cual controla todos los MUXes, habilita los bloques
e inclusive le indica a la ALU que operacion realizar.

*/ 
//////////////////////////////////////////////////////////////////////////////////


module Control_Unit_TB(
    );
    //Inputs
    reg [6:0] Funct7; //Funct7 necesario para diferenciar entre ADD y SUB para instrucciones tipo R
    reg [2:0] Funct3; //Funct3 para seleccionar la operacion
    reg [6:0] Opcode; //Opcode necesario para determinar el formato de la instruccion por realizar
    
    //Outputs
    wire RegWrite; //Salida para habilitar la escritura en registro destino
    wire [2:0] ALUControl; //Salida para seleccionar la operacion a realizar por la ALU
    wire MemWrite; //Salida para habilitar la escritura en memoria
    wire WDSrc; //Salida para activar el MUX que controla si se hacen operaciones tipo U o las otras
    wire ImmReg; //Salida para activar el MUX que controla si se hacen operaciones tipo S o tipo I
    wire ALUSrc; //Salida para activar el MUX que controla si se hacen operaciones tipo S-I o tipo R
    wire MemToReg; //Salida para activar el MUX que controla si se hacen loaders o las otras operaciones
    
    //Instantiate
    //Llamado de variables en el modulo del testbench correspondiente
    Control_Unit UUT(
    .Funct7(Funct7),
    .Funct3(Funct3),
    .Opcode(Opcode),
    .RegWrite(RegWrite),
    .ALUControl(ALUControl),
    .MemWrite(MemWrite),
    .WDSrc(WDSrc),
    .ImmReg(ImmReg),
    .ALUSrc(ALUSrc),
    .MemToReg(MemToReg)
    );
    
    //Stimulus
    initial begin
        //Prueba de instruccion tipo R, para realizar una operacion ADD
        Funct7 = 7'b0000000;
        Funct3 = 3'b000;
        Opcode = 7'b0110011;
        /*
        Resultados esperados:
        RegWrite = 1'b1
        ALUControl = 3'b000
        MemWrite = 1'b0
        WDSrc = 1'b1
        ImmReg = X
        ALUSrc = 1'b1
        MemToReg = 1'b0
        */
        
        #100
        //Prueba de instruccion tipo R, para realizar una operacion SUB
        Funct7 = 7'b0100000;
        Funct3 = 3'b000;
        Opcode = 7'b0110011;
        /*
        Resultados esperados:
        RegWrite = 1'b1
        ALUControl = 3'b001
        MemWrite = 1'b0
        WDSrc = 1'b1
        ImmReg = X
        ALUSrc = 1'b1
        MemToReg = 1'b0
        */
        
        #100
        //Prueba de instruccion tipo R, para realizar una operacion AND
        Funct7 = 7'bX;
        Funct3 = 3'b111;
        Opcode = 7'b0110011;
        /*
        Resultados esperados:
        RegWrite = 1'b1
        ALUControl = 3'b010
        MemWrite = 1'b0
        WDSrc = 1'b1
        ImmReg = 1'bX
        ALUSrc = 1'b1
        MemToReg = 1'b0
        */
        
        #100
        //Prueba de instruccion tipo R, para realizar una operacion XOR
        Funct7 = 7'bX;
        Funct3 = 3'b100;
        Opcode = 7'b0110011;
        /*
        Resultados esperados:
        RegWrite = 1'b1
        ALUControl = 3'b011
        MemWrite = 1'b0
        WDSrc = 1'b1
        ImmReg = 1'bX
        ALUSrc = 1'b1
        MemToReg = 1'b0
        */
        
        #100
        //Prueba de instruccion tipo R, para realizar una operacion SLL
        Funct7 = 7'bX;
        Funct3 = 3'b001;
        Opcode = 7'b0110011;
        /*
        Resultados esperados:
        RegWrite = 1'b1
        ALUControl = 3'b100
        MemWrite = 1'b0
        WDSrc = 1'b1
        ImmReg = 1'bX
        ALUSrc = 1'b1
        MemToReg = 1'b0
        */
        
        #100
        //Prueba de instruccion tipo S, para realizar una operacion SW
        Funct7 = 7'bX;
        Funct3 = 3'b010;
        Opcode = 7'b0100011;
        /*
        Resultados esperados:
        RegWrite = 1'b0
        ALUControl = 3'b000
        MemWrite = 1'b1
        WDSrc = 1'bX
        ImmReg = 1'b1
        ALUSrc = 1'b0
        MemToReg = 1'b0
        */
        
        #100
        //Prueba de instruccion tipo U, para realizar una operacion LUI
        Funct7 = 7'bX;
        Funct3 = 3'bX;
        Opcode = 7'b0110111;
        /*
        Resultados esperados:
        RegWrite = 1'b1
        ALUControl = 3'bX
        MemWrite = 1'b0
        WDSrc = 1'b0
        ImmReg = 1'bX
        ALUSrc = 1'bX
        MemToReg = 1'b0
        */
        
        #100
        //Prueba de instruccion tipo I, para realizar una operacion ADDI
        Funct7 = 7'bX;
        Funct3 = 3'b111;
        Opcode = 7'b0010011;
        /*
        Resultados esperados:
        RegWrite = 1'b1
        ALUControl = 3'bX
        MemWrite = 1'b0
        WDSrc = 1'b0
        ImmReg = 1'bX
        ALUSrc = 1'bX
        MemToReg = 1'b0
        */
        
        #100
        //Prueba de instruccion tipo I, para realizar una operacion LI
        Funct7 = 7'bX;
        Funct3 = 3'b000;
        Opcode = 7'b0010011;
        /*
        Resultados esperados:
        RegWrite = 1'b1
        ALUControl = 3'b000
        MemWrite = 1'b0
        WDSrc = 1'b1
        ImmReg = 1'b0
        ALUSrc = 1'b0
        MemToReg = 1'b0
        */
        
        #100
        //Prueba de instruccion tipo I, para realizar una operacion LW
        Funct7 = 7'bX;
        Funct3 = 3'b010;
        Opcode = 7'b0000011;
        /*
        Resultados esperados:
        RegWrite = 1'b1
        ALUControl = 3'b000
        MemWrite = 1'b0
        WDSrc = 1'b1
        ImmReg = 1'b0
        ALUSrc = 1'b0
        MemToReg = 1'b1
        */
        
        #100 
        $finish;
    end
endmodule
