import validate from './validate';

test('validate required fields', () => {
  expect(validate({
    login: undefined,
    password: undefined
  })).toEqual({
    login: 'This field required',
    password: 'This field required',
  });
});

test('validate length fields', () => {
  expect(validate({
    login: 'a',
    password: 'b'
  })).toEqual({
    login: 'Login should be more then 5 chars',
    password: 'Password should be more then 5 chars'
  });
});

test('success', () => {
  expect(validate({
    login: 'zapix',
    password: '123123'
  })).toEqual({});
});
