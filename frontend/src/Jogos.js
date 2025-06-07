import { useEffect, useState } from "react";

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
      <ul>
        {jogos.map(j => (
          <li key={j.id}>
            {j.data} | {j.equipa_casa} vs {j.equipa_fora} @ {j.local}
          </li>
        ))}
      </ul>
    </div>
  );
}
