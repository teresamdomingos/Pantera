import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import Jogos from "./templates/Jogos";
import Equipas from "./templates/Equipas";
import Atletas from "./templates/Atletas";
import Home from "./templates/Home";
import Navbar from "./templates/Navbar";
import NovoJogo from "./templates/NovoJogo";

function App() {
  return (
    <Router>
      <Navbar />
      <div style={{ padding: "1rem" }}>
        <Routes>
           <Route path="/" element={<Home />} />
          <Route path="/jogos" element={<Jogos />} />
          <Route path="/equipas" element={<Equipas />} />
          <Route path="/atletas" element={<Atletas />} />
          <Route path="/novo-jogo" element={<NovoJogo />} /> {/* nova rota */}
          {/* Podes adicionar rota para "/" com uma homepage se quiseres */}
        </Routes>
      </div>
    </Router>
  );
}

export default App;
