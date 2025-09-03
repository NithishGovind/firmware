#include "CytronMotorDriver.h"

// Create Cytron Objects (PWM_DIR, PWM, DIR)
CytronMD motor1(PWM_DIR, 3,2);
CytronMD motor2(PWM_DIR, 5,4);
CytronMD motor3(PWM_DIR, 6,7);
CytronMD motor4(PWM_DIR, 9,8);

// ====== Motor Control Functions ======
void forward(int speed) {
  motor1.setSpeed(speed);
  motor2.setSpeed(speed);
  motor3.setSpeed(speed);
  motor4.setSpeed(speed);
}

void backward(int speed) {
  motor1.setSpeed(-speed);
  motor2.setSpeed(-speed);
  motor3.setSpeed(-speed);
  motor4.setSpeed(-speed);
}

void left(int speed) {
  motor1.setSpeed(-speed);
  motor2.setSpeed(speed);
  motor3.setSpeed(speed);
  motor4.setSpeed(-speed);
}

void right(int speed) {
  motor1.setSpeed(speed);
  motor2.setSpeed(-speed);
  motor3.setSpeed(-speed);
  motor4.setSpeed(speed);
}

void spinLeft(int speed) {
  motor1.setSpeed(-speed);
  motor2.setSpeed(speed);
  motor3.setSpeed(-speed);
  motor4.setSpeed(speed);
}

void spinRight(int speed) {
  motor1.setSpeed(speed);
  motor2.setSpeed(-speed);
  motor3.setSpeed(speed);
  motor4.setSpeed(-speed);
}

void stopMotors() {
  motor1.setSpeed(0);
  motor2.setSpeed(0);
  motor3.setSpeed(0);
  motor4.setSpeed(0);
}

void setup() {
  Serial.begin(115200);
  Serial.println("Robot Ready. Send commands: f,b,l,r,q,e,s");
}

void loop() {
  if (Serial.available()) {
    char cmd = Serial.read();

    switch (cmd) {
      case 'f': forward(200); break;   // forward
      case 'b': backward(200); break;  // backward
      case 'l': left(200); break;      // left
      case 'r': right(200); break;     // right
      case 'q': spinLeft(200); break;  // spin left
      case 'e': spinRight(200); break; // spin right
      case 's': stopMotors(); break;   // stop
    }
  }
}
