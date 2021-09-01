import React from 'react';
import { PageHeader } from 'antd';

function TodoListHeader({ todoList }) {
  return (
    <PageHeader title={todoList.title} />
  );
}

export default TodoListHeader;
