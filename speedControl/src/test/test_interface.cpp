#include <gtest/gtest.h>
#include <ArduinoFake.h>

#include "../interface.hpp"

using namespace fakeit;

struct IController {
  virtual protocol::StatusCode receiveCommand(protocol::Command command, const unsigned char parameters[]) = 0;
};

const unsigned int DELAY = 1234;

class InterfaceTest : public ::testing::Test {
public:
  InterfaceTest()
    : controller(), interface(controller.get())
  {}

protected:
  Mock<IController> controller;
  InterfaceBase<IController, DELAY> interface;

  virtual void TearDown() {
    controller.Reset();
    ArduinoFake(Serial).Reset();
    ArduinoFake().Reset();
  }
};

TEST_F(InterfaceTest, shouldWaitIfNoSerialDataIsAvailable) {
  When(Method(ArduinoFake(Serial), available)).Return(0);
  When(Method(ArduinoFake(), delay)).AlwaysReturn();

  interface.process();

  Verify(Method(ArduinoFake(Serial), available)).Once();
  Verify(Method(ArduinoFake(), delay).Using(DELAY));
}

TEST_F(InterfaceTest, shouldPassCommandToController) {
  When(Method(ArduinoFake(Serial), available)).Return(2);
  When(Method(ArduinoFake(Serial), read)).Return(protocol::SET_DIRECTION);
  const unsigned char parameter = (unsigned char)(protocol::BACKWARD);
  When(Method(ArduinoFake(Serial), readBytes))
    .Do([](char buffer[], int length) -> int {
          buffer[0] = parameter;
          return 1;
        });

  When(Method(ArduinoFake(), delay)).AlwaysReturn();
  When(OverloadedMethod(ArduinoFake(Serial), write, size_t(uint8_t))).AlwaysReturn(1);
  unsigned char receivedParameter;

  When(Method(controller, receiveCommand))
    .Do([&receivedParameter](protocol::Command command, const unsigned char params[]) mutable -> protocol::StatusCode {
          receivedParameter = params[0];
          return protocol::OK;
        });

  interface.process();

  Verify(Method(ArduinoFake(Serial), available)).Once();
  Verify(Method(ArduinoFake(Serial), read)).Once();
  Verify(Method(ArduinoFake(Serial), readBytes)
         .Matching([](char buffer[], int length) { return length == 1; }))
         .Once();
  Verify(Method(controller, receiveCommand)
         .Matching([](protocol::Command command, const unsigned char[]) {
                     return command == protocol::SET_DIRECTION;
                   }))
         .Once();
  ASSERT_EQ(receivedParameter, parameter);
  Verify(Method(ArduinoFake(), delay).Using(DELAY));
  Verify(OverloadedMethod(ArduinoFake(Serial), write, size_t(uint8_t))
         .Using((uint8_t)protocol::OK))
         .Once();
}
