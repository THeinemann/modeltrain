#include <gtest/gtest.h>
#include <ArduinoFake.h>

#include "../direction_service.h"

using namespace fakeit;

class DirectionServiceTest : public ::testing::Test {
public:
    DirectionServiceTest()
    : ::testing::Test(), directionService(1, 2)
    {}

protected:
    virtual void SetUp() {
        When(Method(ArduinoFake(), digitalWrite)).AlwaysReturn();
    }

    virtual void TearDown() {
        ArduinoFake().Reset();
    }

    DirectionService directionService;
};

TEST_F(DirectionServiceTest, changeDirectionToForward) {
    directionService.setDirection(protocol::FORWARD);
    Verify(Method(ArduinoFake(), digitalWrite).Using(1, LOW));
    Verify(Method(ArduinoFake(), digitalWrite).Using(2, LOW));
    Verify(Method(ArduinoFake(), digitalWrite).Using(2, HIGH)).Once();
    Verify(Method(ArduinoFake(), digitalWrite).Using(1, HIGH)).Never();
}

TEST_F(DirectionServiceTest, changeDirectionToBackward) {
    directionService.setDirection(protocol::BACKWARD);
    Verify(Method(ArduinoFake(), digitalWrite).Using(1, LOW));
    Verify(Method(ArduinoFake(), digitalWrite).Using(2, LOW));
    Verify(Method(ArduinoFake(), digitalWrite).Using(1, HIGH)).Once();
    Verify(Method(ArduinoFake(), digitalWrite).Using(2, HIGH)).Never();
}
