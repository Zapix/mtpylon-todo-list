import RegistrationForm from './RegistrationForm';

import { useRegister } from 'state/authentication/hooks';

function RegistrationFormContainer() {
  const register = useRegister();

  return (
    <RegistrationForm onSubmit={register} />
  );
}

export default RegistrationFormContainer;
