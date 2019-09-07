#include "speed_service.h"
#include "arduino_wrapper.hpp"

SpeedService::SpeedService(unsigned int en)
: en(en)
{
    setSpeed(0);
}

void SpeedService::setSpeed(unsigned char speed) {
    analogWrite(en, speed);
}
