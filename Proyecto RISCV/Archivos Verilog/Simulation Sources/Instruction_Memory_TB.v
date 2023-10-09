`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 08.10.2023 14:48:06
// Design Name: 
// Module Name: Instruction_Memory_TB
// Project Name: 
// Target Devices: 
// Tool Versions: 
// Description: 
// 
// Dependencies: 
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
//////////////////////////////////////////////////////////////////////////////////


module Instruction_Memory_TB(
    );
    
    //Inputs
    reg clk = 0; //Reloj
    reg rst = 0; //Reset 
    reg[31:0] Dir; //Direccion de la instruccion
        
    //Outputs
    wire[31:0] Inst; //Instruccion en la direccion
    
    //Instantiate
    //Llamado de variables en el modulo del testbench correspondiente
    Instruction_Memory UUT(
    .clk(clk),
    .rst(rst),
    .Dir(Dir), 
    .Inst(Inst)
    );
    
    //Stimulus
    initial begin
    clk = 0;
    rst = 0;
    
    //Se revisan diferentes direcciones de memoria como prueba
    Dir = 32'd0;
    #10 Dir = 32'd1;
    #10 Dir = 32'd2;
    #10 Dir = 32'd3;
    #10 Dir = 32'd4;
    #10 Dir = 32'd5;
    #10;
    /*
    #10 Dir = 32'd6;
    #10 Dir = 32'd7;
    #10 Dir = 32'd8;
    #10 Dir = 32'd9;
    #10 Dir = 32'd10;
    #10 Dir = 32'd11;
    #10 Dir = 32'd12;
    #10 Dir = 32'd13;
    #10 Dir = 32'd14;
    #10 Dir = 32'd15;
    #10 Dir = 32'd16;
    #10 Dir = 32'd17;
    #10 Dir = 32'd18;
    #10 Dir = 32'd19;
    #10 Dir = 32'd20;
    #10 Dir = 32'd21;
    #10 Dir = 32'd22;
    #10 Dir = 32'd23;
    #10 Dir = 32'd24;
    #10 Dir = 32'd25;
    #10 Dir = 32'd26;
    #10 Dir = 32'd27;
    #10 Dir = 32'd28;
    #10 Dir = 32'd29;
    #10 Dir = 32'd30;
    #10 Dir = 32'd31;
    #10 Dir = 32'd32;
    #10 Dir = 32'd33;
    #10 Dir = 32'd34;
    */
    $finish;
    end
    
    always #10 clk = clk + 1;

endmodule
