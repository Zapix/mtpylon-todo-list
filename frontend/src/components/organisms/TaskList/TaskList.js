import React from 'react';

import TaskItem from 'components/molecules/TaskItem';

import './TaskList.css';

function TaskList({
  taskList = [] ,
  onMarkComplete: handleMarkComplete,
  onMarkIncomplete: handleMarkIncomplete
}) {
  return (
    <div className="TaskList-container">
      {taskList.map((item) => (
        <div key={item.id} className="TaskList-item">
          <TaskItem
            task={item}
            onMarkComplete={handleMarkComplete}
            onMarkIncomplete={handleMarkIncomplete}
          />
        </div>)
      )}
    </div>
  );
}

export default TaskList;
