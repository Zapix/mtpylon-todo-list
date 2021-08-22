import { Form, Input, Button } from 'antd';
import { UserOutlined, LockOutlined } from '@ant-design/icons';

function LoginForm({ onSubmit: handleSubmit = console.log }) {
  return (
    <Form
      name="login-form"
    >
      <Form.Item
        name="login"
      >
        <Input
          size="large"
          placeholder="Login"
          prefix={<UserOutlined/>}
        />
      </Form.Item>
      <Form.Item
        name="password"
      >
        <Input
          size="large"
          placeholder="Password"
          prefix={<LockOutlined/>}
        />
      </Form.Item>
      <Form.Item>
        <Button
          type="primary"
          htmlType="submit"
          onSubmit={handleSubmit}
        >
          Login
        </Button>
      </Form.Item>
    </Form>
  );
}

export default LoginForm;
