#include <gtest/gtest.h>
#include <fakeit/fakeit.hpp>
#include "../controller.hpp"
#include "../protocol.h"

struct IDirectionService {
    virtual void setDirection(unsigned int direction) = 0;
};

struct ISpeedService {
    virtual void setSpeed(unsigned char speed) = 0;
};

using namespace fakeit;

class ControllerTest : public ::testing::Test {
public:
    ControllerTest()
    : directionService(), speedService(), controller(directionService.get(), speedService.get())
    {}

protected:
    Mock<IDirectionService> directionService;
    Mock<ISpeedService> speedService;
    ControllerBase<IDirectionService, ISpeedService> controller;

    virtual void TearDown() {
        directionService.Reset();
        speedService.Reset();
    }
};

TEST_F(ControllerTest, shouldProcessSetSpeedCommand) {
    When(Method(speedService, setSpeed)).AlwaysReturn();

    unsigned char parameters[] = "\x12";
    auto status = controller.receiveCommand(protocol::SET_SPEED, parameters);
    EXPECT_EQ(status, protocol::OK);

    Verify(Method(speedService, setSpeed).Using(0x12));
}

TEST_F(ControllerTest, shouldProcessSetDirectionCommand) {
    When(Method(directionService, setDirection)).AlwaysReturn();

    unsigned char parameters[] = "\x0";
    auto status = controller.receiveCommand(protocol::SET_DIRECTION, parameters);
    EXPECT_EQ(status, protocol::OK);

    Verify(Method(directionService, setDirection).Using(protocol::FORWARD));
    directionService.Reset();
    When(Method(directionService, setDirection)).AlwaysReturn();

    unsigned char parameters2[] = "\x1";
    auto status2 = controller.receiveCommand(protocol::SET_DIRECTION, parameters2);
    EXPECT_EQ(status2, protocol::OK);

    Verify(Method(directionService, setDirection).Using(protocol::BACKWARD));
}

TEST_F(ControllerTest, shouldReturnClientErrorIfDirectionIsInvalid) {
    When(Method(directionService, setDirection)).AlwaysReturn();

    unsigned char parameters[] = "\x2";
    auto status = controller.receiveCommand(protocol::SET_DIRECTION, parameters);
    EXPECT_EQ(status, protocol::CLIENT_ERROR);

    Verify(Method(directionService, setDirection).Using(protocol::FORWARD)).Never();
}
