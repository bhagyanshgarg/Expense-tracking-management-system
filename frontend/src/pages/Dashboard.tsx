import { useEffect, useState } from "react";
import axios from "axios";
import "../styles/dashboard.css";
import React from "react";

interface Expense {
  id: number;
  title: string;
  amount: number;
  category: string;
  date: string;
  status: string;
}

export default function Dashboard() {
  const [expenses, setExpenses] = useState<Expense[]>([]);

  useEffect(() => {
    const fetchExpenses = async () => {
      try {
        const token = localStorage.getItem("token"); // Get token from local storage
        const response = await axios.get("http://localhost:8000/api/expenses/", {
          headers: { Authorization: `Bearer ${token}` },
        });
        setExpenses(response.data);
      } catch (error) {
        console.error("Failed to fetch expenses", error);
      }
    };

    fetchExpenses();
  }, []);

  return (
    <div className="dashboard-container">
      <h2>Expense Dashboard</h2>
      <table>
        <thead>
          <tr>
            <th>Title</th>
            <th>Amount</th>
            <th>Category</th>
            <th>Date</th>
            <th>Status</th>
          </tr>
        </thead>
        <tbody>
          {expenses.map((expense) => (
            <tr key={expense.id}>
              <td>{expense.title}</td>
              <td>${expense.amount}</td>
              <td>{expense.category}</td>
              <td>{expense.date}</td>
              <td>{expense.status}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
