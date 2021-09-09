import isTaskDone from './isTaskDone';

test('task done', () => {
  expect(isTaskDone({
    '@@type': 'Task',
    '@@constuctor': 'task',
    id: 2,
    title: 'Make mtpylon frontend',
    completed: true,
  })).toBeTruthy();
});

test('task not done', () => {
  expect(isTaskDone({
    '@@type': 'Task',
    '@@constuctor': 'task',
    id: 2,
    title: 'Make mtpylon frontend',
    completed: false,
  })).toBeFalsy();
});
