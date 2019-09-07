
#include "controller.hpp"

Result<protocol::Direction, bool> getDirection(unsigned char directionAsChar) {
    switch(directionAsChar) {
        case '\0':
            return Result<protocol::Direction, bool>(protocol::FORWARD);
        case '\1':
            return Result<protocol::Direction, bool>(protocol::BACKWARD);
    }
    return Result<protocol::Direction, bool>(false);
}

template class ControllerBase<DirectionService, SpeedService>;
