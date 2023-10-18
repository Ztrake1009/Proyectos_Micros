`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
/*

Objetivo:
En este TestBench se espera simular correctamente el funcionamiento
de una ALU utilizando dos numeros de entrada y una señal de control.
Esta ALU debe realizar operaciones de Suma, Resta, AND, XOR y SLL
(Logical Shift Left).

*/  
//////////////////////////////////////////////////////////////////////////////////


module ALU_2to1_TB(
    );
    //Inputs
    reg [31:0] In_A, In_B; //Operando de A y B de la ALU
    reg [2:0] ALUControl; //Selector de operaciones
    
    //Outputs
    wire [31:0] Out_ALU; //Salida de la ALU
    
    //Instantiate
    //Llamado de variables en el modulo del testbench correspondiente
    ALU_2to1 UUT(
    .In_A(In_A),
    .In_B(In_B),
    .ALUControl(ALUControl),
    .Out_ALU(Out_ALU)
    );
    
    //Stimulus
    initial begin
        //Se definen operandos para realizar una suma 
        In_A = 32'd10; //32'h0000000A
        In_B = 32'd4; //32'h00000004
        ALUControl = 3'd0;
        //Resultado esperado: 32'd14
        
        #100
        //Se realiza una resta A-B
        ALUControl = 3'd1;
        //Resultado esperado: 32'd6
        
        //Se definen operandos para realizar una suma con un numero negativo (complemento a dos)
        In_A = 32'd10; //32'h0000000A
        In_B = 32'b11111111111111111111111111010000; //32'd-48
        ALUControl = 3'd0;
        //Resultado esperado: 32'd-38
        
        #100
        //Se realiza una resta A-B
        ALUControl = 3'd1;
        //Resultado esperado: 32'd58
        
        #100
        //Se definen operandos para realizar una AND
        ALUControl = 3'd2;
        In_A = 32'h0000FFFF;
        In_B = 32'h00001000;
        //Resultado esperado: 32'h00001000
        
        #100
        //Se realiza un XOR
        ALUControl=3'd3;
        In_A = 32'h0000FFFF;
        In_B = 32'hFFFFFFFF;
        //Resultado esperado: 32'hFFFF0000
        
        #100
        //Se realiza un SLL (Logical Shift Left)
        ALUControl=3'd4;
        In_A = 32'h0000000F;
        In_B = 32'd3;
        //Resultado esperado: 32'h00000078
        
        #100 
        $finish;
    end
endmodule
