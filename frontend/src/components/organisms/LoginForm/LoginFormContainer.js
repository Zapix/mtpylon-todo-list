import { useLogin } from 'state/authentication/hooks';

import LoginForm from './LoginForm';

function LoginFormContainer() {
  const login = useLogin();

  return (
    <LoginForm onSubmit={login} />
  );
}

export default LoginFormContainer;
