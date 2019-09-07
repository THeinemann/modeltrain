#ifndef __CONTROLLER_HPP
#define __CONTROLLER_HPP

#include "controller.h"

template<class _DirectionService, class _SpeedService>
ControllerBase<_DirectionService, _SpeedService>::ControllerBase(_DirectionService& directionService,
     _SpeedService& speedService)
     : directionService(directionService), speedService(speedService)
 {}


template<class _DirectionService, class _SpeedService>
protocol::StatusCode ControllerBase<_DirectionService, _SpeedService>::receiveCommand(protocol::Command command,
    const unsigned char parameters[]) {
    switch(command) {
    case protocol::SET_SPEED:
      speedService.setSpeed(parameters[0]);
      break;
    case protocol::SET_DIRECTION: {
      auto direction = getDirection(parameters[0]);
      if (direction.isSuccessful()) {
        directionService.setDirection(direction.get());
        break;
      } else {
        return protocol::CLIENT_ERROR;
      }
    }
    default:
      return protocol::INVALID_COMMAND;
    }
    return protocol::OK;
}

#endif
