import React from 'react';
import { useRecoilValueLoadable } from 'recoil';

import { meAtom} from 'state/authentication/atoms';
import UserInfo from './UserInfo';

function UserInfoContainer() {
  const me = useRecoilValueLoadable(meAtom);

  if (me.state !== 'hasValue') {
    return null;
  }

  return (
    <UserInfo>{me.contents.nickname}</UserInfo>
  );
}

export default UserInfoContainer;