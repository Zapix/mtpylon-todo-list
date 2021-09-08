import isTaskDone from './isTaskDone';

test('task done', () => {
  expect(isTaskDone({
    '@@type': 'Task',
    '@@constuctor': 'task',
    id: 2,
    title: 'Make mtpylon frontend',
    status: {
      '@@constructor': 'boolTrue',
      '@@type': 'Bool'
    },
  })).toBeTruthy();
});

test('task not done', () => {
  expect(isTaskDone({
    '@@type': 'Task',
    '@@constuctor': 'task',
    id: 2,
    title: 'Make mtpylon frontend',
    status: {
      '@@constructor': 'boolFalse',
      '@@type': 'Bool'
    },
  })).toBeFalsy();
});
