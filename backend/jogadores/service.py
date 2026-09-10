import database

SELECT_JOGADOR = """
    SELECT j.id, j.nome, j.posicao, j.idade, j.time_id, t.nome AS time_nome
    FROM jogadores j
    JOIN times t ON t.id = j.time_id
"""


def criar_jogador(dados):
    conexao = database.get_connection()
    cursor = conexao.cursor()

    cursor.execute(
        "INSERT INTO jogadores (nome, posicao, idade, time_id) VALUES (?, ?, ?, ?)",
        (dados["nome"], dados["posicao"], dados["idade"], dados["time_id"]),
    )

    conexao.commit()
    novo_id = cursor.lastrowid
    conexao.close()

    return buscar_jogador(novo_id)


def listar_jogadores():
    conexao = database.get_connection()
    linhas = conexao.execute(SELECT_JOGADOR).fetchall()
    conexao.close()

    return [dict(linha) for linha in linhas]


def buscar_jogador(jogador_id):
    conexao = database.get_connection()
    linha = conexao.execute(
        SELECT_JOGADOR + " WHERE j.id = ?", (jogador_id,)
    ).fetchone()
    conexao.close()

    return dict(linha) if linha else None


def atualizar_jogador(jogador_id, dados):
    conexao = database.get_connection()
    conexao.execute(
        "UPDATE jogadores SET nome = ?, posicao = ?, idade = ?, time_id = ? WHERE id = ?",
        (
            dados["nome"],
            dados["posicao"],
            dados["idade"],
            dados["time_id"],
            jogador_id,
        ),
    )
    conexao.commit()
    conexao.close()

    return buscar_jogador(jogador_id)


def excluir_jogador(jogador_id):
    conexao = database.get_connection()
    conexao.execute("DELETE FROM jogadores WHERE id = ?", (jogador_id,))
    conexao.commit()
    conexao.close()
