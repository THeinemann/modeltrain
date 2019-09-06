#include "speed_service.h"
#include "arduino_wrapper.h"

SpeedService::SpeedService(unsigned int en)
: en(en)
{
    setSpeed(0);
}

void SpeedService::setSpeed(unsigned int speed) {
    analogWrite(en, speed);
}
