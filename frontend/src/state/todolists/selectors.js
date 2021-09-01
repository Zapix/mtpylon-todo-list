import * as R from 'ramda';
import { selector } from 'recoil';

import { selectedTodoListIdAtom, todoListsAtomFamily } from './atoms';

export const selectedTodoListSelector = selector({
  'key': 'selectedTodoListSelector',
  get: ({ get }) => {
    const todoListId = get(selectedTodoListIdAtom);

    if (R.isNil(todoListId)) {
      return null;
    }

    const todoLists = get(todoListsAtomFamily());
    const findById = R.propEq('id', parseInt(todoListId, 10));

    return R.find(findById, todoLists);
  }
});
