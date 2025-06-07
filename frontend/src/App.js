import { useEffect, useState } from "react";
import NovoClube from './NovoClube';

function App() {
  const [jogadores, setJogadores] = useState([]);
  const [jogos, setJogos] = useState([]);

  useEffect(() => {
    fetch("http://localhost:8000/api/jogadores/")
      .then(res => res.json())
      .then(data => setJogadores(data));
  }, []);

  useEffect(() => {
    fetch("http://localhost:8000/api/jogos/")
      .then(res => res.json())
      .then(data => setJogos(data));
  }, []);

  return (
    <div>
      <h1>Jogadores</h1>
      <ul>
        {jogadores.map(j => (
          <li key={j.id}>{j.nome} - {j.pontuacao}</li>
        ))}
      </ul>

      <h1>Jogos</h1>
      <ul>
        {jogos.map(j => (
          <li key={j.id}>
            {j.data} | Equipa Casa: {j.equipa_casa} | Equipa Fora: {j.equipa_fora} | Local: {j.local}
          </li>
        ))}
      </ul>
      <NovoClube />
    </div>
  );
}

export default App;
