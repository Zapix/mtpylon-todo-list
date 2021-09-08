import React from 'react';

import TaskList from './TaskList';

function TaskListContainer() {
  const taskList = [
    {
      '@@type': 'Task',
      '@@constructor': 'task',
      id: 1,
      title: 'Make mtpylon backend',
      status: {
        '@@type': 'Bool',
        '@@constructor': 'boolTrue',
      },
    },
    {
      '@@type': 'Task',
      '@@constuctor': 'task',
      id: 2,
      title: 'Make mtpylon frontend',
      status: {
        '@@type': 'Bool',
        '@@constructor': 'boolFalse',
      },
    }
  ]
  return <TaskList taskList={taskList} />
}

export default TaskListContainer;
