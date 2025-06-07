import { useEffect, useState } from "react";

export default function NovoJogo() {
  const [equipas, setEquipas] = useState([]);
  const [divisoes, setDivisoes] = useState([]);
  const [divisaoSelecionada, setDivisaoSelecionada] = useState("");
  const [data, setData] = useState("");
  const [equipaCasa, setEquipaCasa] = useState("");
  const [equipaFora, setEquipaFora] = useState("");

  useEffect(() => {
    // Buscar lista de equipas da API
    fetch("http://localhost:8000/api/equipas/")
      .then(res => res.json())
      .then(data => {
        setEquipas(data);

        // Extrair as divisões únicas para o filtro
        const divsUnicas = [...new Set(data.map(e => e.divisao).filter(Boolean))];
        setDivisoes(divsUnicas);
      })
      .catch(err => console.error("Erro ao carregar equipas:", err));
  }, []);

  // Equipas filtradas pela divisão selecionada
  const equipasFiltradas = divisaoSelecionada
    ? equipas.filter(e => e.divisao === divisaoSelecionada)
    : [];

  const handleSubmit = (e) => {
    e.preventDefault();

    if (equipaCasa === equipaFora) {
      alert("A equipa casa e a equipa fora não podem ser iguais!");
      return;
    }

    fetch("http://localhost:8000/api/jogos/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        data,
        equipa_casa: Number(equipaCasa),
        equipa_fora: Number(equipaFora),
        // local pode vir da backend, então podes remover daqui
      })
    })
    .then(res => {
      if (res.ok) {
        alert("Jogo criado com sucesso!");
        setData("");
        setEquipaCasa("");
        setEquipaFora("");
        setDivisaoSelecionada("");
      } else {
        alert("Erro ao criar jogo.");
      }
    })
    .catch(err => alert("Erro: " + err));
  };

  return (
    <form onSubmit={handleSubmit} style={{ padding: "1rem" }}>
      <h2>Criar Novo Jogo</h2>

      <div>
        <label>Data:</label><br />
        <input
          type="date"
          value={data}
          onChange={e => setData(e.target.value)}
          required
        />
      </div>

      <div>
        <label>Divisão:</label><br />
        <select
          value={divisaoSelecionada}
          onChange={e => setDivisaoSelecionada(e.target.value)}
          required
        >
          <option value="">-- Seleciona divisão --</option>
          {divisoes.map(div => (
            <option key={div} value={div}>{div}</option>
          ))}
        </select>
      </div>

      <div>
        <label>Equipa Casa:</label><br />
        <select
          value={equipaCasa}
          onChange={e => setEquipaCasa(e.target.value)}
          required
          disabled={!divisaoSelecionada}
        >
          <option value="">-- Seleciona equipa casa --</option>
          {equipasFiltradas.map(e => (
            <option key={e.id} value={e.id}>{e.nome} ({e.letra})</option>
          ))}
        </select>
      </div>

      <div>
        <label>Equipa Fora:</label><br />
        <select
          value={equipaFora}
          onChange={e => setEquipaFora(e.target.value)}
          required
          disabled={!divisaoSelecionada}
        >
          <option value="">-- Seleciona equipa fora --</option>
          {equipasFiltradas.map(e => (
            <option key={e.id} value={e.id}>{e.nome} ({e.letra})</option>
          ))}
        </select>
      </div>

      <button type="submit" style={{ marginTop: "10px" }}>Criar Jogo</button>
    </form>
  );
}
