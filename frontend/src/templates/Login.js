import React, { useState } from "react";
import "../css/login.css";
import logo from "../images/logo.jpg";
import { useNavigate } from "react-router-dom"; 



export default function Login({ onLogin }) {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const navigate = useNavigate();

  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      const res = await fetch("http://localhost:8000/api/token/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, password }),
      });

      if (!res.ok) throw new Error("Login falhou");
      const data = await res.json();
      localStorage.setItem("token", data.access);
      localStorage.setItem("refresh_token", data.refresh);

      const resPres = await fetch("http://localhost:8000/api/is_presidente/", {
        headers: { Authorization: `Bearer ${data.access}` },
      });
      const presData = await resPres.json();

      onLogin({
        token: data.access,
        role: presData.is_presidente ? "presidente" : "utilizador",
        nome: presData.nome,
        foto_perfil: presData.foto_perfil
      });

      localStorage.setItem(
        "userRole",
        presData.is_presidente ? "presidente" : "utilizador"
      );
      localStorage.setItem("userNome", presData.nome);
      localStorage.setItem("userFoto", presData.foto_perfil);
      navigate("/");
    } catch (e) {
      setError("Credenciais inválidas");
    }
  };

  return (
    <div className="container-main">
      <div className="login-form">
        <div style={{ display: "flex", justifyContent: "center", alignItems: "center", height: "100px" }}>
          <img src={logo} alt="Logo" className="logo-navbar" style={{ height: "70px" }} />
        </div>

        <form onSubmit={handleLogin}>
          <div className="mb-3">
            <label htmlFor="username" className="form-label">Nome de utilizador</label>
            <input
              type="text"
              className="form-control"
              id="username"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              placeholder="Insira o nome de utilizador"
              required
              autoComplete="off"
            />
          </div>

          <div className="mb-3">
            <label htmlFor="password" className="form-label">Palavra-passe</label>
            <input
              type="password"
              className="form-control"
              id="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              placeholder="Insira a palavra-passe"
              required
              autoComplete="off"
            />
          </div>

          <button type="submit" className="btn btn-login w-100">Entrar</button>

          {error && (
            <div className="container mt-3">
              <div className="alert alert-danger alert-dismissible fade show" role="alert">
                {error}
                <button type="button" className="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
              </div>
            </div>
          )}
        </form>
      </div>

      <div className="footer-text">
        <p>&copy; 2025 Pantera.</p>
      </div>
    </div>
  );
}
