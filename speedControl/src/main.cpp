#include "interface.h"

auto directionService = DirectionService(6, 7);
auto speedService = SpeedService(9);

auto controller = Controller(directionService, speedService);
auto interface = Interface(controller);

extern "C" {
void setup() {
  directionService.setDirection(protocol::FORWARD);
  speedService.setSpeed(0);
}

void loop() {
  interface.process();
}

}
