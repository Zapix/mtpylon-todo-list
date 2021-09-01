import React, { useEffect } from 'react';
import { useParams } from 'react-router-dom';
import { useSetRecoilState } from 'recoil';

import { selectedTodoListIdAtom } from 'state/todolists/atoms';
import MainLayout from 'components/templates/MainLayout';
import { TodoListHeaderContainer } from 'components/organisms/TodoListHeader';

function TodoListPage() {
  const { todoListId }  = useParams();
  const setSelectedTodoListId = useSetRecoilState(selectedTodoListIdAtom);

  useEffect(() => {
    setSelectedTodoListId(todoListId);
  }, [todoListId])

  return (
    <MainLayout>
      <TodoListHeaderContainer />
    </MainLayout>
  );
}

export default TodoListPage;
