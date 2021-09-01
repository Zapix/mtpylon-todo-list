import { useRecoilStateLoadable } from 'recoil';
import { methodFromSchema } from 'zagram';

import { todoListsAtomFamily } from './atoms';

export function useCreateTodoList() {
  const [todoLists, setTodoLists] = useRecoilStateLoadable(todoListsAtomFamily());

  return (data) => {
    const rpc = methodFromSchema(window.schema, 'create_todo_list', data)
    return window.connection.request(rpc)
      .then(data => {
        console.log('Add new todo list:', data);
        console.log('Existing todoLists:', todoLists);
        setTodoLists([data, ...todoLists.contents]);
        return data;
      })
      .catch(error => {
        return Promise.reject({ nonFieldError: error.errorMessage});
      });
  };
}