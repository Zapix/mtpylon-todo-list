import {Button} from 'antd';
import logo from './logo.svg';
import './App.css';

function App(){
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <Button type="primary">Welcome Button</Button>
      </header>
    </div>
  );
}

export default App;
