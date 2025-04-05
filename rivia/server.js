import express from 'express';
import sqlite3 from 'sqlite3';
import path from 'path';
import { fileURLToPath } from 'url';
import racasBuffs from './data/racasBuffs.js';
import equipamentosIniciais from './data/equipamentosIniciais.js';


// Configuração do caminho correto para ES Modules
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const app = express();
const PORT = 3000;

// Configuração do SQLite
const db = new sqlite3.Database('./db/database.sqlite', sqlite3.OPEN_READWRITE | sqlite3.OPEN_CREATE, (err) => {
  if (err) return console.error(err.message);
  console.log('Conectado ao SQLite');
});

// Criar tabela (se não existir)
db.run(`
  CREATE TABLE IF NOT EXISTS personagem (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    raca TEXT NOT NULL,
    classe TEXT NOT NULL,
    forca INTEGER DEFAULT 10,
    agilidade INTEGER DEFAULT 10,
    inteligencia INTEGER DEFAULT 10,
    buffs TEXT,
    inventario TEXT
  )
`);

// Middleware para servir arquivos estáticos
app.use(express.static('public'));
app.use(express.json());

// 🔹 **Criar Rota para Servir a Página Inicial**
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});



app.listen(PORT, () => {
  console.log(`Servidor rodando em http://localhost:${PORT}`);
});


app.post('/api/personagem', (req, res) => {
  const { nome, raca, classe } = req.body;

  const buffs = racasBuffs[raca] || {};
  const inventario = equipamentosIniciais[classe] || [];

  const forca = 10; //buff em arma física ex.espadas e machados
  const agilidade = 10; // buff em arcos
  const inteligencia = 10; //buff em cajados e magias

  const query = `
    INSERT INTO personagem (nome, raca, classe, forca, agilidade, inteligencia, buffs, inventario)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
  `;

  db.run(
    query,
    [
      nome,
      raca,
      classe,
      forca,
      agilidade,
      inteligencia,
      JSON.stringify(buffs),
      JSON.stringify(inventario)
    ],
    function (err) {
      if (err) {
        console.error(err.message);
        return res.status(500).json({ error: "Erro ao salvar personagem" });
      }

      res.status(201).json({ message: "Personagem criado", id: this.lastID });
    }
  );
});