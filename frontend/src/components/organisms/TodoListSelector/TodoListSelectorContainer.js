import React from 'react';

import TodoListSelector from './TodoListSelector';

function TodoListSelectorContainer() {
  const todoLists = [
    {
      id: 1,
      title: 'MTPylon Backend',
    },
    {
      id: 2,
      title: 'MTPylon Frontend'
    },
    {
      id: 3,
      title: 'Investment plans'
    },
    {
      id: 4,
      title: 'Homework'
    },
  ];

  return (
    <TodoListSelector todoLists={todoLists} />
  );
}

export default TodoListSelectorContainer;
