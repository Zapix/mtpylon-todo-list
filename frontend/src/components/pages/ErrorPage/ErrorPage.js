import { Typography } from 'antd'
import { FrownOutlined } from '@ant-design/icons';

import '../../templates/centered/index.css';
import './ErrorPage.css';

const { Title } = Typography;

function ErrorPage({ message = "Something goes wrong" }) {
  return (
    <div className="centered-page">
      <div className="ErrorPage-container" data-testid="error-page">
        <FrownOutlined style={{fontSize: '4em'}} />
        <Title>{message}</Title>
      </div>
    </div>
  );
}

export default ErrorPage;
