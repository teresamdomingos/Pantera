import React from "react";
import { Link, useNavigate } from "react-router-dom";
import "../App.css";
import logo from "../images/logo.jpg";
import 'bootstrap/dist/js/bootstrap.bundle.min.js';


export default function Navbar({ user }) {
  const navigate = useNavigate();

  function logout() {
    localStorage.removeItem("token");
    localStorage.removeItem("userRole");
    localStorage.removeItem("userNome");
    localStorage.removeItem("userFoto"); 

    navigate("/login");
  }

  const userNome = user?.nome || "Utilizador";
  const userRole = user?.role;
  const avatarUrl = user?.foto_perfil
  ? user.foto_perfil.startsWith("/media/")
    ? `http://localhost:8000${user.foto_perfil}` // já tem /media/, só junta host
    : `http://localhost:8000/media/${user.foto_perfil}` // adiciona /media/
  : "https://via.placeholder.com/50";
  return (
    <nav className="navbar navbar-expand-lg">
      <div className="container-fluid logo-nav">
        <Link to="/" className="d-flex align-items-center">
          <img src={logo} alt="Logo" className="logo-navbar" />
        </Link>

        {/* Centro - Itens de navegação */}
        <div className="itens-nav-container">
          <ul className="navbar-nav itens-nav">
            <li className="nav-item">
              <Link to="/jogos" className="nav-link">Jogos</Link>
            </li>
            <li className="nav-item">
              <Link to="/equipas" className="nav-link">Equipas</Link>
            </li>
            <li className="nav-item">
              <Link to="/atletas" className="nav-link">Atletas</Link>
            </li>
            {userRole === "presidente" && (
              <li className="nav-item">
                <Link to="/novo-jogo" className="nav-link">Novo Jogo</Link>
              </li>
            )}
          </ul>
        </div>
        {/* Direita - Utilizador */}
        
        <div className="header-right d-flex align-items-center">
          {userRole ? (
            <>
              <span className="user-name me-2">{userNome}</span>
              <div className="user-avatar dropdown position-relative">
                <a href="#" className="dropdown-toggle seta_dropdown" data-bs-toggle="dropdown" aria-expanded="false">
                  <img src={avatarUrl} alt="Foto de perfil" className="avatar-img" />

                </a>
                <ul className="dropdown-menu dropdown-menu-end">
                  <li><a className="dropdown-item" href="#"><i className="fa-solid fa-user"></i> Perfil</a></li>
                  <li><hr className="dropdown-divider" /></li>
                  <li>
                    <button className="dropdown-item" onClick={logout}>
                      <i className="fa-solid fa-right-from-bracket"></i> Terminar sessão
                    </button>
                  </li>
                </ul>
              </div>
            </>
          ) : (
            <Link to="/login" className="btn btn-secondary">Login</Link>
          )}
        </div>
      </div>
    </nav>
  );
}
