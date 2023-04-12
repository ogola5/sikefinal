import React, { useState, useEffect } from 'react';
import axios from 'axios';

function PaymentList() {
  const [payments, setPayments] = useState([]);

  useEffect(() => {
    // Retrieve payment data from backend API endpoint
    axios.get('/api/payments/')
      .then(response => {
        setPayments(response.data);
      })
      .catch(error => {
        console.log(error);
      });
  }, []);

  return (
    <div>
      <h2>Payment List</h2>
      <h2> Integration of Payment system</h2>
      
      <ul>
        {payments.map(payment => (
          <li key={payment.id}>
            <p>Payment ID: {payment.id}</p>
            <p>Amount: {payment.amount}</p>
            <p>Date: {payment.date}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default PaymentList;
