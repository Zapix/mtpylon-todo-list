import { Form, Input, Button, Alert } from 'antd';
import { UserOutlined, LockOutlined } from '@ant-design/icons';
import { useFormik } from 'formik';

import validate from './validate';

function RegistrationForm({ onSubmit: handleSubmit = () => {} }) {
  const formik = useFormik({
    validate,
    initialValues: {
      nickname: '',
      password: '',
      confirmPassword: '',
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
      name="register-form"
      data-testid="register-form"
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
        name="nickname"
        validateStatus={formik.touched.nickname && formik.errors.nickname ? "error" : "success"}
        help={formik.touched.nickname && formik.errors.nickname ? formik.errors.nickname : null}
      >
        <Input
          data-testid="nickname-field"
          size="large"
          placeholder="Nickname"
          prefix={<UserOutlined />}
          {...formik.getFieldProps('nickname')}
        />
      </Form.Item>
      <Form.Item
        name="password"
        validateStatus={formik.touched.password && formik.errors.password ? "error" : "success"}
        help={formik.touched.password && formik.errors.password ? formik.errors.password : null}
      >
        <Input
          data-testid="password-field"
          size="large"
          placeholder="Password"
          prefix={<LockOutlined />}
          {...formik.getFieldProps('password')}
        />
      </Form.Item>
      <Form.Item
        name="confirm-password"
        validateStatus={formik.touched.confirmPassword && formik.errors.confirmPassword ? (
          "error"
        ) : (
          "success"
        )}
        help={formik.touched.confirmPassword && formik.errors.confirmPassword ? (
          formik.errors.confirmPassword
        ) : (
          null
        )}
      >
        <Input
          data-testid="confirm-password-field"
          size="large"
          placeholder="Confirm Password"
          prefix={<LockOutlined />}
          {...formik.getFieldProps('confirmPassword')}
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

export default RegistrationForm;
