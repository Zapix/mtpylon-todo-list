import { useRecoilValueLoadable } from 'recoil'
import { Redirect, Route} from 'react-router-dom';
import { isObjectOf } from 'zagram';

import { meAtom } from 'state/authentication/atoms';

function AuthenticatedRoute({ children, ...rest }) {
  const me = useRecoilValueLoadable(meAtom);
  return (
    <Route
      {...rest}
      render={({ location }) => (
        isObjectOf('registered_user', me.contents) ? (
          children
        ) : (
          <Redirect
            to={{
              pathname: '/login',
              state: { from: location }
            }}
          />
        )
      )}
    />
  );
}

export default AuthenticatedRoute;
