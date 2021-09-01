import React from 'react';
import { Typography } from 'antd';

import MainLayout from 'components/templates/MainLayout';

const { Title } = Typography;


function MainPage() {
  return (
    <MainLayout>
      <Title>
        Here will be content
      </Title>
    </MainLayout>
  );
}

export default MainPage;
