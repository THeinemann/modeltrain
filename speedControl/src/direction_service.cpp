#include "direction_service.h"
#include "arduino_wrapper.h"


void DirectionService::setDirection(unsigned int direction) {
  digitalWrite(in1, LOW);
  digitalWrite(in2, LOW);

  if (direction == FORWARD) {
    digitalWrite(in1, LOW);
    digitalWrite(in2, HIGH);
  } else {
    digitalWrite(in1, HIGH);
    digitalWrite(in2, LOW);
  }
}
