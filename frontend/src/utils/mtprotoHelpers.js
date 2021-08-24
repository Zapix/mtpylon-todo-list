import * as R from 'ramda';

export const getMTProtoConnectionStatus = R.partial(
  R.pathOr,
  [
    'INIT',
    ['connection', 'status'],
    window
  ]
);


export const isMTProtoAuthKeyCreated = R.pipe(
  getMTProtoConnectionStatus,
  R.equals('AUTH_KEY_CREATED'),
);