import { useState, useEffect, useRef } from "react";
import { useParams } from "react-router-dom";

export default function IniciarJogo() {
  const { id } = useParams();
  const [quartoAtual, setQuartoAtual] = useState(1);
  const [tempoRestante, setTempoRestante] = useState(10); // 10s por quarto para teste
  const [pontosCasa, setPontosCasa] = useState(0);
  const [pontosFora, setPontosFora] = useState(0);
  const [isRunning, setIsRunning] = useState(false);
  const [isPause, setIsPause] = useState(false);
  const [pausaRestante, setPausaRestante] = useState(0);
  const [resultadoFinal, setResultadoFinal] = useState(null); // NOVO: guarda resultado final

  const intervalRef = useRef(null);

  const temposDePausa = {
    1: 60,    // 1 minuto entre Q1 e Q2
    2: 600,   // 10 minutos entre Q2 e Q3
    3: 60     // 1 minuto entre Q3 e Q4
  };

  // Atualizar tempo
  useEffect(() => {
    if (isRunning && !isPause) {
      intervalRef.current = setInterval(() => {
        setTempoRestante(prev => {
          if (prev <= 1) {
            clearInterval(intervalRef.current);
            if (quartoAtual < 4) {
              setIsPause(true);
              setPausaRestante(temposDePausa[quartoAtual] || 0);
            } else {
              setIsRunning(false);
              // Em vez de alert, busca resultado final atualizado
              fetchResultadoFinal();
            }
            return 0;
          }
          return prev - 1;
        });
      }, 1000);
    }
    return () => clearInterval(intervalRef.current);
  }, [isRunning, isPause, quartoAtual]);

  // Contagem da pausa
  useEffect(() => {
    if (isPause && pausaRestante > 0) {
      const pausaTimer = setInterval(() => {
        setPausaRestante(prev => {
          if (prev <= 1) {
            clearInterval(pausaTimer);
            return 0;
          }
          return prev - 1;
        });
      }, 1000);
      return () => clearInterval(pausaTimer);
    }
  }, [isPause, pausaRestante]);

  // Atualiza pontos na API sempre que mudam
  useEffect(() => {
    if (!id) return;
  
    // Calcula o status do jogo
    let status = 'pendente'; // padrão
  
    if (isRunning) {
      status = 'a_decorrer';
    }
  
    // Quando o quarto 4 acaba e o tempo chega a 0, jogo terminou
    if (!isRunning && quartoAtual === 4 && tempoRestante === 0) {
      status = 'terminado';
    }
  
    fetch(`http://localhost:8000/api/jogos/${id}/`, {
      method: "PATCH",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        pontuacao_equipa_casa: pontosCasa,
        pontuacao_equipa_fora: pontosFora,
        status: status,  // envia o status atualizado
      }),
    })
    .then(res => {
      if (!res.ok) {
        console.error("Falha ao atualizar pontuação", res.status);
      }
    })
    .catch(err => {
      console.error("Erro ao atualizar pontuação:", err);
    });
  }, [pontosCasa, pontosFora, id, isRunning, quartoAtual, tempoRestante]);
  

  // Função para buscar o resultado final atualizado na API
  const fetchResultadoFinal = () => {
    fetch(`http://localhost:8000/api/jogos/${id}/`)
      .then(res => res.json())
      .then(data => {
        setResultadoFinal(data);  // Guarda resultado para mostrar na tela
      })
      .catch(err => {
        console.error("Erro a buscar resultado final:", err);
      });
  };

  const iniciarJogo = () => {
    setIsRunning(true);
    setIsPause(false);
  };

  const iniciarQuartoSeguinte = () => {
    if (quartoAtual < 4) {
      setQuartoAtual(prev => prev + 1);
      setTempoRestante(10); // para testes, 10s
      setIsRunning(true);
      setIsPause(false);
    }
  };

  return (
    <div className="text-center mt-5">
      <h2>Jogo #{id}</h2>

      {resultadoFinal ? (
        // Mostra resultado final no meio da tela
        <div style={{ fontSize: "2rem", fontWeight: "bold" }}>
          <p>Jogo Finalizado!</p>
          <p>
            {resultadoFinal.equipa_casa_nome} {resultadoFinal.pontuacao_equipa_casa} - {resultadoFinal.pontuacao_equipa_fora} {resultadoFinal.equipa_fora_nome}
          </p>
        </div>
      ) : (
        <>
          <h3>Quarto {quartoAtual}</h3>

          {isPause && pausaRestante > 0 ? (
            <div>
              <p>Pausa de {pausaRestante} segundos</p>
              <button className="btn btn-primary" onClick={iniciarQuartoSeguinte}>
                Iniciar Quarto {quartoAtual + 1}
              </button>
            </div>
          ) : (
            <>
              <h4>{Math.floor(tempoRestante / 60)}:{String(tempoRestante % 60).padStart(2, '0')}</h4>

              {!isRunning ? (
                <button className="btn btn-success" onClick={iniciarJogo}>
                  Iniciar Quarto
                </button>
              ) : (
                <div className="my-3">
                  <h5>Pontuação</h5>
                  <p>Casa: {pontosCasa} <button className="btn btn-outline-success btn-sm" onClick={() => setPontosCasa(p => p + 1)}>+1</button></p>
                  <p>Fora: {pontosFora} <button className="btn btn-outline-primary btn-sm" onClick={() => setPontosFora(p => p + 1)}>+1</button></p>
                </div>
              )}
            </>
          )}
        </>
      )}
    </div>
  );
}
