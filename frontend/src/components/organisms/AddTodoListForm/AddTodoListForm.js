import React from 'react';
import { Form, Input, Button, Alert } from 'antd';
import { PlusOutlined } from '@ant-design/icons';
import { useFormik } from 'formik';

import validate from './validate';

function AddTodoListForm({ onSubmit: handleSubmit = () => {} }) {
  const formik = useFormik({
    validate,
    initialValues: {
      title: '',
    },
    onSubmit: (values, { setErrors }) => {
      return handleSubmit(values)
        .catch((reason) => {
          setErrors(reason);
          return Promise.reject(reason);
        });
    },
  })
  return (
    <Form
      name="add-todo-list-form"
      data-testid="add-todo-list_form"
      onFinish={formik.handleSubmit}
    >
      <Form.Item>
        {formik.errors.nonFieldError ? (
          <Alert
            data-testid="error-alert"
            message={formik.errors.nonFieldError}
            type="error"
          />
        ) : null}
      </Form.Item>
      <Form.Item
        validateStatus={formik.errors.title && formik.touched.title ? "error" : "" }
        help={formik.errors.title && formik.touched.title ? formik.errors.title : null}
      >
        <Input
          data-testid="title-field"
          placeholder="ToDo List"
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
          Create List
        </Button>
      </Form.Item>
    </Form>
  );
}

export default AddTodoListForm;
