import { getMTProtoConnectionStatus, isMTProtoAuthKeyCreated } from './mtprotoHelpers';
import { is } from 'ramda';

describe('getMTProtoConnectionStatus', () => {
  afterEach(() => {
    delete window.connection;
  });

  test('INIT', () => {
    window.connection = { status: 'INIT' };
    expect(getMTProtoConnectionStatus()).toEqual('INIT');
  });
});

describe('isMTPRotoAuthKeyCreated', () => {
  afterEach(() => {
    delete window.connection;
  });

  test('not created', () => {
    window.connection = { status: 'INIT' };
    expect(isMTProtoAuthKeyCreated()).toBeFalsy();
  });

  test('created', () => {
    window.connection = { status: 'AUTH_KEY_CREATED' };
    expect(isMTProtoAuthKeyCreated()).toBeTruthy();
  });
});
