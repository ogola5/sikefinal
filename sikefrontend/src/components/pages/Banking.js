import React from 'react';
import {Route, Routes, Link, useMatch } from 'react-router-dom';
import Transactions from './Transactions';
import BankAccount from './BankAccount';
import Accounts from './Accounts';

function Banking() {
  // const match = useMatch();

  return (
    <div>
      <h1>Banking System</h1>
      <h2>We offer the following services:</h2>
      <ul>
        <li>Savings</li>
        <li>Loans to Business</li>
        <li>Keep track of all transactions</li>
      </ul>
      {/* <nav>
        <ul>
          <li><Link to={`${match.url}/transactions`}>Transactions</Link></li>
          <li><Link to={`${match.url}/bankaccount`}>Bank Account</Link></li>
          <li><Link to={`${match.url}/account`}>Accounts</Link></li>
        </ul>
      </nav>
      <Routes>
        <Route path={`${match.path}/transactions`} element={<Transactions />} />
        <Route path={`${match.path}/bankaccount`} element={<BankAccount />} />
        <Route path={`${match.path}/account`} element={<Accounts />} />
      </Routes> */}
    </div>
  );
}

export default Banking;

// function App() {
//   return (
//     <Router>
//       <Banking />
//     </Router>
//   );
// }

// export default App;
