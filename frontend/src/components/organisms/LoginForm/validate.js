/**
 * @param {{nickname: string, password: string}} values
 * @return {{nickname: string, password: string}} - errors for nickname form
 */
function validate(values) {
  const errors = {};

  if (!values.nickname) {
    errors.nickname = 'This field required';
  } else if (values.nickname.length < 5){
    errors.nickname = 'Login should be more then 5 chars'
  }

  if (!values.password) {
    errors.password = 'This field required';
  } else if (values.password.length < 5) {
    errors.password = 'Password should be more then 5 chars'
  }

  return errors;
}

export default validate;
