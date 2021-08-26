import { render, screen, fireEvent, waitFor, cleanup } from '@testing-library/react';
import useEvent from '@testing-library/user-event';

import RegistrationForm from './RegistrationForm';
import userEvent from '@testing-library/user-event';

afterEach(() => {
  cleanup();
});

test('enable submit button', () => {
  render(
    <RegistrationForm onSubmit={jest.fn()} />
  )

  const nicknameField = screen.getByTestId('nickname-field');
  useEvent.type(nicknameField, 'jhondoe');
  fireEvent.blur(nicknameField);

  const passwordField = screen.getByTestId('password-field');
  useEvent.type(passwordField, '123123');
  fireEvent.blur(passwordField);

  const confirmPasswordField = screen.getByTestId('confirm-password-field');
  useEvent.type(confirmPasswordField, '123123');
  fireEvent.blur(confirmPasswordField, '123123');

  return waitFor(() => screen.getByTestId('submit-button'))
    .then(() => {
      const submitButton = screen.getByTestId('submit-button');
      expect(submitButton).toBeEnabled();
    });
});

test('submit error', () => {
  const register = jest.fn();
  register.mockRejectedValue({ nonFieldError: 'not found' });

  render(<RegistrationForm onSubmit={register} />);

  const nicknameField = screen.getByTestId('nickname-field');
  useEvent.type(nicknameField, 'jhondoe');
  fireEvent.blur(nicknameField);

  const passwordField = screen.getByTestId('password-field');
  useEvent.type(passwordField, '123123');
  fireEvent.blur(passwordField);

  const confirmPasswordField = screen.getByTestId('confirm-password-field');
  useEvent.type(confirmPasswordField, '123123');
  fireEvent.blur(confirmPasswordField, '123123');

  const submitButton = screen.getByTestId('submit-button');
  fireEvent.click(submitButton);

  return waitFor(() => screen.getByTestId('error-alert'));
});
