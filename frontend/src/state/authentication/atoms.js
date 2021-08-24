import { atom } from 'recoil';
import { methodFromSchema } from 'zagram';
import { isMTProtoAuthKeyCreated } from 'utils/mtprotoHelpers';
import waitFor from '../../utils/waitFor';

export const meAtom = atom({
  key: 'me',
  default: waitFor(isMTProtoAuthKeyCreated)
    .then(() => {
      const rpc = methodFromSchema(window.schema, 'get_me');
      return window.connection.request(rpc);
    }),
});
