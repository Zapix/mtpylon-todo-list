import React from 'react';
import { useRecoilValueLoadable } from 'recoil';

import { taskListFamily } from 'state/todolists/atoms';

import TaskList from './TaskList';

function TaskListContainer({ todoListId }) {
  const taskList = useRecoilValueLoadable(taskListFamily(todoListId));
  console.log(taskList);

  if (taskList.state === 'hasValue') {
    return <TaskList taskList={taskList.contents} />
  }

  return <TaskList taskList={[]} />
}

export default TaskListContainer;
