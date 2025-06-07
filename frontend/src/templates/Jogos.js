import { useEffect, useState } from "react";
import { Link } from "react-router-dom";

export default function Jogos() {
  const [jogos, setJogos] = useState([]);

  useEffect(() => {
    fetch("http://localhost:8000/api/jogos/")
      .then(res => res.json())
      .then(data => setJogos(data));
  }, []);

  return (
    <div style={{ padding: "1rem" }}>
      <h2>Lista de Jogos</h2>

      {/*/ Botão para criar novo jogo*/}
      <Link to="/novo-jogo">
        <button style={{ marginBottom: "1rem" }}>Criar Novo Jogo</button>
      </Link>

      <ul>
        {jogos.map(j => (
          <li key={j.id}>
            {j.data} | {j.equipa_casa_nome} vs {j.equipa_fora_nome} @ {j.local}
          </li>
        ))}
      </ul>
    </div>
  );
}
