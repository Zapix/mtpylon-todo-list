import React from 'react';
import ReactDOM from 'react-dom';
import {RecoilRoot} from 'recoil';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';

import { MTProto } from 'zagram';

Promise.all([
  fetch('http://localhost:8081/schema').then(response => response.json()),
  fetch('http://localhost:8081/pub-keys').then(response => response.json()),
]).then(([schema, pems]) => {
  window.schema = schema;
  window.connection = new MTProto(
    'ws://localhost:8081/ws',
    schema,
    pems,
  );

  ReactDOM.render(
    <React.StrictMode>
      <RecoilRoot>
        <App />
      </RecoilRoot>
    </React.StrictMode>,
    document.getElementById('root')
  );
});


// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
