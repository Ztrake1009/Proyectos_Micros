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
    input RST, //Reset del sistema
    output reg [31:0] PC_O,
    output reg [31:0] Instruction_O,
    output reg [31:0] new_PC_O,
    output reg [6:0] Funct7_O,
    output reg [2:0] Funct3_O,
    output reg [6:0] Opcode_O,
    output reg [4:0] RS1_O,
    output reg [4:0] RS2_O,
    output reg [4:0] RD_O,
    output reg [6:0] Imm_O,
    output reg [19:0] LUI_O,
    output reg [31:0] RD1_O,
    output reg [31:0] RD2_O,
    output reg [31:0] out_ALU_O,
    output reg [31:0] mux_ALU_O,
    output reg [4:0] mux_Imm_O,
    output reg [31:0] mux_WD_O,
    output reg [31:0] mux_MEM_O,
    output reg [11:0] out_Conc_O,
    output reg [31:0] out_Ext_Imm_O,
    output reg [31:0] out_Ext_LUI_O,
    output reg [31:0] out_MEM_O,
    output reg RegWrite_O,
    output reg [2:0] ALUControl_O,
    output reg MemWrite_O,
    output reg WDSrc_O,
    output reg ImmReg_O,
    output reg ALUSrc_O,
    output reg MemToReg_O
    );
    
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
    
    Instruction_Memory Intruction_Memory_1(PC, Instruction);
    
    Control_Unit Control_Unit_1(Instruction[31:25], Instruction[14:12], Instruction[6:0], RegWrite, ALUControl, MemWrite, WDSrc, ImmReg, ALUSrc, MemToReg);
    
    Register_File Register_File_1(CLK, RST, Instruction[19:15], Instruction[24:20], Instruction[11:7], mux_WD, RegWrite, RD1, RD2);
    
    Extend_20to32 Extend_20to32_1(Instruction[31:12], out_Ext_LUI);
    
    Mux_2to1 Mux_2to1_WD(out_Ext_LUI, mux_MEM, WDSrc, mux_WD);
    
    Mux_2to1 Mux_2to1_Imm(Instruction[24:20], Instruction[11:7], ImmReg, mux_Imm);
    
    Concatenar Concatenar_1(mux_Imm[4:0], Instruction[31:25], out_Conc);
    
    Extend_12to32 Extend_12to32_2(out_Conc, out_Ext_Imm);
    
    Mux_2to1 Mux_2to1_ALU(out_Ext_Imm, RD2, ALUSrc, mux_ALU);
    
    ALU_2to1 ALU_2to1_1(RD1, mux_ALU, ALUControl, out_ALU);
    
    Data_Memory Data_Memory_1(CLK, RST, out_ALU, RD2, MemWrite, out_MEM);

    Mux_2to1 Mux_2to1_MEM(out_ALU, out_MEM, MemToReg, mux_MEM);
    
    always @(*) begin //Siempre que exista un cambio 
        PC_O <= PC;
        Instruction_O <= Instruction;
        new_PC_O <= new_PC;
        Funct7_O <= Funct7;
        Funct3_O <= Funct3;
        Opcode_O <= Opcode;
        RS1_O <= RS1;
        RS2_O <= RS2;
        RD_O <= RD;
        Imm_O <= Imm;
        LUI_O <= LUI;
        RD1_O <= RD1;
        RD2_O <= RD2;
        out_ALU_O <= out_ALU;
        mux_ALU_O <= mux_ALU;
        mux_Imm_O <= mux_Imm;
        mux_Imm_O <= mux_Imm;
        mux_WD_O <= mux_WD;
        mux_MEM_O <= mux_MEM;
        out_Conc_O <= out_Conc;
        out_Ext_Imm_O <= out_Ext_Imm;
        out_Ext_LUI_O <= out_Ext_LUI;
        out_MEM_O <= out_MEM;
        RegWrite_O <= RegWrite;
        ALUControl_O <= ALUControl;
        MemWrite_O <= MemWrite;
        WDSrc_O <= WDSrc;
        ImmReg_O <= ImmReg;
        ALUSrc_O <= ALUSrc;
        MemToReg_O <= MemToReg;
    end
    
endmodule
