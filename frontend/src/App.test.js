import { render, screen, waitFor } from '@testing-library/react';
import { RecoilRoot } from 'recoil';
import { BrowserRouter as Router } from 'react-router-dom';

import { meAtom } from 'state/authentication/atoms';

import App from './App';

beforeEach(() => {
  window.connection = new EventTarget();
  window.connection.init = () => {
  };
  window.schema = {
    'constructors': [{
      'id': -1720552011,
      'predicate': 'boolTrue',
      'type': 'Bool',
      'params': []
    }, {
      'id': -1132882121,
      'predicate': 'boolFalse',
      'type': 'Bool',
      'params': []
    }, {
      'id': -1985249584,
      'predicate': 'anonymous_user',
      'type': 'User',
      'params': []
    }, {
      'id': -366049798,
      'predicate': 'registered_user',
      'type': 'User',
      'params': [{ 'name': 'id', 'type': 'int' }, { 'name': 'nickname', 'type': 'string' }]
    }, {
      'id': 2112128313,
      'predicate': 'todo_list',
      'type': 'TodoList',
      'params': [{ 'name': 'id', 'type': 'int' }, { 'name': 'title', 'type': 'string' }]
    }, {
      'id': 659881707,
      'predicate': 'todo_lists_result',
      'type': 'TodoListsResult',
      'params': [{ 'name': 'todo_lists', 'type': 'Vector<TodoList>' }]
    }, {
      'id': 1600875913,
      'predicate': 'task',
      'type': 'Task',
      'params': [{ 'name': 'id', 'type': 'int' }, {
        'name': 'title',
        'type': 'string'
      }, { 'name': 'completed', 'type': 'Bool' }]
    }, {
      'id': -1304717529,
      'predicate': 'task_list',
      'type': 'TaskList',
      'params': [{ 'name': 'tasks', 'type': 'Vector<Task>' }]
    }],
    'methods': [{
      'id': -786547692,
      'method': 'register',
      'type': 'User',
      'params': [{ 'name': 'nickname', 'type': 'string' }, { 'name': 'password', 'type': 'string' }]
    }, {
      'id': -1265849575,
      'method': 'login',
      'type': 'User',
      'params': [{ 'name': 'nickname', 'type': 'string' }, { 'name': 'password', 'type': 'string' }]
    }, { 'id': 1169887620, 'method': 'get_me', 'type': 'User', 'params': [] }, {
      'id': -1107009002,
      'method': 'create_todo_list',
      'type': 'TodoList',
      'params': [{ 'name': 'title', 'type': 'string' }]
    }, {
      'id': -600513500,
      'method': 'get_todo_lists',
      'type': 'TodoListsResult',
      'params': []
    }, {
      'id': -795996351,
      'method': 'get_single_todo_list',
      'type': 'TodoList',
      'params': [{ 'name': 'todo_list_id', 'type': 'int' }]
    }, {
      'id': 1817756127,
      'method': 'remove_todo_list',
      'type': 'Bool',
      'params': [{ 'name': 'todo_list_id', 'type': 'int' }]
    }, {
      'id': 1653811007,
      'method': 'create_task',
      'type': 'Task',
      'params': [{ 'name': 'todo_list_id', 'type': 'int' }, { 'name': 'title', 'type': 'string' }]
    }, {
      'id': -1589847375,
      'method': 'get_task_list',
      'type': 'TaskList',
      'params': [{ 'name': 'todo_list_id', 'type': 'int' }]
    }, {
      'id': 1646026399,
      'method': 'edit_task_title',
      'type': 'Task',
      'params': [{ 'name': 'task_id', 'type': 'int' }, { 'name': 'title', 'type': 'string' }]
    }, {
      'id': -1241755262,
      'method': 'set_as_completed',
      'type': 'Task',
      'params': [{ 'name': 'task_id', 'type': 'int' }]
    }, {
      'id': -174067091,
      'method': 'set_as_uncompleted',
      'type': 'Task',
      'params': [{ 'name': 'task_id', 'type': 'int' }]
    }, {
      'id': -2038687995,
      'method': 'remove_task',
      'type': 'Bool',
      'params': [{ 'name': 'task_id', 'type': 'int' }]
    }]
  };
});

afterEach(() => {
  Reflect.deleteProperty(window, 'connection');
  Reflect.deleteProperty(window, 'schema') ;
});

test('renders loading page', () => {
  render(
    <RecoilRoot>
      <Router>
        <App/>
      </Router>
    </RecoilRoot>
  );

  const loadingPage = screen.getByTestId('loading-page');
  expect(loadingPage).toBeInTheDocument();
});

test('renders loading until user info did not received', () => {
  render(
    <RecoilRoot>
      <Router>
        <App/>
      </Router>
    </RecoilRoot>
  );

  const event = new Event('statusChanged');
  event.status = 'AUTH_KEY_CREATED';
  window.connection.dispatchEvent(event);

  return waitFor(() => screen.getByTestId('loading-page')).then(() => {
    const loadingPage = screen.getByTestId('loading-page');
    expect(loadingPage).toBeInTheDocument();
  });
});

test('renders main page', () => {
  const user = {
    '@@type': 'User',
    '@@constructor': 'registered_user',
    nickname: 'johndoe',
    id: 12
  }

  render(
    <RecoilRoot initializeState={({ set }) => set(meAtom, user)}>
      <Router>
        <App/>
      </Router>
    </RecoilRoot>
  );

  window.connection.status = 'AUTH_KEY_CREATED';
  window.connection.request = jest.fn();
  window.connection.request.mockResolvedValue({
    '@@constructor': 'registered_user',
    '@@type': 'User',
    nickname: 'johndoe',
    id: 12
  });

  const event = new Event('statusChanged');
  event.status = 'AUTH_KEY_CREATED';
  window.connection.dispatchEvent(event);

  return waitFor(() => screen.getByTestId('main-page')).then(() => {
    const mainPage = screen.getByTestId('main-page');
    expect(mainPage).toBeInTheDocument();
  });
});

test('renders login page', () => {
  const anonymousUser = {
    '@@type': 'User',
    '@@constructor': 'anonymous_user',
  }

  render(
    <RecoilRoot initializeState={({ set }) => set(meAtom, anonymousUser)}>
      <Router>
        <App/>
      </Router>
    </RecoilRoot>
  );

  window.connection.status = 'AUTH_KEY_CREATED';
  window.connection.request = jest.fn();
  window.connection.request.mockResolvedValue({
    '@@constructor': 'anonymous_user',
    '@@type': 'User',
  });

  const event = new Event('statusChanged');
  event.status = 'AUTH_KEY_CREATED';
  window.connection.dispatchEvent(event);

  return waitFor(() => screen.getByTestId('login-page')).then(() => {
    const mainPage = screen.getByTestId('login-page');
    expect(mainPage).toBeInTheDocument();
  });
});

test('renders error page', () => {
  render(
    <RecoilRoot>
      <Router>
        <App/>
      </Router>
    </RecoilRoot>
  );

  const event = new Event('statusChanged');
  event.status = 'AUTH_KEY_FAILED';
  window.connection.dispatchEvent(event);

  return waitFor(() => screen.getByTestId('error-page')).then(() => {
    const errorPage = screen.getByTestId('error-page');
    expect(errorPage).toBeInTheDocument();
  });
});
