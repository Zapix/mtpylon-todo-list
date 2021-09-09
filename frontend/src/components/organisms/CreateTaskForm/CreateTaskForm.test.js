import React from 'react';
import { screen, render, fireEvent, waitFor } from '@testing-library/react';

import CreateTaskForm from './CreateTaskForm';
import userEvent from '@testing-library/user-event';

test('enable button', () => {
  render(<CreateTaskForm onSubmit={jest.fn()} />);

  const titleField = screen.getByTestId('title-field');
  userEvent.type(titleField, 'hello');
  fireEvent.blur(titleField);

  return waitFor(() => screen.getByTestId('submit-button')).then(() => {
    const submitButton = screen.getByTestId('submit-button');
    expect(submitButton).toBeEnabled();
  });
});

test('show error', () => {
  const createTask = jest.fn();
  createTask.mockRejectedValue({ title: 'Server Error' });

  render(<CreateTaskForm onSubmit={createTask} />);

  const titleField = screen.getByTestId('title-field');
  userEvent.type(titleField, 'hello');
  fireEvent.blur(titleField);

  const submitButton = screen.getByTestId('submit-button');
  fireEvent.click(submitButton);

  return waitFor(() => screen.getByRole('alert'));
});