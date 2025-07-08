import { BrowserRouter as Router, Routes, Route, Navigate, Outlet } from "react-router-dom";
import { useState, useEffect } from "react";
import Jogos from "./templates/Jogos";
import Equipas from "./templates/Equipas";
import Atletas from "./templates/Atletas";
import Home from "./templates/Home";
import Navbar from "./templates/Navbar";
import NovoJogo from "./templates/NovoJogo";
import IniciarJogo from "./templates/IniciarJogo";
import Login from "./templates/Login";
import 'bootstrap/dist/css/bootstrap.min.css';

function App() {
  const [user, setUser] = useState(null);

  useEffect(() => {
    const role = localStorage.getItem("userRole");
    const token = localStorage.getItem("token");
    const nome = localStorage.getItem("userNome");
    const foto_perfil = localStorage.getItem("userFoto");
    if (token && role) {
      setUser({ token, role, nome, foto_perfil});
    }
  }, []);

  function PresidenteRoute({ children }) {
    if (!user || user.role !== "presidente") {
      return <Navigate to="/login" />;
    }
    return children;
  }

  // Layout com Navbar (apenas para páginas autenticadas)
  const AppLayout = () => (
    <>
      <Navbar user={user} />
      <div style={{ padding: "1rem" }}>
        <Outlet />
      </div>
    </>
  );

  return (
    <Router>
      <Routes>
        {/* Página de login SEM Navbar */}
        <Route path="/login" element={<Login onLogin={setUser} />} />

        {/* Rotas com Navbar */}
        <Route element={<AppLayout />}>
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
        </Route>
      </Routes>
    </Router>
  );
}

export default App;
