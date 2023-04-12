import React, { useState } from 'react';
import '../styles/navbar.css';

const Navbar = () => {
  const [showMenu, setShowMenu] = useState(false);

  const handleMenuClick = () => {
    setShowMenu(!showMenu);
  };

  return (
    <nav className="navbar">
      <div className="navbar-left">
        <a href="/" className="logo">
          SikePay
        </a>
      </div>
      <div className={`navbar-right ${showMenu ? 'active' : ''}`}>
        <ul className="nav-links">
          <li>
            <a href="/banking">Banking</a>
          </li>
          <li>
            <a href="/business">Business</a>
          </li>
          
          <li>
            <a href="/payment">Payment</a>
          </li>
          <li>
            <a href="/employee">Employees Management</a>
          </li>
        </ul>
        <div className="navbar-buttons">
          <a href="/login">
            <button className="login-btn">Login</button>
          </a>
          <a href="/signup">
            <button className="signup-btn">Sign Up</button>
          </a>
        </div>
      </div>
      <div className="navbar-menu" onClick={handleMenuClick}>
        <div className={`menu-icon ${showMenu ? 'active' : ''}`}>
          <span></span>
          <span></span>
          <span></span>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;





