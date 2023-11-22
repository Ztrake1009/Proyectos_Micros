// Define el pin del Relay 1 para el motor DC (para moverlo hacia abajo).
const int relay_A = 26;
// Define el pin del Relay 2 para el motor DC (para moverlo hacia arriba).
const int relay_B = 27;
// Define el pin para el final de carrera alto (se presiona cuando baja la cremallera).
const int final_Carrera_A = 32;
// Define el pin para el final de carrera bajo (se presiona cuando sube la cremallera).
const int final_Carrera_B = 33;

volatile int activarMotor = 0; // Variable para indicar la activación del motor.

void setup() {
  Serial.begin(9600); // Inicia la comunicación serial.

  pinMode(2, OUTPUT);

  // Inicializa el pin del Relay 1 como salida.
  pinMode(relay_A, OUTPUT);
  // Inicializa el pin del Relay 2 como salida.
  pinMode(relay_B, OUTPUT);

  // Inicializa el pin del final de carrera alto.
  pinMode(final_Carrera_A, INPUT);
  // Inicializa el pin del final de carrera bajo.
  pinMode(final_Carrera_B, INPUT);

  // Configura la interrupción para que pare el movimiento cuando va hacia abajo.
  attachInterrupt(digitalPinToInterrupt(final_Carrera_A), stop_Abajo, RISING);
  // Configura la interrupción para que pare el movimiento cuando va hacia arriba.
  attachInterrupt(digitalPinToInterrupt(final_Carrera_B), stop_Arriba, RISING);
}

void loop() {
  if (activarMotor == 1) {    
    delay(5000); // Espera 5 segundos

    // Activar o desactivar el imán

    // Activa el motor
    digitalWrite(relay_A, HIGH);
    digitalWrite(relay_B, LOW);
    digitalWrite(2, HIGH);
  }

  else if (activarMotor == 2) {
    // Apaga el motor
    
    digitalWrite(relay_A, LOW);
    digitalWrite(relay_B, LOW);
    digitalWrite(2, LOW);

    /*
    delay(5000); // Espera 5 segundos

    // Activar o desactivar el imán

    // Activa el motor
    digitalWrite(relay_A, LOW);
    digitalWrite(relay_B, HIGH);
    */
  }
}


void stop_Abajo() {
  // Apaga el motor
  digitalWrite(relay_A, LOW);
  digitalWrite(relay_B, LOW);

  //delay (5000);

  //digitalWrite(relay_A, HIGH);
  //digitalWrite(relay_B, LOW);
  //digitalWrite(2, HIGH);


  //Serial.println(1);

  activarMotor = 1;
}

void stop_Arriba() {
  
  //digitalWrite(relay_A, LOW);
  //digitalWrite(relay_B, LOW);
  //digitalWrite(2, LOW);
  //delay(1000);
  
  activarMotor = 2;
  //Serial.println(0);
}
