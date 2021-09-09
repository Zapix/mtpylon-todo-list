import * as R from 'ramda';
import { isObjectOf } from 'zagram';

export default R.pipe(
  R.prop('completed'),
);
