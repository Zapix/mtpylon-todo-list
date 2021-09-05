import React from 'react';
import { useFormik } from 'formik';
import { Form, Input, Button } from 'antd';
import { PlusOutlined } from '@ant-design/icons';

import validate from './validate';

function CreateTaskForm({ onSubmit: handleSubmit = () => {} }) {
  const formik = useFormik({
    validate,
    initialValues: {
      title: '',
    },
    onSubmit: (values, { setErrors }) => handleSubmit(values)
      .then(() => formik.resetForm())
      .catch((reason) => setErrors(reason))
  });

  return (
    <Form
      name="create-task-form"
      data-testid="create-task-form"
      layout="inline"
      onFinish={formik.handleSubmit}
    >
      <Form.Item
        validateStatus={formik.touched.title && formik.errors.title ? 'error' : 'success'}
        help={formik.touched.title && formik.errors.title ? formik.errors.title : null}
      >
        <Input
          data-testid="title-field"
          type="text"
          placeholder="Task..."
          {...formik.getFieldProps('title')}
        />
      </Form.Item>
      <Form.Item>
        <Button
          data-testid="submit-button"
          htmlType="submit"
          type="primary"
          icon={<PlusOutlined />}
          disabled={formik.isSubmitting || !formik.isValid}
        >
          Add Task
        </Button>
      </Form.Item>
    </Form>
  );
}

export default CreateTaskForm;
