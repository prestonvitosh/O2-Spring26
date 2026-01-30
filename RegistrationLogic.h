#ifndef REGISTRATION_LOGIC_H
#define REGISTRATION_LOGIC_H

#include <string>
#include <regex>
#include <cctype>

struct RegistrationState {
    std::string email;
    std::string password;
    bool termsAccepted = false;

    bool isEmailValid = false;
    bool isPasswordValid = false;
    bool canSubmit = false;  
};

class RegistrationLogic {
public:
    static bool validateEmail(const std::string& email) {
        
        static const std::regex pattern(
            R"([A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,})"
        );
        return std::regex_match(email, pattern);
    }

    static bool validatePassword(const std::string& password) {
        // Rule: >= 8 chars, has uppercase, lowercase, digit
        if (password.size() < 8) return false;

        bool hasUpper = false;
        bool hasLower = false;
        bool hasDigit = false;

        for (unsigned char c : password) { // unsigned char avoids cctype UB
            if (std::isupper(c)) hasUpper = true;
            if (std::islower(c)) hasLower = true;
            if (std::isdigit(c)) hasDigit = true;
        }
        return hasUpper && hasLower && hasDigit;
    }

    // Call this whenever user changes email/password/terms checkbox
    static void recompute(RegistrationState& s) {
        s.isEmailValid = validateEmail(s.email);
        s.isPasswordValid = validatePassword(s.password);
        s.canSubmit = s.isEmailValid && s.isPasswordValid && s.termsAccepted;
    }
};

#endif 
