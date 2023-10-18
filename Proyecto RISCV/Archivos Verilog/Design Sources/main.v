`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
/*

Funcionalidad:
En este bloque se espera ejecutar el funcionamiento del bloque principal,
donde se conectan todos los bloques secundarios para el correcto funcionamiento
de la microarquitectura RISCV32.

Entradas:
Variable CLK (Reloj del sistema).
Variable RST (Reset del sistema).

Salidas:
Variable Out_ALU (Sale la operacion realizada por la ALU).

Razon:
Se crea para poder conectar todos los bloques secundarios de la microarquitectura.

*/
//////////////////////////////////////////////////////////////////////////////////


module main(
    input CLK, //Reloj del sistema
    input RST //Reset del sistema
    );
    
    //reg [31:0] initial_PC = 32'h0;
    wire [31:0] PC;
    wire [31:0] Instruction;
    wire [31:0] new_PC;
    wire [6:0] Funct7;
    wire [2:0] Funct3;
    wire [6:0] Opcode;
    wire [4:0] RS1;
    wire [4:0] RS2;
    wire [4:0] RD;
    wire [6:0] Imm;
    wire [19:0] LUI;
    wire [31:0] RD1;
    wire [31:0] RD2;
    wire [31:0] out_ALU;
    wire [31:0] mux_ALU;
    wire [4:0] mux_Imm;
    wire [31:0] mux_WD;
    wire [31:0] mux_MEM;
    wire [11:0] out_Conc;
    wire [31:0] out_Ext_Imm;
    wire [31:0] out_Ext_LUI;
    wire [31:0] out_MEM;
    wire RegWrite;
    wire [2:0] ALUControl;
    wire MemWrite;
    wire WDSrc;
    wire ImmReg;
    wire ALUSrc;
    wire MemToReg;
    
    assign Funct7 = Instruction[31:25];
    assign Funct3 = Instruction[14:12];
    assign Opcode = Instruction[6:0];
    assign RS1 = Instruction[19:15];
    assign RS2 = Instruction[24:20];
    assign RD = Instruction[11:7];
    assign Imm = Instruction[31:25];
    assign LUI = Instruction[31:12];

    Save_PC Save_PC_1(CLK, RST, new_PC, PC);
    
    PCplus4 PCplus4_1(PC, new_PC);
    
    Instruction_Memory Intruction_Memory_1(PC, Instruccion);
    
    Control_Unit Control_Unit_1(Funct7, Funct3, Opcode, RegWrite, ALUControl, MemWrite, WDSrc, ImmReg, ALUSrc, MemToReg);
    
    Register_File Register_File_1(CLK, RST, RS1, RS2, RD, mux_WD, RegWrite, RD1, RD2);
    
    Extend_20to32 Extend_20to32_1(LUI, out_Ext_LUI);
    
    Mux_2to1 Mux_2to1_WD(out_Ext_LUI, mux_MEM, WDSrc, mux_WD);
    
    Mux_2to1 Mux_2to1_Imm(RS2, RD, ImmReg, mux_Imm);
    
    Concatenar Concatenar_1(mux_Imm[4:0], Imm, out_Conc);
    
    Extend_12to32 Extend_12to32_2(out_Conc, out_Ext_Imm);
    
    Mux_2to1 Mux_2to1_ALU(out_Ext_Imm, RD2, ALUSrc, mux_ALU);
    
    ALU_2to1 ALU_2to1_1(RD1, mux_ALU, ALUControl, out_ALU);
    
    Data_Memory Data_Memory_1(CLK, RST, out_ALU, RD2, MemWrite, out_MEM);

    Mux_2to1 Mux_2to1_MEM(out_ALU, out_MEM, MemToReg, mux_MEM);
    
endmodule
