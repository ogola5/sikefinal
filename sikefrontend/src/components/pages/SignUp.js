import React, { useState } from "react";
import '../styles/signup.css';
import axios from 'axios';
import { useNavigate } from "react-router-dom";

function SignupForm() {
  const [formData, setFormData] = useState({
    business_name: "",
    email: "",
    contact: "",
    business_owner: "",
    nationality: "",
    business_category: "",
    password: "",
    confirm_password: "",
  });

  const navigate = useNavigate();

  const handleChange = (event) => {
    const { name, value } = event.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    axios.post('/api/business/', formData)
      .then(response => {
          // Handle successful response
      })
      .catch(error => {
          // Handle error
      });
    // Clear the form
    setFormData({
      business_name: "",
      email: "",
      contact: "",
      business_owner: "",
      nationality: "",
      business_category: "",
      password: "",
      confirm_password: "",
    });
    // Redirect to login page
    navigate("/login");
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Business Name:
        <input
          type="text"
          name="business_name"
          value={formData.business_name}
          onChange={handleChange}
        />
      </label>
      <label>
        Email:
        <input
          type="email"
          name="email"
          value={formData.email}
          onChange={handleChange}
        />
      </label>
      <label>
        Contact (with country code):
        <input
          type="text"
          name="contact"
          value={formData.contact}
          onChange={handleChange}
        />
      </label>
      <label>
        Business Owner:
        <input
          type="text"
          name="business_owner"
          value={formData.business_owner}
          onChange={handleChange}
        />
      </label>
      <label>
        Nationality:
        <input
          type="text"
          name="nationality"
          value={formData.nationality}
          onChange={handleChange}
        />
      </label>
      <label>
        Business Category:
        <input
          type="text"
          name="business_category"
          value={formData.business_category}
          onChange={handleChange}
        />
      </label>
      <label>
        Password:
        <input
          type="text"
          name="password"
          value={formData.password}
          onChange={handleChange}
        />
      </label>
      <label>
        confirm password:
        <input
          type="text"
          name="confirm_password"
          value={formData.confirm_password}
          onChange={handleChange}
        />
      </label>
      <button type="submit">Submit</button>
    </form>
  )
}
export default SignupForm