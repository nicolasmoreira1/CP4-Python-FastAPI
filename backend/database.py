import sqlite3


def get_connection():
    conexao = sqlite3.connect("dados.db")
    conexao.execute("PRAGMA foreign_keys = ON")
    conexao.row_factory = sqlite3.Row
    return conexao


def criar_tabelas():
    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS times (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cidade TEXT NOT NULL,
            ano_fundacao INTEGER
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS jogadores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            posicao TEXT NOT NULL,
            idade INTEGER,
            time_id INTEGER NOT NULL,
            FOREIGN KEY (time_id) REFERENCES times (id)
        )
    """)

    conexao.commit()
    conexao.close()
