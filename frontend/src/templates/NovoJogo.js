import { useEffect, useState } from "react";

export default function NovoJogo() {
  const [equipas, setEquipas] = useState([]);
  const [divisoes, setDivisoes] = useState([]);
  const [divisaoSelecionada, setDivisaoSelecionada] = useState("");
  const [data, setData] = useState("");
  const [equipaCasa, setEquipaCasa] = useState("");
  const [equipaFora, setEquipaFora] = useState("");

  useEffect(() => {
    fetch("http://localhost:8000/api/equipas/")
      .then(res => res.json())
      .then(data => {
        setEquipas(data);
        const divsUnicas = [...new Set(data.map(e => e.divisao).filter(Boolean))];
        setDivisoes(divsUnicas);
      })
      .catch(err => console.error("Erro ao carregar equipas:", err));
  }, []);

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
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        data,
        equipa_casa: Number(equipaCasa),
        equipa_fora: Number(equipaFora),
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
    <div className="container mt-5 d-flex justify-content-center">
      <div className="card p-4 shadow" style={{ maxWidth: "500px", width: "100%" }}>
        <h4 className="text-center mb-4">Criar Novo Jogo</h4>
        <form onSubmit={handleSubmit}>
          <div className="mb-3">
            <label className="form-label">Data:</label>
            <input
              type="date"
              className="form-control"
              value={data}
              onChange={e => setData(e.target.value)}
              required
            />
          </div>

          <div className="mb-3">
            <label className="form-label">Divisão:</label>
            <select
              className="form-select"
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

          <div className="mb-3">
            <label className="form-label">Equipa Casa:</label>
            <select
              className="form-select"
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

          <div className="mb-3">
            <label className="form-label">Equipa Fora:</label>
            <select
              className="form-select"
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

          <div className="d-grid">
            <button type="submit" className="btn btn-success">
              Criar Jogo
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}
