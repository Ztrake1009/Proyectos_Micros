#include <Stepper.h>

const int stepsPerRevolution = 200;  // Los Motores necesitan 200 pasos para dar una vuelta.
Stepper Motor_X(stepsPerRevolution, 2, 4, 16, 17); // Define los pines del Motor X.
Stepper Motor_Y(stepsPerRevolution, 19, 21, 22, 23); // Define los pines del Motor Y.

// Define los pines del motor.
const int motor_Pin_A = 26;
const int motor_Pin_B = 27;
const int enable1Pin = 14;

// Set del PWM.
const int freq = 30000;
const int pwmChannel = 0;
const int resolution = 8;
const int dutyCycle = 200;

// Define el pin para el final de carrera alto (se presiona cuando baja la cremallera).
const int final_Carrera_A = 32;
// Define el pin para el final de carrera bajo (se presiona cuando sube la cremallera).
const int final_Carrera_B = 33;

// Define el pin para encender y apagar el imán.
const int Iman = 12;

// Variable para indicar la activación del motor en cierta dirección.
// 0 = Apagado.
// 1 = Dirección Horaria.
// 2 = Dirección Antihoraria.
volatile int activarMotor = 0;

volatile int pasos = 0;
int estado = 0;

void setup() {
  Serial.begin(9600); // Inicia la comunicación serial.
  Motor_X.setSpeed(200); // Establece la velocidad del Motor X.
  Motor_Y.setSpeed(200); // Establece la velocidad del Motor Y.

  // Inicializa los pines del motor como salidas.
  pinMode(motor_Pin_A, OUTPUT);
  pinMode(motor_Pin_B, OUTPUT);
  pinMode(enable1Pin, OUTPUT);

  // Configura las funciones PWM del LED.
  ledcSetup(pwmChannel, freq, resolution);
  
  // Configura el canal GPIO por ser controlado.
  ledcAttachPin(enable1Pin, pwmChannel);

  // Inicializa el pin del final de carrera alto.
  pinMode(final_Carrera_A, INPUT);
  // Inicializa el pin del final de carrera bajo.
  pinMode(final_Carrera_B, INPUT);

  // Inicializa el pin del Imán como salida.
  pinMode(Iman, OUTPUT);
  digitalWrite(Iman, LOW);
  
  // Configura la interrupción para que pare el movimiento cuando va hacia abajo.
  attachInterrupt(digitalPinToInterrupt(final_Carrera_A), stop_Abajo, RISING);
  // Configura la interrupción para que pare el movimiento cuando va hacia arriba.
  attachInterrupt(digitalPinToInterrupt(final_Carrera_B), stop_Arriba, RISING);
}

void loop() {
  if (Serial.available() > 0) {
    char comando = Serial.read();
    if ((comando == 'X')||(comando == 'Y')||(comando == 'Z')) {
      int pasos = Serial.parseInt();
      // Mueve el Motor X la cantidad de pasos especificada.
      if (comando == 'X') {
        Motor_X.step(pasos);
      }
      // Mueve el Motor Y la cantidad de pasos especificada.
      else if (comando == 'Y') {
        Motor_Y.step(pasos);
      }
      else if (comando == 'Z'){
        //pasos = 1;
        activarMotor = 1;
      }
      // Envía señal de finalización a Python.
      Serial.println("Motor_Listo");
    }
  }
  
  if (activarMotor == 0) {
    // Apaga el motor.
    digitalWrite(motor_Pin_A, LOW);
    digitalWrite(motor_Pin_B, LOW);
    ledcWrite(pwmChannel, dutyCycle);
    digitalWrite(Iman, LOW);
    estado = 0;
  }
  else if (activarMotor == 1) {
    // Activa el motor en dirección Horaria.
    digitalWrite(motor_Pin_A, HIGH);
    digitalWrite(motor_Pin_B, LOW);
    ledcWrite(pwmChannel, dutyCycle);
    Serial.println("esperando stop abajo");
    estado = 0;
    delay(5000);
  
   
    
  }
  else if (activarMotor == 2) {
    //digitalWrite(Iman, HIGH);
    /*
    delay (2000); // Espera 2 segundos.
    if (pasos == 1) {
    // Activa el imán.
      digitalWrite(Iman, HIGH);
    }

    else if (pasos == 2) {
    // Desactiva el imán.
      digitalWrite(Iman, LOW);
    }
    */
    delay (2000); //Espera 3 segundos.
    digitalWrite(Iman, HIGH);
    delay(2000); // Espera 2 s antes de subir.
    // Ahora sube el motor.
    activarMotor = 3;
    
  }
  else if (activarMotor == 3) {
    // Subir el motor, rotación antihoraria.
     // Espera 2 s antes de subir.
    // Ahora sube el motor.
    
    digitalWrite(motor_Pin_A, LOW);
    digitalWrite(motor_Pin_B, HIGH);
    ledcWrite(pwmChannel, dutyCycle);
    estado = 1;
    
  }


}

void stop_Abajo() {
  if (estado == 0){
    // Apaga el motor.
    digitalWrite(motor_Pin_A, LOW);
    digitalWrite(motor_Pin_B, LOW);
    ledcWrite(pwmChannel, dutyCycle);
    Serial.println("stop abajo");
    // Indica que funcione el iman
    activarMotor = 2;
  }
}

void stop_Arriba() {
  if (estado == 1){
    // Apaga el motor.
    digitalWrite(motor_Pin_A, LOW);
    digitalWrite(motor_Pin_B, LOW);
    ledcWrite(pwmChannel, dutyCycle);
    Serial.println("stop arriba");
    estado = 0;
    // Indica que el motor se apague.
    activarMotor = 0;
  }
}