
#include "CytronMotorDriver.h"

// Create Cytron Objects (PWM_DIR, PWM, DIR)
CytronMD motor1(PWM_DIR, 2, 3);
CytronMD motor2(PWM_DIR, 4, 5);
CytronMD motor3(PWM_DIR, 6, 7);
CytronMD motor4(PWM_DIR, 8, 9);

// ====== Motor Control Functions ======

// Move Forward
void forward(int speed) {
  motor1.setSpeed(speed);
  motor2.setSpeed(speed);
  motor3.setSpeed(speed);
  motor4.setSpeed(speed);
}

// Move Backward
void backward(int speed) {
  motor1.setSpeed(-speed);
  motor2.setSpeed(-speed);
  motor3.setSpeed(-speed);
  motor4.setSpeed(-speed);
}

// Move Left (like strafing)
void left(int speed) {
  motor1.setSpeed(-speed);
  motor2.setSpeed(speed);
  motor3.setSpeed(speed);
  motor4.setSpeed(-speed);
}

// Move Right (like strafing)
void right(int speed) {
  motor1.setSpeed(speed);
  motor2.setSpeed(-speed);
  motor3.setSpeed(-speed);
  motor4.setSpeed(speed);
}

// Spin Left (rotate in place CCW)
void spinLeft(int speed) {
  motor1.setSpeed(-speed);
  motor2.setSpeed(speed);
  motor3.setSpeed(-speed);
  motor4.setSpeed(speed);
}

// Spin Right (rotate in place CW)
void spinRight(int speed) {
  motor1.setSpeed(speed);
  motor2.setSpeed(-speed);
  motor3.setSpeed(speed);
  motor4.setSpeed(-speed);
}

// Stop Motors
void stopMotors() {
  motor1.setSpeed(0);
  motor2.setSpeed(0);
  motor3.setSpeed(0);
  motor4.setSpeed(0);
}

void setup() {
  Serial.begin(115200);
  Serial.println("Basic Motor Control Ready!");
}

void loop() {
  // Example Test Sequence
  forward(200);
  delay(2000);

  backward(200);
  delay(2000);

  left(200);
  delay(2000);

  right(200);
  delay(2000);

  spinLeft(200);
  delay(2000);

  spinRight(200);
  delay(2000);

  stopMotors();
  delay(3000);
}
