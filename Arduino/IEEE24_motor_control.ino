#define PI 3.1415926535897932384626433832795

//change this to motor's specifics
const int motor_speed = ;
const int en_left = ;
const int en_right = ;
const int in1_left = ;
const int in2_left = ;
const int in3_right = ;
const int in4_right = ;

void setup() {
   Serial.begin(9600);
   pinMode(en_left, OUTPUT);
   pinMode(in1_left, OUTPUT);
   pinMode(en_right, OUTPUT);
   pinMode(in2_left, OUTPUT);
   pinMode(in3_right, OUTPUT);
   pinMode(in4_right, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    //get direction and cm from pi
    String data = Serial.readStringUntil('\n');
    char direction = data[0];
    String s = data.substring(1);
    int cm = s.toInt()
    int steps = getStepsFromCm(cm);

    switch(direction){
      case "l":
        break;
      case "r":
        break;
      case "f":
        break;
      case "b":
        break;
    }
  }
}

getStepsFromCm(cm){
  //probably have to change this depending on motors
  steps = cm * (20 / PI);
  return steps
}

forward() {
  analogWrite(en_left, motorSpeed);
  digitalWrite(in1_left, HIGH);
  digitalWrite(in2_left, LOW);
  analogWrite(en_right, motorSpeed);
  digitalWrite(in3_right, HIGH);
  digitalWrite(in4_right, LOW);
}

backward(){
  analogWrite(en_left, motorSpeed);
  digitalWrite(in1_left, LOW);
  digitalWrite(in2_left, HIGH);
  analogWrite(en_right, motorSpeed);
  digitalWrite(in3_right, LOW);
  digitalWrite(in4_right, HIGH);
}

left(){
  analogWrite(en_left, motorSpeed);
  digitalWrite(in1_left, LOW);
  digitalWrite(in2_left, HIGH);
  analogWrite(en_right, motorSpeed);
  digitalWrite(in3_right, HIGH);
  digitalWrite(in4_right, LOW);
}

right(){
  analogWrite(en_left, motorSpeed);
  digitalWrite(in1_left, HIGH);
  digitalWrite(in2_left, LOW);
  analogWrite(en_right, motorSpeed);
  digitalWrite(in3_right, LOW);
  digitalWrite(in4_right, HIGH);
}
