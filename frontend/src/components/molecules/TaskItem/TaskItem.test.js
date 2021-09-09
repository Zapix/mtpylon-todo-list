import React from 'react';
import { screen, render, fireEvent, waitFor } from '@testing-library/react';

import TaskItem from './TaskItem';

test('mark as complete', () => {
  const task = {
    '@@type': 'Task',
    '@@constuctor': 'task',
    id: 2,
    title: 'Make mtpylon frontend',
    completed: false,
  };

  const markAsComplete = jest.fn();
  const markAsInComplete = jest.fn();

  render(
    <TaskItem
      task={task}
      onMarkComplete={markAsComplete}
      onMarkIncomplete={markAsInComplete}
    />
  );

  const markCompleteButton = screen.getByTestId("mark-as-complete-button");
  fireEvent.click(markCompleteButton);

  expect(markAsComplete).toBeCalledWith(task);
  expect(markAsInComplete).not.toBeCalled();
});

test('mark as incomplete', () => {
  const task = {
    '@@type': 'Task',
    '@@constructor': 'task',
    id: 1,
    title: 'Make mtpylon backend',
    completed: true,
  };

  const markAsComplete = jest.fn();
  const markAsInComplete = jest.fn();

  render(
    <TaskItem
      task={task}
      onMarkComplete={markAsComplete}
      onMarkIncomplete={markAsInComplete}
    />
  );

  const markInCompleteButton = screen.getByTestId('mark-as-incomplete-button');
  fireEvent.click(markInCompleteButton);

  expect(markAsComplete).not.toBeCalled();
  expect(markAsInComplete).toBeCalledWith(task);
});
