import validate from './validate';

test('test validate error', () => {
  const errors = validate({});
  expect(errors).toEqual({
    title: 'Title is required',
  });
});

test('test validate success', () => {
  const errors = validate({ title: 'New list' });
  expect(errors).toEqual({});
});
