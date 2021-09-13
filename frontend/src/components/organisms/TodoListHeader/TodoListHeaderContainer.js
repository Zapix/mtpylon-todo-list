import React from 'react';
import * as R from 'ramda';
import { useRecoilValueLoadable } from 'recoil';

import { selectedTodoListSelector } from 'state/todolists/selectors';
import TodoListHeader from './TodoListHeader';


function TodoListHeaderContainer(){
  const todoList = useRecoilValueLoadable(selectedTodoListSelector);

  if (todoList.state !== 'hasValue' || R.isNil(todoList.contents)) {
    return null;
  }

  return (
    <TodoListHeader todoList={todoList.contents} />
  );
}

export default TodoListHeaderContainer;
