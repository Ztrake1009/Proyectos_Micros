#include <Stepper.h>

const int stepsPerRevolution = 200;  // Cambia esto según tu motor
Stepper myStepper(stepsPerRevolution, 16, 17, 18, 19); // Define los pines STEP y DIR

void setup() {
  Serial.begin(9600);  // Inicia la comunicación serial
  myStepper.setSpeed(200);  // Establece la velocidad del motor (cambia según tus necesidades)
}

void loop() {
  if (Serial.available() > 0) {
    int pasos = Serial.parseInt();  // Lee el valor de Python a través de la comunicación serial
    //int motor = Serial.parseInt();  // Lee el valor de Python a través de la comunicación serial
    if (pasos != 0) {
      //Serial.print("Recibido: ");
      //Serial.println(pasos);
      myStepper.step(pasos);   // Mueve el motor la cantidad de pasos especificada
    }
  }
}
