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
    status TEXT DEFAULT 'active'
  )`);
});

module.exports = {
  getOrCreateUser(cid){return new Promise((res,rej)=>db.get('SELECT * FROM users WHERE chat_id=?',[cid],(e,r)=>{if(r)return res(r);db.run('INSERT INTO users (chat_id,created_at) VALUES (?,?)',[cid,new Date().toISOString()],(er)=>{er?rej(er):res({chat_id:cid,balance:0});});}));},
  getUser(cid){return new Promise((res,rej)=>db.get('SELECT * FROM users WHERE chat_id=?',[cid],(e,r)=>r?res(r):rej(e||'nf')));},
  addBalance(cid,a){return new Promise((res,rej)=>db.run('UPDATE users SET balance=balance+? WHERE chat_id=?',[a,cid],e=>e?rej(e):res()));},
  setBalance(cid,a){return new Promise((res,rej)=>db.run('UPDATE users SET balance=? WHERE chat_id=?',[a,cid],e=>e?rej(e):res()));},
  getKeys(cid){return new Promise((res,rej)=>db.all('SELECT * FROM keys WHERE chat_id=? ORDER BY id',[cid],(e,r)=>e?rej(e):res(r)));},
  addKey(cid,name,url,exp){return new Promise((res,rej)=>db.run('INSERT INTO keys (chat_id,name,url,expires,status) VALUES (?,?,?,?,?)',[cid,name,url,exp,'active'],function(e){e?rej(e):res(this.lastID);}));},
  allUsers(){return new Promise((res,rej)=>db.all('SELECT * FROM users',(e,r)=>e?rej(e):res(r)));}
};
