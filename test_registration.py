import unittest
from unittest.mock import RegistrationForm, patch, MagicMock
import re  


class TestRegistrationForm(unittest.TestCase):
    """Unit tests for Registration Form"""
    
    def setUp(self):
        """Set up test fixtures before each test method"""
     
        self.form = RegistrationForm()
        self.form.email = ""
        self.form.password = ""
        self.form.terms_accepted = False
        self.form.signup_button_enabled = False
        
        # Helper method to validate email
        self.form.validate_email = lambda email: bool(re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email))
        
        # Helper method to validate password (adjust rules as needed)
        self.form.validate_password = lambda pwd: len(pwd) >= 8 and any(c.isupper() for c in pwd) and any(c.islower() for c in pwd) and any(c.isdigit() for c in pwd)
        
        # Helper method to check if signup should be enabled
        self.form.update_signup_button_state = lambda: setattr(self.form, 'signup_button_enabled', 
            self.form.validate_email(self.form.email) and 
            self.form.validate_password(self.form.password) and 
            self.form.terms_accepted)
    
    def test_1_valid_email_entry(self):
        """Test 1: Valid Email Entry - should enable sign up button when valid email is entered"""
        # Arrange
        valid_email = "test@example.com"
        valid_password = "Password123!"
        
        # Act - Enter valid email
        self.form.email = valid_email
        self.form.password = valid_password
        self.form.terms_accepted = True
        self.form.update_signup_button_state()
        
        # Assert
        self.assertTrue(self.form.validate_email(valid_email), "Email should be valid")
        self.assertTrue(self.form.signup_button_enabled, "Sign up button should be enabled with valid email, password, and terms accepted")
        self.assertEqual(self.form.email, valid_email, "Email should be set correctly")
    
    def test_2_valid_password_entry(self):
        """Test 2: Valid Password Entry - should enable sign up button when valid password is entered"""
        # Arrange
        valid_email = "user@example.com"
        valid_password = "SecurePass123!"
        
        # Act - Enter valid password
        self.form.email = valid_email
        self.form.password = valid_password
        self.form.terms_accepted = True
        self.form.update_signup_button_state()
        
        # Assert
        self.assertTrue(self.form.validate_password(valid_password), "Password should be valid")
        self.assertTrue(self.form.signup_button_enabled, "Sign up button should be enabled with valid email, password, and terms accepted")
        self.assertEqual(self.form.password, valid_password, "Password should be set correctly")
    
    def test_3_terms_of_service_checkbox(self):
        """Test 3: Terms of Service Checkbox - should enable sign up button only when checkbox is checked"""
        # Arrange
        valid_email = "test@example.com"
        valid_password = "Password123!"
        
        # Act - Enter valid email and password but don't accept terms
        self.form.email = valid_email
        self.form.password = valid_password
        self.form.terms_accepted = False
        self.form.update_signup_button_state()
        
        # Assert - Button should be disabled without terms acceptance
        self.assertFalse(self.form.signup_button_enabled, "Sign up button should be disabled when terms are not accepted")
        self.assertFalse(self.form.terms_accepted, "Terms should not be accepted")
        
        # Act - Accept terms
        self.form.terms_accepted = True
        self.form.update_signup_button_state()
        
        # Assert - Button should now be enabled
        self.assertTrue(self.form.signup_button_enabled, "Sign up button should be enabled when terms are accepted")
        self.assertTrue(self.form.terms_accepted, "Terms should be accepted")


class TestRegistrationFormIntegration(unittest.TestCase):
    """Integration tests showing how the form works together"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.form = RegistrationForm()
        self.form.email = ""
        self.form.password = ""
        self.form.terms_accepted = False
        self.form.signup_button_enabled = False
        
        self.form.validate_email = lambda email: bool(re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email))
        self.form.validate_password = lambda pwd: len(pwd) >= 8 and any(c.isupper() for c in pwd) and any(c.islower() for c in pwd) and any(c.isdigit() for c in pwd)
        self.form.update_signup_button_state = lambda: setattr(self.form, 'signup_button_enabled', 
            self.form.validate_email(self.form.email) and 
            self.form.validate_password(self.form.password) and 
            self.form.terms_accepted)
    
    def test_all_three_conditions_required(self):
        """Test that all three conditions (email, password, terms) must be met"""
        # Test with only email
        self.form.email = "test@example.com"
        self.form.password = ""
        self.form.terms_accepted = False
        self.form.update_signup_button_state()
        self.assertFalse(self.form.signup_button_enabled)
        
        # Test with email and password
        self.form.password = "Password123!"
        self.form.terms_accepted = False
        self.form.update_signup_button_state()
        self.assertFalse(self.form.signup_button_enabled)
        
        # Test with all three
        self.form.terms_accepted = True
        self.form.update_signup_button_state()
        self.assertTrue(self.form.signup_button_enabled)


if __name__ == '__main__':
    unittest.main()
