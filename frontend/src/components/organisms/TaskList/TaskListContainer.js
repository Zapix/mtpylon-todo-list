import React from 'react';
import { useRecoilValueLoadable } from 'recoil';

import { taskListFamily } from 'state/todolists/atoms';
import { useSetAsCompleted, useSetAsIncompleted } from 'state/todolists/hooks';

import TaskList from './TaskList';

function TaskListContainer({ todoListId }) {
  const taskList = useRecoilValueLoadable(taskListFamily(todoListId));
  const setAsCompleted = useSetAsCompleted(todoListId);
  const setAsIncompleted = useSetAsIncompleted(todoListId)

  if (taskList.state === 'hasValue') {
    return (
      <TaskList
        taskList={taskList.contents}
        onMarkComplete={setAsCompleted}
        onMarkIncomplete={setAsIncompleted}
      />
    );
  }

  return null;
}

export default TaskListContainer;
