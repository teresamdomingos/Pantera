import { useEffect, useState } from "react";

export default function Atletas() {
  const [atletas, setAtletas] = useState([]);

  useEffect(() => {
    fetch("http://localhost:8000/api/atletas/")
      .then(res => res.json())
      .then(data => setAtletas(data));
  }, []);

   return (
    <div style={{ padding: "1rem" }}>
      <h2>Lista de Atletas</h2>
      <ul>
        {atletas.map(a => (
          <li key={a.id}>
            {a.nome} {a.apelido} - Nº {a.numero_camisola} - Clube: {a.clube_nome || "Sem clube"} {a.equipa_letra || "Sem"}
          </li>
        ))}
      </ul>
    </div>
  );
}
