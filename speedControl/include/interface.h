#ifndef __INTERFACE_H
#define __INTERFACE_H

#include "controller.h"

template<class _Controller, unsigned int delayTime>
class InterfaceBase {
   public:
      InterfaceBase(_Controller& controller);

        void process();

      private:
     _Controller& controller;
  };

  typedef InterfaceBase<Controller, 1500> Interface;

#endif
