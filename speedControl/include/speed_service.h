#ifndef __SPEED_SERVICE_H
#define __SPEED_SERVICE_H

class SpeedService {
public:
  SpeedService(unsigned int en);

  void setSpeed(unsigned char speed);

private:
  const unsigned int en;
};

#endif
