#include "direction_service.h"
#include "arduino_wrapper.hpp"


void DirectionService::setDirection(protocol::Direction direction) {
  digitalWrite(in1, LOW);
  digitalWrite(in2, LOW);

  if (direction == protocol::FORWARD) {
    digitalWrite(in1, LOW);
    digitalWrite(in2, HIGH);
  } else {
    digitalWrite(in1, HIGH);
    digitalWrite(in2, LOW);
  }
}
