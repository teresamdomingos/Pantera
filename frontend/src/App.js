import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import Jogos from "./Jogos";
import Equipas from "./Equipas";
import Atletas from "./Atletas";
import Home from "./Home";
import Navbar from "./Navbar";

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
          {/* Podes adicionar rota para "/" com uma homepage se quiseres */}
        </Routes>
      </div>
    </Router>
  );
}

export default App;
