import { atom } from 'recoil';

export const connectionStatusAtom = atom({
  key: 'connectionStatus',
  default: 'INIT',
});
