function validate(input) {
  const errors = {};
  if (!input.title) {
    errors.title = 'Title is required'
  }

  return errors;
}

export default validate;
