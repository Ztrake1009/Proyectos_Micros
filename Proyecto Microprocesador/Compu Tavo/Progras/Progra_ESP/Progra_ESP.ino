#include <Stepper.h>

const int stepsPerRevolution = 200;  // Los Motores necesitan 200 pasos para dar una vuelta.
Stepper Motor_X(stepsPerRevolution, 2, 4, 16, 17); // Define los pines del Motor X.
Stepper Motor_Y(stepsPerRevolution, 19, 21, 22, 23); // Define los pines del Motor Y.

// Define el pin del Relay 1 para el motor DC (para moverlo hacia abajo).
const int Relay_A = 26;
// Define el pin del Relay 2 para el motor DC (para moverlo hacia arriba).
const int Relay_B = 27;
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

void setup() {
  Serial.begin(9600); // Inicia la comunicación serial.
  Motor_X.setSpeed(200); // Establece la velocidad del Motor X.
  Motor_Y.setSpeed(200); // Establece la velocidad del Motor Y.

  pinMode(2, OUTPUT);

  // Inicializa el pin del Relay 1 como salida.
  pinMode(Relay_A, OUTPUT);
  // Inicializa el pin del Relay 2 como salida.
  pinMode(Relay_B, OUTPUT);

  // Inicializa el pin del final de carrera alto.
  pinMode(final_Carrera_A, INPUT);
  // Inicializa el pin del final de carrera bajo.
  pinMode(final_Carrera_B, INPUT);

  // Inicializa el pin del Imán como salida.
  pinMode(Iman, OUTPUT);
  
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
        activarMotor = 1;
      }
      // Envía señal de finalización a Python.
      Serial.println("Motor_Listo");
    }
  }
  
  if (activarMotor == 0) {
    // Apaga el motor.
    digitalWrite(Relay_A, LOW);
    digitalWrite(Relay_B, LOW);
    //digitalWrite(2, LOW);
  }
  else if (activarMotor == 1) {
    // Activa el motor en dirección Horaria.
    digitalWrite(Relay_A, LOW);
    digitalWrite(Relay_B, HIGH);
  }
  else if (activarMotor == 2) {
    if (pasos == 1) {
    // Activa el imán.
      digitalWrite(Iman, HIGH);
    }

    else if (pasos == 2) {
    // Activa el imán.
      digitalWrite(Iman, LOW);
    }

    delay (3000); // Espera 3 segundos.

    // Activa el motor en dirección Antihoraria.
    digitalWrite(Relay_A, HIGH);
    digitalWrite(Relay_B, LOW);
    //digitalWrite(2, HIGH);
  }
}

void stop_Abajo() {
  // Apaga el motor.
  digitalWrite(Relay_A, LOW);
  digitalWrite(Relay_B, LOW);
  //digitalWrite(2, LOW);

  // Indica que el motor se mueva en dirección Antihoraria.
  activarMotor = 2;
}

void stop_Arriba() {
  // Apaga el motor.
  digitalWrite(Relay_A, LOW);
  digitalWrite(Relay_B, LOW);

  // Indica que el motor se apague.
  activarMotor = 0;
}