import { useEffect, useState } from "react";

function App() {
  const [jogadores, setJogadores] = useState([]);

  useEffect(() => {
    fetch("http://localhost:8000/api/jogadores/")
      .then(res => res.json())
      .then(data => setJogadores(data));
  }, []);

  return (
    <div>
      <h1>Jogadores</h1>
      <ul>
        {jogadores.map(j => (
          <li key={j.id}>{j.nome} - {j.pontuacao}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;