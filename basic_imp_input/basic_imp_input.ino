#include "CytronMotorDriver.h"

// Configure the motor drivers
CytronMD motor1(PWM_DIR, 3, 2);  // PWM = Pin 3, DIR = Pin 2
CytronMD motor2(PWM_DIR, 5, 4);  // PWM = Pin 5, DIR = Pin 4
CytronMD motor3(PWM_DIR, 6, 7);  // PWM = Pin 6, DIR = Pin 7
CytronMD motor4(PWM_DIR, 9, 8);  // PWM = Pin 9, DIR = Pin 8

void setup() {
  // nothing needed here
    // Move forward at 50% speed for 5 seconds
  motor1.setSpeed(128);
  motor2.setSpeed(128);
  motor3.setSpeed(128);
  motor4.setSpeed(128);
  delay(5000);

  // Move backward at 50% speed for 5 seconds
  motor1.setSpeed(-128);
  motor2.setSpeed(-128);
  motor3.setSpeed(-128);
  motor4.setSpeed(-128);
  delay(5000);

  // Stop for 2 seconds
  motor1.setSpeed(0);
  motor2.setSpeed(0);
  motor3.setSpeed(0);
  motor4.setSpeed(0);
  delay(2000);
}

void loop() {

}
