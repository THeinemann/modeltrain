#ifndef __DIRECTION_SERVICE_H
#define __DIRECTION_SERVICE_H

#include "protocol.h"

class DirectionService {
public:
  DirectionService(unsigned int in1, unsigned int in2)
    : in1(in1), in2(in2)
  {}

  void setDirection(protocol::Direction direction);

private:
  const unsigned int in1;
  const unsigned int in2;
};

#endif
