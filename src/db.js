const sqlite3 = require('sqlite3').verbose();
const path = require('path');

const db = new sqlite3.Database(path.join(__dirname, '../bot.db'));

db.serialize(() => {
  db.run(`CREATE TABLE IF NOT EXISTS users (
    chat_id INTEGER PRIMARY KEY,
    balance INTEGER DEFAULT 0,
    created_at TEXT
  )`);
  db.run(`CREATE TABLE IF NOT EXISTS keys (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    chat_id INTEGER,
    name TEXT,
    url TEXT,
    expires INTEGER,
    status TEXT DEFAULT 'active',
    created_at TEXT
  )`);
  db.run(`CREATE TABLE IF NOT EXISTS payments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    chat_id INTEGER,
    amount INTEGER,
    months INTEGER,
    status TEXT DEFAULT 'pending',
    created_at TEXT
  )`);
});

module.exports = {
  getOrCreateUser(chatId) {
    return new Promise((resolve, reject) => {
      db.get('SELECT * FROM users WHERE chat_id=?', [chatId], (e, row) => {
        if (row) return resolve(row);
        db.run('INSERT INTO users (chat_id, balance, created_at) VALUES (?,?,?)',
          [chatId, 0, new Date().toISOString()], (err) => {
            if (err) return reject(err);
            resolve({ chat_id: chatId, balance: 0 });
          });
      });
    });
  },
  getUser(chatId) {
    return new Promise((res, rej) => db.get('SELECT * FROM users WHERE chat_id=?', [chatId], (e,r)=> r?res(r):rej(e||'not found')));
  },
  addBalance(chatId, amt) {
    return new Promise((res, rej) => db.run('UPDATE users SET balance=balance+? WHERE chat_id=?', [amt, chatId], e=>e?rej(e):res()));
  },
  setBalance(chatId, amt) {
    return new Promise((res, rej) => db.run('UPDATE users SET balance=? WHERE chat_id=?', [amt, chatId], e=>e?rej(e):res()));
  },
  getKeys(chatId) {
    return new Promise((res, rej) => db.all('SELECT * FROM keys WHERE chat_id=? ORDER BY id', [chatId], (e,r)=>e?rej(e):res(r)));
  },
  addKey(chatId, name, url, expires) {
    return new Promise((res, rej) => db.run('INSERT INTO keys (chat_id,name,url,expires,status,created_at) VALUES (?,?,?,?,?,?)',
      [chatId,name,url,expires,'active',new Date().toISOString()], function(e){e?rej(e):res(this.lastID);}));
  },
  setKeyStatus(id, status) {
    return new Promise((res, rej) => db.run('UPDATE keys SET status=? WHERE id=?', [status,id], e=>e?rej(e):res()));
  },
  allUsers() {
    return new Promise((res, rej) => db.all('SELECT * FROM users', (e,r)=>e?rej(e):res(r)));
  },
  addPayment(chatId, amount, months) {
    return new Promise((res, rej) => db.run('INSERT INTO payments (chat_id,amount,months,status,created_at) VALUES (?,?,?,?,?)',
      [chatId,amount,months,'pending',new Date().toISOString()], function(e){e?rej(e):res(this.lastID);}));
  }
};
