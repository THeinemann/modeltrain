#ifdef TEST
#include <catch.hpp>
#include <ArduinoFake.h>

#include "../direction_service.h"

using namespace fakeit;

TEST_CASE("Direction is changed", "[DirectionService]") {
    When(Method(ArduinoFake(), digitalWrite)).AlwaysReturn();
    auto directionService = DirectionService(1, 2);

    SECTION("Set direction to forward") {
        directionService.setDirection(DirectionService::FORWARD);
        Verify(Method(ArduinoFake(), digitalWrite).Using(1, LOW));
        Verify(Method(ArduinoFake(), digitalWrite).Using(2, LOW));
        Verify(Method(ArduinoFake(), digitalWrite).Using(2, HIGH)).Once();
        Verify(Method(ArduinoFake(), digitalWrite).Using(1, HIGH)).Never();
    }

    SECTION("Set direction to backward") {
        directionService.setDirection(DirectionService::BACKWARD);
        Verify(Method(ArduinoFake(), digitalWrite).Using(1, LOW));
        Verify(Method(ArduinoFake(), digitalWrite).Using(2, LOW));
        Verify(Method(ArduinoFake(), digitalWrite).Using(1, HIGH)).Once();
        Verify(Method(ArduinoFake(), digitalWrite).Using(2, HIGH)).Never();
    }

    ArduinoFake().Reset();
}

#endif
