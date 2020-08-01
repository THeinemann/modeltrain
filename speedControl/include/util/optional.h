#ifndef __UTIL_OPTIONAL_H
#define __UTIL_OPTIONAL_H

class unit {};

template<typename T>
class optional {
public:
  optional()
    : valid(false), nothing(unit())
    {}

  optional(const T& value)
    : valid(true), value(value)
    {}

  bool isValid() {
    return valid;
  }

  T& get() {
    return value;
  }

private:
  const bool valid;
  const union {
    T value;
    unit nothing;
  };
};

#endif
