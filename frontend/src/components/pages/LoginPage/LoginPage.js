import { Typography, Row, Col } from 'antd';
import { Link } from 'react-router-dom';

import { LoginFormContainer } from 'components/organisms/LoginForm';
import 'components/templates/centered/index.css';

const { Title, Paragraph } = Typography;

function LoginPage() {
  return (
    <div className="centered-page" data-testid="login-page">
      <Title>Welcome, please login!</Title>
      <Row>
        <Col span={12} offset={6}>
          <LoginFormContainer />
        </Col>
      </Row>
      <Paragraph>
        <Link to="/register">Register</Link>
      </Paragraph>
    </div>
  );
}

export default LoginPage;
