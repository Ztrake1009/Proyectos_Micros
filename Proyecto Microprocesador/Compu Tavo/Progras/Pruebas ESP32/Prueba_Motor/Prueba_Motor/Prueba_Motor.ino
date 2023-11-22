#include <Stepper.h>

const int stepsPerRevolution = 200;  // Cambia esto según tu motor
Stepper Motor_X(stepsPerRevolution, 2, 4, 16, 17); // Define los pines del Motor en X
Stepper Motor_Y(stepsPerRevolution, 19, 21, 22, 23); // Define los pines del Motor en Y

bool Motor_X_Moved = false;
bool Motor_Y_Moved = false;

void setup() {
  Serial.begin(9600);  // Inicia la comunicación serial
  Motor_X.setSpeed(200);  // Establece la velocidad del motor
  Motor_Y.setSpeed(200);  // Establece la velocidad del motor
}

void loop() {
  if (Serial.available() > 0) {
    char comando = Serial.read();
    if ((comando == 'X')||(comando == 'Y')) {
      int pasos = Serial.parseInt();

      if (comando == 'X') {
        Motor_X.step(pasos);    // Mueve el motor A la cantidad de pasos especificada
        Motor_X_Moved = true;
      }
      else if (comando == 'Y') {
        Motor_Y.step(pasos);    // Mueve el motor B la cantidad de pasos especificada
        Motor_Y_Moved = true;
      }
      Serial.println("MotorListo");  // Envía señal de finalización a Python
    }
  }
}