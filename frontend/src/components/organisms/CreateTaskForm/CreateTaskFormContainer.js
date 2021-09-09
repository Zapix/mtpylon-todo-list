import React from 'react';

import { useCreateTask } from 'state/todolists/hooks';
import CreateTaskForm from './CreateTaskForm';

function CreateTaskFormContainer({ todoListId }) {
  const createTask = useCreateTask(todoListId);

  return (
    <CreateTaskForm
      onSubmit={createTask}
    />
  );
}

export default CreateTaskFormContainer;
