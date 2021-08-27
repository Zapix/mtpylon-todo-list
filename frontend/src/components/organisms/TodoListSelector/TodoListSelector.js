import React from 'react';

import { Menu } from 'antd';
import { PlusOutlined, FileDoneOutlined } from '@ant-design/icons'

function TodoListSelector({ todoLists = []}) {
  return (
    <Menu theme="dark">
      <Menu.Item key="add" icon={<PlusOutlined />}>
        Add Todo List
      </Menu.Item>
      {todoLists.map((item) => (
        <Menu.Item key={item.id} icon={<FileDoneOutlined />}>
          {item.title}
        </Menu.Item>
      ))}
    </Menu>
  );
}

export default TodoListSelector;