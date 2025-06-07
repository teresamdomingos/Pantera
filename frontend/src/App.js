import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import Jogos from "./Jogos";
import Equipas from "./Equipas";
import Atletas from "./Atletas";
import Home from "./Home";

function App() {
  return (
    <Router>
      <div>
        <nav style={{ padding: '1rem', borderBottom: '1px solid #ccc' }}>
          <Link to="/" style={{ margin: '0 1rem' }}>Início</Link>
          <Link to="/jogos" style={{ margin: '0 1rem' }}>Jogos</Link>
          <Link to="/equipas" style={{ margin: '0 1rem' }}>Equipas</Link>
          <Link to="/atletas" style={{ margin: '0 1rem' }}>Atletas</Link>
        </nav>

        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/jogos" element={<Jogos />} />
          <Route path="/equipas" element={<Equipas />} />
          <Route path="/atletas" element={<Atletas />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
