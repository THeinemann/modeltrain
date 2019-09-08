#ifndef __INTERFACE_H
#define __INTERFACE_H

#include "controller.h"

const unsigned int DELAY = 250;

template<class _Controller, unsigned int delayTime>
class InterfaceBase {
public:
  InterfaceBase(_Controller& controller);

  void process();

private:
  _Controller& controller;
};

typedef InterfaceBase<Controller, DELAY> Interface;

#endif
