String dataString = "";
bool dataComplete = false;
int ledState = 0;

const int ledPin = 23;



void setup() {
  Serial.begin(9600);
  
  pinMode(ledPin, OUTPUT);
  digitalWrite(ledPin, LOW);
}

void loop() {
  if (Serial.available()) {
    serialEvent();
  }

  if (dataComplete) {
    ledState = dataString.toInt();

    // Tarea por realizar
    task();

    dataString = "";
    dataComplete = false;
  }
}

void serialEvent() {
  while (Serial.available()) {
    char inChar = (char)Serial.read();
    dataString += inChar;
    if (inChar == '\n') {
      dataComplete = true;
    }
  }
}

void task() {
  if (ledState == 1) {
    digitalWrite(ledPin, HIGH);
  }
  else {
    digitalWrite(ledPin, LOW);
  }
}