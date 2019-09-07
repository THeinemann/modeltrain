#include "protocol.h"

namespace protocol {

unsigned int numberOfParameters(Command command) {
  switch(command) {
  case SET_DIRECTION:
    return 1;
  case SET_SPEED:
    return 1;
  default:
    return 0;
  }
}

}
