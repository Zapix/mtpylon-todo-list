import { render, screen, waitFor } from '@testing-library/react';
import { RecoilRoot } from 'recoil';

import App from './App';

beforeEach(() => {
  window.connection = new EventTarget();
  window.connection.init = () => {};
});

afterEach(() => {
  delete window.connection;
});

test('renders loading page', () => {
  render(
    <RecoilRoot>
      <App />
    </RecoilRoot>
  );

  const loadingPage =screen.getByTestId('loading-page');
  expect(loadingPage).toBeInTheDocument();
});

test('renders main page', (done) => {
  render(
    <RecoilRoot>
      <App />
    </RecoilRoot>
  );


  const event = new Event('statusChanged');
  event.status = 'AUTH_KEY_CREATED';
  window.connection.dispatchEvent(event);

  waitFor(() => screen.getByTestId('main-page')).then(() => {
    const button = screen.getByTestId('main-page');
    expect(button).toBeInTheDocument();
    done();
  });
});

test('renders error page', (done) => {
  render(
    <RecoilRoot>
      <App />
    </RecoilRoot>
  );


  const event = new Event('statusChanged');
  event.status = 'AUTH_KEY_FAILED';
  window.connection.dispatchEvent(event);

  waitFor(() => screen.getByTestId('error-page')).then(() => {
    const button = screen.getByTestId('error-page');
    expect(button).toBeInTheDocument();
    done();
  });
});
