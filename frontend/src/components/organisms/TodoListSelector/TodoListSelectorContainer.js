import React from 'react';
import { useRecoilValueLoadable } from 'recoil';

import { todoListsAtomFamily } from 'state/todolists/atoms';
import TodoListSelector from './TodoListSelector';

function TodoListSelectorContainer() {
  const todoLists = useRecoilValueLoadable(todoListsAtomFamily());

  if (todoLists.state !== 'hasValue') {
    return null;
  }

  return (
    <TodoListSelector todoLists={todoLists.contents} />
  );
}

export default TodoListSelectorContainer;
