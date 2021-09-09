import React, { useEffect } from 'react';
import { useParams } from 'react-router-dom';
import { useSetRecoilState } from 'recoil';
import { Row, Col } from 'antd';

import { selectedTodoListIdAtom } from 'state/todolists/atoms';
import MainLayout from 'components/templates/MainLayout';
import { TodoListHeaderContainer } from 'components/organisms/TodoListHeader';
import { CreateTaskFormContainer } from 'components/organisms/CreateTaskForm';
import { TaskListContainer } from 'components/organisms/TaskList';

function TodoListPage() {
  const { todoListId }  = useParams();
  const setSelectedTodoListId = useSetRecoilState(selectedTodoListIdAtom);

  useEffect(() => {
    setSelectedTodoListId(todoListId);
  }, [todoListId])

  return (
    <MainLayout>
      <TodoListHeaderContainer />
      <Row>
        <Col offset={6} span={12}>
          <CreateTaskFormContainer
            todoListId={todoListId}
          />
        </Col>
      </Row>
      <Row>
        <Col offset={6} span={12}>
          <TaskListContainer todoListId={todoListId} />
        </Col>
      </Row>
    </MainLayout>
  );
}

export default TodoListPage;
