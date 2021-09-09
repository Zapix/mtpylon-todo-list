import * as R from 'ramda';
import { atom, atomFamily, selectorFamily, } from 'recoil';
import { methodFromSchema } from 'zagram';

import { meAtom } from 'state/authentication/atoms';

export const selectedTodoListIdAtom = atom({
  key: 'selectedTodoList',
  default: null,
})

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

export const taskListFamily = atomFamily({
  key: 'taskList',
  default: selectorFamily({
    key: 'taskList/default',
    get: (todoListId) => ({ get }) => {
      console.log(`Select for todo list: ${todoListId}`);

      const rpc = methodFromSchema(window.schema, 'get_task_list', { todo_list_id: todoListId });
      console.log(rpc);

      return window.connection.request(rpc).then(data => {
        return data.tasks;
      });
    },
  }),
});
