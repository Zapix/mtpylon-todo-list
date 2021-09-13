import React from 'react';
import ReactDOM from 'react-dom';
import {RecoilRoot} from 'recoil';
import { BrowserRouter as Router } from 'react-router-dom';

import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';

import { MTProto } from 'zagram';


function loadAuthData() {
  const authDataStr = window.localStorage.getItem('authData');

  if (authDataStr) {
    return JSON.parse(authDataStr);
  }

  return authDataStr;
}

function saveAuthData(authKey, authKeyId, serverSalt) {
  window.localStorage.setItem('authData', JSON.stringify({
    authKey,
    authKeyId,
    serverSalt
  }));
}

Promise.all([
  fetch('http://localhost:8081/schema').then(response => response.json()),
  fetch('http://localhost:8081/pub-keys').then(response => response.json()),
]).then(([schema, pems]) => {
  const authData = loadAuthData();

  console.log('Auth key data:', authData);

  window.schema = schema;
  window.connection = new MTProto(
    'ws://localhost:8081/ws',
    schema,
    pems,
    authData
  );

  window.connection.addEventListener('statusChanged', (e) => {
    if (e.status === 'AUTH_KEY_CREATED') {
      saveAuthData(
        window.connection.authKey,
        Array.from(window.connection.authKeyId),
        Array.from(window.connection.serverSalt),
      );
    }
  })

  ReactDOM.render(
    <React.StrictMode>
      <RecoilRoot>
        <Router>
          <App />
        </Router>
      </RecoilRoot>
    </React.StrictMode>,
    document.getElementById('root')
  );
});


// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
