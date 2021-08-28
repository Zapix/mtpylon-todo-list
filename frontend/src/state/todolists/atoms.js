import * as R from 'ramda';
import { atomFamily, selectorFamily, } from 'recoil';
import { methodFromSchema } from 'zagram';

import { meAtom } from 'state/authentication/atoms';

export const todoListsAtomFamily = atomFamily({
  key: 'todoLists',
  default: selectorFamily({
    key: 'currentUserSelector',
    get: () => ({ get }) => {
      get(meAtom);
      const rpc = methodFromSchema(window.schema, 'get_todo_lists')
      return window.connection.request(rpc)
        .then(R.propOr([], 'todo_lists'))
    },
  }),
});