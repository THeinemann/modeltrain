#ifndef __CONTROLLER_H
#define __CONTROLLER_H

#include "direction_service.h"
#include "speed_service.h"
#include "protocol.h"
#include "util/optional.h"

optional<protocol::Direction> getDirection(unsigned char directionAsChar);

template<class _DirectionService, class _SpeedService>
class ControllerBase {
public:
  ControllerBase(_DirectionService& directionService, _SpeedService& speedService);

  protocol::StatusCode receiveCommand(protocol::Command command, const unsigned char parameters[]);
private:
  _DirectionService& directionService;
  _SpeedService& speedService;
};

typedef ControllerBase<DirectionService, SpeedService> Controller;

#endif
