import database


def criar_time(dados):
    conexao = database.get_connection()
    cursor = conexao.cursor()

    cursor.execute(
        "INSERT INTO times (nome, cidade, ano_fundacao) VALUES (?, ?, ?)",
        (dados["nome"], dados["cidade"], dados["ano_fundacao"]),
    )

    conexao.commit()
    novo_id = cursor.lastrowid
    conexao.close()

    return buscar_time(novo_id)


def listar_times():
    conexao = database.get_connection()
    linhas = conexao.execute("SELECT * FROM times").fetchall()
    conexao.close()

    return [dict(linha) for linha in linhas]


def buscar_time(time_id):
    conexao = database.get_connection()
    linha = conexao.execute("SELECT * FROM times WHERE id = ?", (time_id,)).fetchone()
    conexao.close()

    return dict(linha) if linha else None


def atualizar_time(time_id, dados):
    conexao = database.get_connection()
    conexao.execute(
        "UPDATE times SET nome = ?, cidade = ?, ano_fundacao = ? WHERE id = ?",
        (dados["nome"], dados["cidade"], dados["ano_fundacao"], time_id),
    )
    conexao.commit()
    conexao.close()

    return buscar_time(time_id)


def tem_jogadores(time_id):
    conexao = database.get_connection()
    total = conexao.execute(
        "SELECT COUNT(*) FROM jogadores WHERE time_id = ?", (time_id,)
    ).fetchone()[0]
    conexao.close()

    return total > 0


def excluir_time(time_id):
    conexao = database.get_connection()
    conexao.execute("DELETE FROM times WHERE id = ?", (time_id,))
    conexao.commit()
    conexao.close()
