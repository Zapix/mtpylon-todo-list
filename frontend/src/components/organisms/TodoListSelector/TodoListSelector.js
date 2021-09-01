import React from 'react';
import { Link } from 'react-router-dom';
import { Menu } from 'antd';
import { PlusOutlined, FileDoneOutlined } from '@ant-design/icons'

function TodoListSelector({ todoLists = []}) {
  return (
    <Menu theme="dark">
      <Menu.Item key="add" icon={<PlusOutlined />}>
        <Link to="/add-todo-list">
          Add Todo List
        </Link>
      </Menu.Item>
      {todoLists.map((item) => (
        <Menu.Item key={item.id} icon={<FileDoneOutlined />}>
          <Link to={`/todo-list/${item.id}`}>
            {item.title}
          </Link>
        </Menu.Item>
      ))}
    </Menu>
  );
}

export default TodoListSelector;