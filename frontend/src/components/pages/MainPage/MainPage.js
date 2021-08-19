import { Typography } from 'antd';
import { Link } from 'react-router-dom';

const { Title, Paragraph } = Typography;

function MainPage() {
  return (
    <div data-testid="main-page">
      <Title>Main App Page</Title>
      <Paragraph>
        <Link to="/login">Login</Link>
      </Paragraph>
    </div>
  );
}

export default MainPage;
