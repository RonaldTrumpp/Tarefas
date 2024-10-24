import sqlite3

def conectar():
    conn = sqlite3.connect('tarefas.db')
    return conn

def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            descricao TEXT NOT NULL,
            status TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def adicionar_tarefa(descricao):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO tarefas (descricao, status) VALUES (?, ?)', (descricao, 'pendente'))
    conn.commit()
    conn.close()

def listar_tarefas():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tarefas')
    tarefas = cursor.fetchall()
    conn.close()
    return tarefas

def editar_tarefa(id, nova_descricao):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('UPDATE tarefas SET descricao = ? WHERE id = ?', (nova_descricao, id))
    conn.commit()
    conn.close()

def excluir_tarefa(id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM tarefas WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    
