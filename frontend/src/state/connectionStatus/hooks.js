import { useEffect } from 'react';
import { useRecoilCallback } from 'recoil';

import { connectionStatusAtom } from './atoms';

export function useMTprotoConnection(connection) {
  const updateStatus = useRecoilCallback(({ set })  => (state) => {
    set(connectionStatusAtom, state);
  });

  useEffect(() => {
    connection.addEventListener('statusChanged', (e) => {
      console.log(`MTProto status: ${e.status}`);
      updateStatus(e.status);
    })
    window.connection.init();
  }, []);
}
