import React from 'react';
import { Route, Routes } from 'react-router-dom';
import HomePage from './components/pages/HomePage';
import Business from './components/pages/Business';
import Payment from './components/pages/Payment';
import Banking from './components/pages/Banking';
import Login from './components/pages/Login';
import SignUp from './components/pages/SignUp';
import Navbar from './components/pages/Navbar';
import Products from './components/pages/Products';
import Accounts from './components/pages/Accounts';
import BankAccount from './components/pages/BankAccount';
import Employee from './components/pages/Employee';

function App() {
  
  return (
    <div>
      <Navbar/>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/business" element={<Business />} />
        <Route path="/payment" element={<Payment />} />
        <Route path="/banking" element={<Banking />} />
        <Route path="/login" element={<Login />} />
        <Route path="/signup" element={<SignUp />} />
        <Route path="/products" element={<Products />} />
        <Route path="/accounts" element={<Accounts />} />
        <Route path="/bankuser" element={<BankAccount />} />
        <Route path="/employee" element={<Employee />} />
      </Routes>
    </div>
  );
}

export default App;
