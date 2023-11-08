void setup() {
   Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    String data = Serial.readStringUntil('\n');
    char direction = data[0];
    String s = data.substring(1);
    int cm = s.toInt()
  }
}
