import React, { useEffect } from 'react';
import { useParams } from 'react-router-dom';
import { useSetRecoilState } from 'recoil';
import { Row, Col, PageHeader } from 'antd';

import { selectedTodoListIdAtom } from 'state/todolists/atoms';
import MainLayout from 'components/templates/MainLayout';

function TodoListPage() {
  const { todoListId }  = useParams();
  const setSelectedTodoListId = useSetRecoilState(selectedTodoListIdAtom);

  useEffect(() => {
    setSelectedTodoListId(todoListId);
  }, [todoListId])

  return (
    <MainLayout>
      <PageHeader
        title={`Todo List Page ${todoListId}`}
      />
    </MainLayout>
  );
}

export default TodoListPage;
