import { useRecoilValue } from 'recoil';

import { connectionStatusAtom } from './state/connectionStatus/atoms';
import { useMTprotoConnection } from './state/connectionStatus/hooks';
import LoadingPage from './components/pages/LoadingPage';
import ErrorPage  from './components/pages/ErrorPage';
import MainPage from './components/pages/MainPage';
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
      <MainPage />
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
