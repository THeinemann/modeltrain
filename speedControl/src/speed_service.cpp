#include "speed_service.h"
#include "arduino_wrapper.hpp"

SpeedService::SpeedService(unsigned int en)
: en(en)
{}

void SpeedService::setSpeed(unsigned char speed) {
    analogWrite(en, speed);
}
