import React from 'react';
import { Layout } from 'antd';

import './MainLayout.css';

import AppHeader from 'components/organisms/AppHeader';
import { TodoListSelectorContainer } from 'components/organisms/TodoListSelector';

const { Header, Sider, Content } = Layout;

function MainLayout({ children, dataTestId='main-page' }) {
  return (
    <div data-testid={dataTestId} className="MainLayout-page">
      <Layout className="MainLayout-layout">
        <Header theme="light">
          <AppHeader />
        </Header>
        <Layout>
          <Sider>
            <TodoListSelectorContainer />
          </Sider>
          <Content>
            {children}
          </Content>
        </Layout>
      </Layout>
    </div>
  );
}

export default MainLayout;
