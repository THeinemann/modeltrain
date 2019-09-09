#ifndef __INTERFACE_HPP
#define __INTERFACE_HPP

#include "arduino_wrapper.hpp"
#include "interface.h"
#include "protocol.h"

template<class _Controller, unsigned int _delay>
InterfaceBase<_Controller, _delay>::InterfaceBase(_Controller& controller)
  : controller(controller)
{}

template<class _Controller, unsigned int _delay>
void InterfaceBase<_Controller, _delay>::process() {
  if (Serial.available()) {
    auto command = static_cast<protocol::Command>(Serial.read());
    unsigned int buffer_size = protocol::numberOfParameters(command);
    unsigned char buffer[buffer_size];
    unsigned int readBytes = Serial.readBytes(buffer, buffer_size);

    if (readBytes == buffer_size) {
      auto status = controller.receiveCommand(command, buffer);
      Serial.write(static_cast<uint8_t>(status));
    } else {
      Serial.write(static_cast<uint8_t>(protocol::INVALID_COMMAND));
    }

  }
  delay(_delay);
}


#endif
