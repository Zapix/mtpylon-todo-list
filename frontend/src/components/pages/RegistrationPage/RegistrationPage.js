import { Typography, Row, Col } from 'antd';
import { Link } from 'react-router-dom';

import 'components/templates/centered/index.css';

const { Title, Paragraph } = Typography;

function RegistrationPage() {
  return (
    <div className="centered-page" data-testid="registration-page">
      <Title>Welcome, please register!</Title>
      <Row>
        <Col span={12} offset={6}>
          Here will be registration form
        </Col>
      </Row>
      <Paragraph>
        Back to <Link to="/">Login</Link>
      </Paragraph>
    </div>
  );

}

export default RegistrationPage;
