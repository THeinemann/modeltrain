#include "interface.h"
#include "arduino_wrapper.hpp"

auto directionService = DirectionService(6, 7);
auto speedService = SpeedService(9);

auto controller = Controller(directionService, speedService);
auto interface = Interface(controller);

extern "C" {
void setup() {
  Serial.begin(9600);
  directionService.setDirection(protocol::FORWARD);
  speedService.setSpeed(0);
}

void loop() {
  interface.process();
}

}
