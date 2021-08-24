import { useSetRecoilState } from 'recoil';
import { methodFromSchema } from 'zagram';

import { meAtom } from './atoms';

export function useLogin() {
  const setMe = useSetRecoilState(meAtom);

  return (data) => {
    const rpc = methodFromSchema(window.schema, 'login', data);
    return window.connection.request(rpc)
      .then((result) => {
        setMe(result);
      })
      .catch(error => {
        return Promise.reject({ 'nonFieldError': error.errorMessage });
      });
  }
}
