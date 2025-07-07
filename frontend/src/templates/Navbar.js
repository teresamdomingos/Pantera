import React from "react";
import { Link, useNavigate } from "react-router-dom";
import "../App.css";
import logo from "../images/logo.jpg";

export default function Navbar({user}) {
  const userRole = localStorage.getItem("userRole");
  const navigate = useNavigate();

  function logout() {
    localStorage.removeItem("token");
    localStorage.removeItem("userRole");
    navigate("/login");
  }

  return (
    <nav className="navbar">
      <div className="logo-nav">
        <Link to="/">
          <img src={logo} alt="Logo" className="logo-navbar" />
        </Link>
      </div>

      <ul className="itens-nav">
        <li><Link to="/jogos">Jogos</Link></li>
        <li><Link to="/equipas">Equipas</Link></li>
        <li><Link to="/atletas">Atletas</Link></li>
        {userRole === "presidente" && (
          <li><Link to="/novo-jogo">Novo Jogo (Presidente)</Link></li>
        )}
        {userRole ? (
          <li><button onClick={logout}>Logout</button></li>
        ) : (
          <li><Link to="/login">Login</Link></li>
        )}
      </ul>
    </nav>
  );
}
