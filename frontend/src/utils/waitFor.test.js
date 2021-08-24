import waitFor from './waitFor';

test('single check', () => {
  const check = jest.fn();
  check.mockReturnValue(true);

  return waitFor(check).then(() => {
    expect(check.mock.calls.length).toEqual(1);
  });
});

test('double check', () => {
  const check = jest.fn();
  check.mockReturnValueOnce(false).mockReturnValue(true);

  return waitFor(check).then(() => {
    expect(check.mock.calls.length).toEqual(2);
  });
});
