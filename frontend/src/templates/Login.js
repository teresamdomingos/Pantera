import React, { useState } from "react";

export default function Login({ onLogin }) {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      const res = await fetch("http://localhost:8000/api/token/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, password }),
        
      });
      console.log("A enviar login:", { username, password });

      if (!res.ok) throw new Error("Login falhou");
      const data = await res.json();
      localStorage.setItem("token", data.access);
      localStorage.setItem("refresh_token", data.refresh);

      // Opcional: confirma se é presidente
      const resPres = await fetch("http://localhost:8000/api/is_presidente/", {
        headers: { Authorization: `Bearer ${data.access}` },
      });
      const presData = await resPres.json();

      onLogin({token: data.access,role: presData.is_presidente ? "presidente" : "utilizador", nome: presData.nome});
      localStorage.setItem("userRole", presData.is_presidente ? "presidente" : "utilizador");
      localStorage.setItem("userNome", presData.nome);
    } catch (e) {
      setError("Credenciais inválidas");
    }
  };

  return (
    <form onSubmit={handleLogin}>
      <input value={username} onChange={e => setUsername(e.target.value)} placeholder="Username" />
      <input type="password" value={password} onChange={e => setPassword(e.target.value)} placeholder="Password" />
      <button type="submit">Login</button>
      {error && <p>{error}</p>}
    </form>
  );
}
