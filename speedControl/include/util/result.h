#ifndef __UTIL_RESULT_H
#define __UTIL_RESULT_H

template<typename Success, typename Error>
class Result {
public:
  enum Status {
               SUCCESS,
               ERROR
  };

  Result(Success&& successResult)
    : status(SUCCESS), successResult(successResult)
  {}

  Result(Error&& errorResult)
    : status(ERROR), errorResult(errorResult)
  {}

  bool isSuccessful() {
    return status == SUCCESS;
  }

  Success& get() {
    return successResult;
  }

  Error& getError() {
    return getError;
  }

private:
  const Status status;

  const union {
    Success successResult;
    Error errorResult;
  };
};

#endif
