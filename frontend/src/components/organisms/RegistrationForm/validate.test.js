import validate from './validate';

test('validate required fields', () => {
  expect(validate({
    nickname: undefined,
    password: undefined
  })).toEqual({
    nickname: 'This field required',
    password: 'This field required',
  });
});

test('validate length fields', () => {
  expect(validate({
    nickname: 'a',
    password: 'b',
    confirmPassword: 'b',
  })).toEqual({
    nickname: 'Login should be more then 5 chars',
    password: 'Password should be more then 5 chars'
  });
});

test('passwords should match', () => {
  expect(validate({
    nickname: 'zapix',
    password: '123123',
    confirmPassword: '12',
  })).toEqual({
    password: 'Passwords should match',
  });
});

test('success', () => {
  expect(validate({
    nickname: 'zapix',
    password: '123123',
    confirmPassword: '123123',
  })).toEqual({});
});