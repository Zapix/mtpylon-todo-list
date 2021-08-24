import { render, screen, fireEvent, waitFor, cleanup } from '@testing-library/react';
import userEvent from '@testing-library/user-event';

import LoginForm from './LoginForm';

afterEach(() => {
  cleanup();
});

test('render and filling inputs', () => {
  render(<LoginForm onSubmit={jest.fn()} />);

  const loginField = screen.getByTestId('login-field');
  userEvent.type(loginField,  'jhondoe');
  fireEvent.blur(loginField);

  const passwordField = screen.getByTestId('password-field');
  userEvent.type(passwordField, '123123');
  fireEvent.blur(passwordField);

  return waitFor(() => screen.getByTestId('submit-button')).then(() => {
    const submitButton = screen.getByTestId('submit-button');
    expect(submitButton).toBeEnabled();
  })
});


test('submit error', () => {
  const login = jest.fn();
  login.mockRejectedValue({nonFieldError: 'not found'});

  render(<LoginForm onSubmit={login} />);

  const submitButton = screen.getByTestId('submit-button');

  const loginField = screen.getByTestId('login-field');
  userEvent.type(loginField,  'johndoe');

  const passwordField = screen.getByTestId('password-field');
  userEvent.type(passwordField, '123123');

  fireEvent.click(submitButton);

  return waitFor(() => screen.getByTestId('error-alert'));
});