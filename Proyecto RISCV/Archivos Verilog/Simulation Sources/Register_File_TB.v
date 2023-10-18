`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
/*

Objetivo:
En este TestBench se espera simular correctamente el funcionamiento
del Register File, como las funciones de lectura y escritura.

*/
//////////////////////////////////////////////////////////////////////////////////


module Register_File_TB(
    );
    //Inputs
    reg CLK; //Clock
    reg RST; //Reset
    reg [4:0] A1; //Registro Rs1
    reg [4:0] A2; //Registro Rs2
    reg [4:0] A3; //Registro Destino Rd
    reg [31:0] WD; //Write Data
    reg RegWrite; //Write Enable
    
    //Outputs
    wire [31:0] RD1; //Contenido del Registro Rs1
    wire [31:0] RD2; //Contenido del Registro Rs2

    //Instantiate
    //Llamado de variables en el modulo del testbench correspondiente
    Register_File UUT(
    .CLK(CLK),
    .RST(RST),
    .A1(A1),
    .A2(A2),
    .A3(A3),
    .WD(WD),
    .RegWrite(RegWrite),
    .RD1(RD1),
    .RD2(RD2)
    );
    
    //Stimulus
    initial begin
        CLK = 0;
        RST = 1; //Se prueba el Reset 
        
        #100
        RST = 0;
        
        //Pruebas de escritura de datos en registros

        #100        
        //Los valores A1 y A2 pueden ser cualquier numero ya que
        //en esta parte se prueba la escritura usando el WD
        A1 = 5'd0;
        A2 = 5'd0;
        
        //Se habilita la escritura
        RegWrite = 1;
        
        //Prueba de escritura en el registro 1, el valor 30 en decimal 
        A3 = 5'd1;
        WD = 32'd30;
        /*
        Resultados esperados:
        RD1 = 32'd0
        RD2 = 32'd0
        */
        
        #100
        //Prueba de escritura en el registro 2, el valor 15 en decimal
        A3 = 5'd2;
        WD = 32'd15;
        /*
        Resultados esperados:
        RD1 = 32'd0
        RD2 = 32'd0
        */
        
        #100
        //Prueba de escritura en el registro 3, el valor 25 en decimal
        A3 = 5'd3;
        WD = 32'd25;
        /*
        Resultados esperados:
        RD1 = 32'd0
        RD2 = 32'd0
        */
        
        #100
        //Prueba de escritura en el registro 4, el valor 5 en decimal
        A3 = 5'd4;
        WD = 32'd5;
        /*
        Resultados esperados:
        RD1 = 32'd0
        RD2 = 32'd0
        */
        
        #100
        //Prueba de escritura en el registro 5, el valor 18 en decimal
        A3 = 5'd5;
        WD = 32'd18;
        /*
        Resultados esperados:
        RD1 = 32'd0
        RD2 = 32'd0
        */
        
        #100
        //Prueba de escritura en el registro 0, el valor 18 en decimal
        A3 = 5'd0;
        WD = 32'd18;
        /*
        Resultados esperados:
        Como se restringio la escritura en el registro 0, aunque se
        haga en el testbench, internamente no realiza la escritura
        RD1 = 32'd0
        RD2 = 32'd0
        */
        
        //Pruebas de lectura de los datos en los registros
        
        #100
        //Se deshabilita la escritura
        RegWrite = 0;

        //Prueba de lectura de los registros 3 y 1
        A1 = 5'd3; //Se lee el registro 3
        A2 = 5'd1; //Se lee el registro 1
        /*
        Resultados esperados:
        RD1 = 32'd25
        RD2 = 32'd30
        */
                
        #100
        //Prueba de lectura de los registros 2 y 0
        A1 = 5'd2; //Se lee el registro 2
        A2 = 5'd0; //Se lee el registro 0
        /*
        Resultados esperados:
        RD1 = 32'd15
        RD2 = 32'd0
        */
        
        //Se prueba la escritura de datos en un registro
        #100
        RegWrite = 1;
        A1 = 5'd3; //Se lee el registro 3, es decir, el valor 32'd25
        A2 = 5'd4; //Se lee el registro 4, es decir, el valor 32'd5
        A3 = 5'd6; //Se escribe en el registro 6
        WD = 32'd4; //Valor a guardar en el registro 6, es decir, el valor 32'd4
        /*
        Resultados esperados:
        Debido a que A1 y A2 estan leyendo los valores de los registros
        3 y 4 respectivamente, se esperan estos valores a la salida
        RD1 = 32'd25
        RD2 = 32'd5
        */
        
        #100 
        $finish;
    end
    always #20 CLK = ~CLK; //Se genera el Clock
endmodule
