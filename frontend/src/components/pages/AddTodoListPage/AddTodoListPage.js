import React from 'react';

import MainLayout from 'components/templates/MainLayout';
import { PageHeader } from 'antd';


function AddTodoListPage() {
  return (
    <MainLayout dataTestId="add-todo-list-page">
      <PageHeader
        title="Add ToDo list"
      />
    </MainLayout>
  );
}

export default AddTodoListPage;
