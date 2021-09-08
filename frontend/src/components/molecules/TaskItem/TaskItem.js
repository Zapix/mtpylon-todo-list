import React from 'react';
import { Button, Tooltip } from 'antd';
import { CheckOutlined, CloseOutlined } from '@ant-design/icons';
import { isObjectOf } from 'zagram';

import './TaskItem.css';

function TaskItem({ task }) {
  return (
    <div className="TaskItem-container">
      <div className="TaskItem-title">
        task item {task.title}
      </div>
      <div className="TaskItem-actions">
        {
          isObjectOf('boolTrue', task.status) ? (
            <Tooltip title="Mark as incomplete">
              <Button
                type="primary"
                shape="circle"
                danger
                icon={<CloseOutlined />}
              />
            </Tooltip>
          ): (
            <Tooltip title="mark as complete">
              <Button
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
