import React from 'react';

import "./TitleWithIcon.css";

function TitleWithIcon({ icon, children }) {
  return (
    <h3 className="TitleWithIcon-title">
      {icon}&nbsp;{children}
    </h3>
  );
}

export default TitleWithIcon;
