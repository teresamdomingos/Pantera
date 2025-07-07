import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router-dom";
import { useState, useEffect } from "react";
import Jogos from "./templates/Jogos";
import Equipas from "./templates/Equipas";
import Atletas from "./templates/Atletas";
import Home from "./templates/Home";
import Navbar from "./templates/Navbar";
import NovoJogo from "./templates/NovoJogo";
import IniciarJogo from "./templates/IniciarJogo";
import Login from "./templates/Login";

function App() {
  const [user, setUser] = useState(null);

  // Tenta recuperar estado do login do localStorage quando a app carrega
  useEffect(() => {
    const role = localStorage.getItem("userRole");
    const token = localStorage.getItem("token");
    const nome = localStorage.getItem("userNome");
    if (token && role) {
      setUser({ token, role, nome });
    }
  }, []);

  // Protege rotas só para presidente
  function PresidenteRoute({ children }) {
    if (!user || user.role !== "presidente") {
      return <Navigate to="/login" />;
    }
    return children;
  }

  return (
    <Router>
      <Navbar user={user} />
      <div style={{ padding: "1rem" }}>
        <Routes>
          <Route path="/login" element={<Login onLogin={setUser} />} />
          <Route path="/" element={<Home />} />
          <Route path="/jogos" element={<Jogos />} />
          <Route path="/equipas" element={<Equipas />} />
          <Route path="/atletas" element={<Atletas />} />
          <Route
            path="/novo-jogo"
            element={
              <PresidenteRoute>
                <NovoJogo />
              </PresidenteRoute>
            }
          />
          <Route path="/iniciar-jogo/:id" element={<IniciarJogo />} />
          {/* Outras rotas */}
        </Routes>
      </div>
    </Router>
  );
}

export default App;
