import React, { useState, useEffect } from 'react';
import axios from 'axios';

function BusinessList() {
  const [businesses, setBusinesses] = useState([]);

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/onlinestore/Customers/')
      .then(response => {
        setBusinesses(response.data);
      })
      .catch(error => {
        console.log(error);
      });
  }, []);

  return (
    <div>
      <h1>Businesses</h1>
      <p>Here offers the following:</p>
      <ul>
        <li>Online Store for Businesses</li>
        <li>Point Of Sales for Shops</li>
        <li>Product Payment Method</li>
        <li>Product marketing</li>
      </ul>
      {businesses.map(business => (
        <div key={business.id}>
          <h2>{business.name}</h2>
          <p>{business.description}</p>
        </div>
      ))}
    </div>
  );
}

export default BusinessList;
