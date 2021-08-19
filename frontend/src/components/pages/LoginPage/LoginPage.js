import { Typography } from 'antd';
import { Link } from 'react-router-dom';

import '../../templates/centered/index.css';

const { Title, Paragraph } = Typography;

function LoginPage() {
  return (
    <div className="centered-page" data-testid="login-page">
      <Title>Login Page</Title>
      <Paragraph>
        <Link to="/">Back to main</Link>
      </Paragraph>
    </div>
  );
}

export default LoginPage;
