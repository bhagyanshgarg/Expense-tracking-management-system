import { Link } from "react-router-dom";
import "../styles/navbar.css";
import React from "react";

export default function Navbar() {
  return (
    <nav className="navbar">
      <h1>Expense Tracker</h1>
      <ul>
        <li><Link to="/">Dashboard</Link></li>
        <li><Link to="/login">Login</Link></li>
        <li><Link to="/register">Register</Link></li>
      </ul>
    </nav>
  );
}
