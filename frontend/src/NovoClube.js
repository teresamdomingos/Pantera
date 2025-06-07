import { useState, useEffect } from "react";

function NovoClube() {
  const [clubes, setClubes] = useState([]);
  const [form, setForm] = useState({
    nome: "",
    nome_completo: "",
    local: "",
  });

  useEffect(() => {
    fetch("http://localhost:8000/api/clubes/")
      .then(res => res.json())
      .then(data => setClubes(data));
  }, []);

  const handleChange = e => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = e => {
    e.preventDefault();
    fetch("http://localhost:8000/api/clubes/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(form),
    })
      .then(res => res.json())
      .then(novoClube => {
        setClubes([...clubes, novoClube]);
        setForm({ nome: "", nome_completo: "", local: "" }); // limpar form
      });
  };

  return (
    <div>
      <h2>Novo Clube</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          name="nome"
          placeholder="Nome curto"
          value={form.nome}
          onChange={handleChange}
        />
        <input
          type="text"
          name="nome_completo"
          placeholder="Nome completo"
          value={form.nome_completo}
          onChange={handleChange}
        />
        <input
          type="text"
          name="local"
          placeholder="Local"
          value={form.local}
          onChange={handleChange}
        />
        <button type="submit">Criar Clube</button>
      </form>

      <h3>Clubes existentes:</h3>
      <ul>
        {clubes.map(clube => (
          <li key={clube.id}>{clube.nome_completo} - {clube.local}</li>
        ))}
      </ul>
    </div>
  );
}

export default NovoClube;
