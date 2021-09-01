import React from 'react';
import TitleWithIcon from '../../molecules/TitleWithIcon/TitleWithIcon';
import { UserOutlined } from '@ant-design/icons';

function UserInfo({ children }) {
  return (
    <TitleWithIcon icon={<UserOutlined />}>{children}</TitleWithIcon>
  );
}

export default UserInfo;