import React from 'react';

import AppTitle from 'components/atoms/AppTitle';
import { UserInfoContainer } from 'components/organisms/UserInfo'

import './AppHeader.css'

function AppHeader() {
  return (
    <div className="AppHeader-header">
      <div className="AppHeader-title">
        <AppTitle>MTPylon ToDo List</AppTitle>
      </div>
      <div className="AppHeader-user">
        <UserInfoContainer />
      </div>
    </div>
  );
}

export default AppHeader;