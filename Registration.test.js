import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import Registration from '../Registration'; 

describe('Registration Form', () => {
  let emailInput;
  let passwordInput;
  let termsCheckbox;
  let signUpButton;

  beforeEach(() => {
    render(<Registration />);
    emailInput = screen.queryByLabelText(/email/i) || 
                 screen.queryByPlaceholderText(/email/i) || 
                 screen.queryByRole('textbox', { name: /email/i });
    passwordInput = screen.queryByLabelText(/password/i) || 
                    screen.queryByPlaceholderText(/password/i) || 
                    screen.queryByLabelText(/^password$/i);
    termsCheckbox = screen.queryByLabelText(/terms|terms of service|agree/i) || 
                    screen.queryByRole('checkbox');
    signUpButton = screen.getByRole('button', { name: /sign up|register|submit/i });
  });

  describe('1. Valid Email Entry', () => {
    it('should enable sign up button when valid email format is entered with valid password and terms accepted', async () => {
      const user = userEvent.setup();
      
      // Enter valid email
      await user.type(emailInput, 'test@example.com');
      
      // Enter valid password
      await user.type(passwordInput, 'Password123!');
      
      // Accept terms
      await user.click(termsCheckbox);
      
      // Wait for button to be enabled
      await waitFor(() => {
        expect(signUpButton).not.toBeDisabled();
      });
      
      // Verify email was entered correctly
      expect(emailInput.value).toBe('test@example.com');
    });
  });

  describe('2. Valid Password Entry', () => {
    it('should enable sign up button when valid password is entered with valid email and terms accepted', async () => {
      const user = userEvent.setup();
      
      // Enter valid email
      await user.type(emailInput, 'user@example.com');
      
      // Enter valid password
      await user.type(passwordInput, 'SecurePass123!');
      
      // Accept terms
      await user.click(termsCheckbox);
      
      // Wait for button to be enabled
      await waitFor(() => {
        expect(signUpButton).not.toBeDisabled();
      });
      
      // Verify password was entered correctly
      expect(passwordInput.value).toBe('SecurePass123!');
    });
  });

  describe('3. Terms of Service Checkbox', () => {
    it('should enable sign up button only when terms checkbox is checked along with valid email and password', async () => {
      const user = userEvent.setup();
      
      // Enter valid email and password
      await user.type(emailInput, 'test@example.com');
      await user.type(passwordInput, 'Password123!');
      
      // Button should be disabled without terms acceptance
      expect(signUpButton).toBeDisabled();
      
      // Check terms checkbox
      await user.click(termsCheckbox);
      
      // Button should now be enabled
      await waitFor(() => {
        expect(signUpButton).not.toBeDisabled();
      });
      
      // Verify checkbox is checked
      expect(termsCheckbox).toBeChecked();
    });
  });
});
