#ifndef __DIRECTION_SERVICE_H
#define __DIRECTION_SERVICE_H


class DirectionService {
public:
    static const unsigned int FORWARD = 0;
    static const unsigned int BACKWARD = 1;

    DirectionService(unsigned int in1, unsigned int in2)
    : in1(in1), in2(in2)
    {}

    void setDirection(unsigned int direction);

private:
    const unsigned int in1;
    const unsigned int in2;
};

#endif
