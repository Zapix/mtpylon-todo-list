import React, { useState } from 'react';
import { Redirect } from 'react-router-dom';

import AddTodoListForm from './AddTodoListForm';

import { useCreateTodoList } from 'state/todolists/hooks';


function AddToDoListFormContainer() {
  const [redirect, setRedirect] = useState(false);
  const createTodoList = useCreateTodoList();

  return (redirect ? (
    <Redirect to="/" />
  ): (
    <AddTodoListForm
      onSubmit={(data) => createTodoList(data).then(() => setRedirect(true))}
    />
  ))
}

export default AddToDoListFormContainer;