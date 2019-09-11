
#include "controller.hpp"

optional<protocol::Direction> getDirection(unsigned char directionAsChar) {
    switch(directionAsChar) {
        case '\0':
            return optional<protocol::Direction>(protocol::FORWARD);
        case '\1':
            return optional<protocol::Direction>(protocol::BACKWARD);
    }
    return optional<protocol::Direction>();
}

template class ControllerBase<DirectionService, SpeedService>;
