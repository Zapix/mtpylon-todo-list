import React from 'react';
import * as R from 'ramda';
import { useRecoilValue} from 'recoil';

import { selectedTodoListSelector } from 'state/todolists/selectors';
import TodoListHeader from './TodoListHeader';


function TodoListHeaderContainer(){
  const todoList = useRecoilValue(selectedTodoListSelector);

  if (R.isNil(todoList)) {
    return null;
  }

  return (
    <TodoListHeader todoList={todoList} />
  );
}

export default TodoListHeaderContainer;
