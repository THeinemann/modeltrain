#ifdef TEST
#include <gtest/gtest.h>
#include <ArduinoFake.h>

#include "../speed_service.h"

using namespace fakeit;

class SpeedServiceTest : public ::testing::Test {
public:
    SpeedServiceTest()
    : ::testing::Test()
    {}

protected:
    virtual void SetUp() {
        When(Method(ArduinoFake(), analogWrite)).AlwaysReturn();
    }

    virtual void TearDown() {
        ArduinoFake().Reset();
    }
};

TEST_F(SpeedServiceTest, shouldSetSpeed) {
    SpeedService speedService(7);
    speedService.setSpeed(47);
    Verify(Method(ArduinoFake(), analogWrite).Using(7, 47)).Once();
}

TEST_F(SpeedServiceTest, shouldSetSpeedToZeroAtStart) {
    SpeedService speedService(7);
    Verify(Method(ArduinoFake(), analogWrite).Using(7, 0)).Once();
}

#endif
