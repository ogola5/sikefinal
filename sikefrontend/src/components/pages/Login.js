import React, { useState } from "react";
import '../styles/login.css';

function LoginPage() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [loginSuccess, setLoginSuccess] = useState(false);

  const handleEmailChange = (event) => {
    setEmail(event.target.value);
  };

  const handlePasswordChange = (event) => {
    setPassword(event.target.value);
  };

  const handleLogin = (event) => {
    event.preventDefault();
    // Check if email and password are valid
    if (email === "example@example.com" && password === "password123") {
      setLoginSuccess(true);
    } else {
      alert("Invalid email or password");
    }
  };

  return (
    <div>
      <form onSubmit={handleLogin}>
        <label>
          Email:
          <input
            type="email"
            value={email}
            onChange={handleEmailChange}
          />
        </label>
        <label>
          Password:
          <input
            type="password"
            value={password}
            onChange={handlePasswordChange}
          />
        </label>
        <button type="submit">Login</button>
      </form>
      {loginSuccess && <p>Login Successful</p>}
    </div>
  );
}

export default LoginPage;
