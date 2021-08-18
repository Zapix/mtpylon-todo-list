import { Loading3QuartersOutlined } from '@ant-design/icons';

import '../../templates/centered/index.css';

function LoadingPage() {
  return (
    <div className="centered-page">
      <Loading3QuartersOutlined spin={true} style={{fontSize: '4em'}} />
    </div>
  );
}

export default LoadingPage;