import { useRecoilStateLoadable } from 'recoil';
import { methodFromSchema } from 'zagram';

import { todoListsAtomFamily, taskListFamily } from './atoms';

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

export function useCreateTask(todoListId) {
  const [taskList, setTaskList] = useRecoilStateLoadable(taskListFamily(todoListId));

  return (data) => {
    const rpc = methodFromSchema(
      window.schema,
      'create_task',
      {
        todo_list_id: todoListId,
        ...data,
      }
    );

    return window.connection.request(rpc).then(data => {
      console.log('Add new task: ', data);
      console.log('Existing task list:', taskList);
      setTaskList([data, ...taskList.contents]);
      return data;
    })
      .catch(error => {
        return Promise.reject({ nonFieldError: error.errorMessage });
      })
  };
}
