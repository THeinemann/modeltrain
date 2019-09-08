#ifndef __PROTOCOL_H
#define __PROTOCOL_H

namespace protocol {

  enum Command {
                SET_SPEED = 0,
                SET_DIRECTION = 1
  };

  enum Direction {
                  FORWARD = 0,
                  BACKWARD = 1
  };

  enum StatusCode {
                   OK = 20,
                   CLIENT_ERROR = 40,
                   INVALID_COMMAND = 44,
                   INTERNAL_ERROR = 50
  };

  unsigned int numberOfParameters(Command command);

}

#endif
