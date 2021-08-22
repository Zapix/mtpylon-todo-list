/**
 * @param {{login: string, password: string}} values
 * @return {{login: string, password: string}} - errors for login form
 */
function validate(values) {
  const errors = {};

  if (!values.login) {
    errors.login = 'This field required';
  } else if (values.login.length < 5){
    errors.login = 'Login should be more then 5 chars'
  }

  if (!values.password) {
    errors.password = 'This field required';
  } else if (values.password.length < 5) {
    errors.password = 'Password should be more then 5 chars'
  }

  return errors;
}

export default validate;
