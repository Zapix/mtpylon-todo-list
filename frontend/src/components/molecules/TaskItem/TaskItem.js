import React from 'react';
import classNames from 'classnames';
import { Button, Tooltip } from 'antd';
import { CheckOutlined, CloseOutlined } from '@ant-design/icons';
import isTaskDone from 'utils/isTaskDone';

import './TaskItem.css';

function TaskItem({
  task,
  onMarkComplete: handleMarkComplete = () => {},
  onMarkIncomplete: handleMarkIncomplete = () => {}
}) {
  return (
    <div className={classNames({
      'TaskItem-container': true,
      completed: isTaskDone(task),
    })}>
      <div className="TaskItem-title">
        {task.title}
      </div>
      <div className="TaskItem-actions">
        {
          isTaskDone(task) ? (
            <Tooltip title="Mark as incomplete">
              <Button
                onClick={(e) =>  {
                  e.preventDefault();
                  handleMarkIncomplete(task);
                }}
                data-testid="mark-as-incomplete-button"
                type="primary"
                shape="circle"
                danger
                icon={<CloseOutlined />}
              />
            </Tooltip>
          ): (
            <Tooltip title="mark as complete">
              <Button
                onClick={(e) => {
                  e.preventDefault();
                  handleMarkComplete(task);
                }}
                data-testid="mark-as-complete-button"
                type="primary"
                shape="circle"
                icon={<CheckOutlined />}
              />
            </Tooltip>
          )
        }
      </div>
    </div>
  );
}

export default TaskItem;
