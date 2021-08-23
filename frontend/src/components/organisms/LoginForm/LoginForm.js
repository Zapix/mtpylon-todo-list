import { Form, Input, Button, Alert } from 'antd';
import { UserOutlined, LockOutlined } from '@ant-design/icons';
import { useFormik } from 'formik';

import validate from './validate';

function LoginForm({ onSubmit: handleSubmit = console.log }) {
  const formik = useFormik({
    validate,
    initialValues: {
      login: '',
      password: '',
    },
    onSubmit: (values, { setErrors }) => {
      return handleSubmit(values)
        .catch((reason) => {
          setErrors(reason);
          return Promise.reject(reason);
        });
    },
  });

  return (
    <Form
      name="login-form"
      data-testid="login-form"
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
        name="login"
        validateStatus={formik.touched.login && formik.errors.login ? "error" : "success"}
        help={formik.touched.login && formik.errors.login ? formik.errors.login : null}
      >
        <Input
          data-testid="login-field"
          size="large"
          placeholder="Login"
          prefix={<UserOutlined/>}
          {...formik.getFieldProps('login')}
        />
      </Form.Item>
      <Form.Item
        validateStatus={formik.touched.password && formik.errors.password ? "error" : "success"}
        help={formik.touched.password && formik.errors.password ? formik.errors.password: null}
      >
        <Input
          data-testid="password-field"
          size="large"
          placeholder="Password"
          prefix={<LockOutlined/>}
          type="password"
          {...formik.getFieldProps('password')}
        />
      </Form.Item>
      <Form.Item>
        <Button
          data-testid="submit-button"
          type="primary"
          htmlType="submit"
          disabled={formik.isSubmitting || !formik.isValid}
        >
          Login
        </Button>
      </Form.Item>
    </Form>
  );
}

export default LoginForm;
