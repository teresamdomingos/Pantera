import React from "react";
import { Link } from "react-router-dom";
import "./App.css";
import logo from "./logo.jpg"; // caminho correto


export default function Navbar() {
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
      </ul>

      
    </nav>
  );
}
