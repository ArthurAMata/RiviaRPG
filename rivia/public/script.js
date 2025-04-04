document.getElementById('personagemForm').addEventListener('submit', async function (e) {
    e.preventDefault();
  
    const nome = document.getElementById('nome').value;
    const raca = document.getElementById('raca').value;
    const classe = document.getElementById('classe').value;
  
    const response = await fetch('/api/personagem', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ nome, raca, classe })
    });
  
    if (response.ok) {
      window.location.href = 'game.html'; 
    } else {
      alert('Erro ao criar personagem');
    }
  });

  const opcoesRaca = ["Humano", "Elfo da floresta", "Elfo nobre", "Anão", "Dragonborn", "Orc", "Bruxo"];
  const opcoesClasse = ["Knigth", "Druida", "Mago de ataque", "Arqueiro", "Viking", "Bardo"];
  
  let indiceRaca = 0;
  let indiceClasse = 0;
  
  function trocarOpcao(tipo, direcao) {
    if (tipo === "raca") {
      indiceRaca = (indiceRaca + direcao + opcoesRaca.length) % opcoesRaca.length;
      document.getElementById("raca").textContent = opcoesRaca[indiceRaca];
    } else if (tipo === "classe") {
      indiceClasse = (indiceClasse + direcao + opcoesClasse.length) % opcoesClasse.length;
      document.getElementById("classe").textContent = opcoesClasse[indiceClasse];
    }
  
    atualizarSprite();
  }
  
  function atualizarSprite() {
    const raca = opcoesRaca[indiceRaca].toLowerCase().replace(/ /g, "_");
    const classe = opcoesClasse[indiceClasse].toLowerCase().replace(/ /g, "_");
  
    document.getElementById("spritePersonagem").src = `sprites/${raca}_${classe}.png`;
  }

  
