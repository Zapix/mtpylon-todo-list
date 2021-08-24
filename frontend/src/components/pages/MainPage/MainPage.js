import { Typography } from 'antd';
import { Link } from 'react-router-dom';
import { useRecoilValueLoadable } from 'recoil';

import { meAtom } from '../../../state/authentication/atoms';

const { Title, Paragraph } = Typography;

function MainPage() {
  const me = useRecoilValueLoadable(meAtom);

  return (
    <div data-testid="main-page">
      <Title>Main App Page</Title>
      <Paragraph>
        <Title level={3}>Welcome, {me.contents.nickname}!</Title>
        <Link to="/login">Login</Link>
      </Paragraph>
    </div>
  );
}

export default MainPage;
