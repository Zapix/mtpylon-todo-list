import React from 'react';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import userEvent from '@testing-library/user-event';

import AddTodoListForm from './AddTodoListForm';

test('submit button enabled', () => {
  render(<AddTodoListForm onSubmit={jest.fn()} />);

  const titleField = screen.getByTestId('title-field');
  userEvent.type(titleField, 'hello');
  fireEvent.blur(titleField);

  return waitFor(() => screen.getByTestId('submit-button')).then(() => {
    const submitButton = screen.getByTestId('submit-button');
    expect(submitButton).toBeEnabled();
  });
});

test('submit error', () => {
  const createTodo = jest.fn();
  createTodo.mockRejectedValue({ nonFieldError: 'not created' });

  render(<AddTodoListForm onSubmit={createTodo} />);

  const titleField = screen.getByTestId('title-field');
  userEvent.type(titleField, 'hello');
  fireEvent.blur(titleField);

  const submitButton = screen.getByTestId('submit-button');
  fireEvent.click(submitButton);

  return waitFor(() => screen.getByTestId('error-alert'));
});