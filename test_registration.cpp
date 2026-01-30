#include <iostream>
#include <string>
#include <vector>
#include "RegistrationLogic.h"

static int testsRun = 0;
static int testsFailed = 0;

#define CHECK(cond) do { \
  ++testsRun; \
  if (!(cond)) { \
    ++testsFailed; \
    std::cerr << "FAIL: " << #cond << " @ " << __FILE__ << ":" << __LINE__ << "\n"; \
  } \
} while (0)

void test_email_validation() {
  CHECK(RegistrationLogic::validateEmail("test@example.com"));

  std::vector<std::string> bad = {
    "invalid-email",
    "test@",
    "@example.com",
    "a@b",    
    "a@b.",    // trailing dot
  };

  for (const auto& e : bad) {
    CHECK(!RegistrationLogic::validateEmail(e));
  }
}

void test_password_validation() {
  CHECK(RegistrationLogic::validatePassword("ValidPass123"));

  std::vector<std::string> bad = {
    "short",
    "nouppercase123",
    "NOLOWERCASE123",
    "NoDigitsHere",
  };

  for (const auto& p : bad) {
    CHECK(!RegistrationLogic::validatePassword(p));
  }
}

void test_can_submit_rule() {
  RegistrationState s;

  RegistrationLogic::recompute(s);
  CHECK(!s.canSubmit);

  s.email = "test@example.com";
  s.password = "ValidPass123";
  s.termsAccepted = false;
  RegistrationLogic::recompute(s);
  CHECK(s.isEmailValid);
  CHECK(s.isPasswordValid);
  CHECK(!s.canSubmit);

  s.termsAccepted = true;
  RegistrationLogic::recompute(s);
  CHECK(s.canSubmit);

  s.email = "bad-email";
  RegistrationLogic::recompute(s);
  CHECK(!s.canSubmit);
}

int main() {
  std::cout << "Running registration tests...\n";

  test_email_validation();
  test_password_validation();
  test_can_submit_rule();

  std::cout << "\nTests run: " << testsRun
            << "\nFailures: " << testsFailed << "\n";

  return testsFailed ? 1 : 0;
}
