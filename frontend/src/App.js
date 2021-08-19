import {
  Switch,
  Route,
} from 'react-router';
import { useRecoilValue } from 'recoil';

import { connectionStatusAtom } from './state/connectionStatus/atoms';
import { useMTprotoConnection } from './state/connectionStatus/hooks';
import LoadingPage from './components/pages/LoadingPage';
import ErrorPage  from './components/pages/ErrorPage';
import MainPage from './components/pages/MainPage';
import LoginPage from './components/pages/LoginPage';
import './App.css';

function App(){
  const connectionStatus = useRecoilValue(connectionStatusAtom);
  useMTprotoConnection(window.connection);

  let component = null;
  if (connectionStatus === 'INIT') {
    component = (
      <LoadingPage />
    );
  } else if (connectionStatus === 'AUTH_KEY_CREATED') {
    component = (
     <Switch>
       <Route path="/login">
         <LoginPage />
       </Route>
       <Route path="/">
         <MainPage />
       </Route>
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
