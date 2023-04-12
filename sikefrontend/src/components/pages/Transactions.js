import React, { useState, useEffect } from "react";
import axios from "axios";
import "../styles/transaction.css"; // import your stylesheet

function TransactionsTable() {
  const [transactions, setTransactions] = useState([]);

  useEffect(() => {
    axios.get("your_backend_api_url/transactions/").then((response) => {
      setTransactions(response.data);
    });
  }, []);

  return (
    <table className="table">
      <thead>
        <tr>
          <th>Date</th>
          <th>Description</th>
          <th>Amount</th>
        </tr>
      </thead>
      <tbody>
        {transactions.map((transaction) => (
          <tr key={transaction.id}>
            <td>{transaction.date}</td>
            <td>{transaction.description}</td>
            <td>{transaction.amount}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}
export default TransactionsTable