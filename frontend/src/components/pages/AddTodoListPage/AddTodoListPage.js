import React from 'react';
import { PageHeader, Row, Col } from 'antd';

import MainLayout from 'components/templates/MainLayout';
import { AddToDoListFormContainer } from 'components/organisms/AddTodoListForm';


function AddTodoListPage() {
  return (
    <MainLayout dataTestId="add-todo-list-page">
      <PageHeader
        title="Add ToDo list"
      />
      <Row>
        <Col span={12} offset={6}>
          <AddToDoListFormContainer />
        </Col>
      </Row>
    </MainLayout>
  );
}

export default AddTodoListPage;
