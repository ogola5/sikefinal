import React, { useState, useEffect } from 'react';

function Accounts() {
  const [accounts, setAccounts] = useState([]);

  useEffect(() => {
    async function fetchAccounts() {
      const response = await fetch('http://127.0.0.1:8000/accounts/');
      const data = await response.json();
      setAccounts(data);
    }
    fetchAccounts();
  }, []);

  return (
    <table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Maximum Withdrawal Amount</th>
          <th>Annual Interest Rate</th>
          <th>Interest Calculation per Year</th>
        </tr>
      </thead>
      <tbody>
        {accounts.map((account) => (
          <tr key={account.id}>
            <td>{account.name}</td>
            <td>{account.maximum_withdrawal_amount}</td>
            <td>{account.annual_interest_rate}%</td>
            <td>{account.interest_calculation_per_year}%</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}

export default Accounts;
