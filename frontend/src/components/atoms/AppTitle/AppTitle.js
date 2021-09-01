import React from 'react';
import "./AppTitle.css";
import { Link } from 'react-router-dom';

function AppTitle({ children }) {
  return (
    <h1 className="AppTitle-title">
      <Link to="/">{children}</Link>
    </h1>
  );
}

export default AppTitle;
