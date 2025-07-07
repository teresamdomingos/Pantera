import { useEffect, useState } from "react";
import { Link, useNavigate } from "react-router-dom";


export default function Jogos() {
  const [jogos, setJogos] = useState([]);
  const navigate = useNavigate();


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
        <button className="btn btn-secondary mb-3">Criar Novo Jogo</button>
      </Link>




      <ul>
        {jogos.map(j => (
          <li key={j.id} className="mb-2 d-flex align-items-center justify-content-between">
            <span>
              {j.data} | {j.equipa_casa_nome} vs {j.equipa_fora_nome} @ {j.local}
            </span>

            {/* Botão iniciar jogo */}
            <button
              className="btn btn-primary btn-sm"
              onClick={() => navigate(`/iniciar-jogo/${j.id}`)}
            >
              Iniciar Jogo
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
}
