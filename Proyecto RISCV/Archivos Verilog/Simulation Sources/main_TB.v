`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
/*

Objetivo:
En este TestBench se espera simular correctamente el funcionamiento de la
microarquitectura completa utilizando los bloques separados.

*/
//////////////////////////////////////////////////////////////////////////////////


module main_TB(
    );
    //Inputs
    reg CLK; //Clock
    reg RST; //Reset
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
    
    //Instantiate
    //Llamado de variables en el modulo del testbench correspondiente
    /*
    main UUT(
    .CLK(CLK),
    .RST(RST)
    );
    */
    main UUT (.CLK(CLK),.RST(RST),.PC_O(PC),.Instruction_O(Instruction),.new_PC_O(new_PC),.Funct7_O(Funct7)
    ,.Funct3_O(Funct3),.Opcode_O(Opcode),.RS1_O(RS1),.RS2_O(RS2),.RD_O(RD),.Imm_O(Imm),.LUI_O(LUI),.RD1_O(RD1),.RD2_O(RD2)
    ,.out_ALU_O(out_ALU),.mux_ALU_O(mux_ALU),.mux_Imm_O(mux_Imm),.mux_WD_O(mux_WD),.mux_MEM_O(mux_MEM),.out_Conc_O(out_Conc)
    ,.out_Ext_Imm_O(out_Ext_Imm),.out_Ext_LUI_O(out_Ext_LUI),.out_MEM_O(out_MEM),.RegWrite_O(RegWrite),.ALUControl_O(ALUControl)
    ,.MemWrite_O(MemWrite),.WDSrc_O(WDSrc),.ImmReg_O(ImmReg),.ALUSrc_O(ALUSrc),.MemToReg_O(MemToReg)); 

    integer file = 0; //Variable interna para abrir el archivo
    integer i = 0; //Variable interna, contador
    
    //Stimulus
    initial begin
        RST = 0;
        CLK = 0;
        
        #10
        RST = 1;
        
        #10
        RST = 0;
        
        #345
        file = $fopen("MEM_DUMP.txt","w");
        $fwrite(file, "Dirección   Valor\n");
        
        for (i=0; i<256; i=i+1) begin //Ciclo que recorre la Data Memory                 
            if (i%4 == 0 ) begin
                $fwrite(file, "0x%h  0x%h\n", i, UUT.Data_Memory_1.RAM[i]); //Escritura  
            end    
        end
        
        $fclose(file);
        $stop;
        
        #10
        $finish;

    end
    always #5 CLK = ~CLK;
endmodule

/*
Resultados Esperados:
Direccion   Valor
0x000000EC  0x0000abcd
0x000000D0  0x00000015
0x000000D4  0x00000700
0x000000D8  0xFFFFF90E
0x000000DC  0x0000000E
0x000000E0  0x00000009
0x000000E4  0x00000007
0x000000E8  0x0000000E


*/
