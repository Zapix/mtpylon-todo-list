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

export function useSetAsCompleted(todoListId) {
  const [taskList, setTaskList] = useRecoilStateLoadable(taskListFamily(todoListId));

  return (task) => {
    const rpc = methodFromSchema(
      window.schema,
      'set_as_completed',
      { task_id: task.id },
    );
    const completedTask = { ...task, completed: true };

    setTaskList(taskList.contents.map(
      (item) => item.id === completedTask.id ? completedTask : item
    ));

    return window.connection.request(rpc)
      .catch(error => {
        console.warn(error);
        setTaskList(taskList.contents.map(
          (item) => item.id === task.id ? task : item
        ));
      });
  };
}

export function useSetAsIncompleted(todoListId) {
  const [taskList, setTaskList] = useRecoilStateLoadable(taskListFamily(todoListId));

  return (task) => {
    const rpc = methodFromSchema(
      window.schema,
      'set_as_uncompleted',
      { task_id: task.id },
    );
    const uncompletedTask = { ...task, completed: false };

    setTaskList(taskList.contents.map(
      (item) => item.id === uncompletedTask.id ? uncompletedTask : item
    ));

    return window.connection.request(rpc).catch(error => {
      console.warn(error);
      setTaskList(taskList.contents.map(
        (item) => item.id === task.id ? task : item
      ));
    });
  };
}
