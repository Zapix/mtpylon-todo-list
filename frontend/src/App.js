import { Switch } from 'react-router';
import { useRecoilValue, useRecoilValueLoadable } from 'recoil';

import AnonymousRoute from 'components/molecules/AnonymousRoute';
import AuthenticatedRoute from 'components/molecules/AuthenticatedRoute';
import { connectionStatusAtom } from 'state/connectionStatus/atoms';
import { meAtom } from 'state/authentication/atoms';
import { useMTprotoConnection } from 'state/connectionStatus/hooks';
import LoadingPage from 'components/pages/LoadingPage';
import ErrorPage  from 'components/pages/ErrorPage';
import MainPage from 'components/pages/MainPage';
import LoginPage from 'components/pages/LoginPage';
import './App.css';

function App(){
  const connectionStatus = useRecoilValue(connectionStatusAtom);
  useMTprotoConnection(window.connection);

  const me = useRecoilValueLoadable(meAtom);

  let component = null;
  if (
    connectionStatus === 'INIT' ||
    (me.state === 'loading' && connectionStatus === 'AUTH_KEY_CREATED')
  ) {
    component = (
      <LoadingPage />
    );
  } else if (connectionStatus === 'AUTH_KEY_CREATED' && me.state === 'hasValue') {
    component = (
     <Switch>
       <AnonymousRoute path="/login">
         <LoginPage />
       </AnonymousRoute>
       <AuthenticatedRoute path="/">
         <MainPage />
       </AuthenticatedRoute>
     </Switch>
    );
  } else {
    component = (
      <ErrorPage />
    );
  }

  return (
    <div className="App">
      {component}
    </div>
  );
}

export default App;
