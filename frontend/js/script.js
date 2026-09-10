const API = "http://localhost:8000";

const formTime = document.getElementById("form-time");
const formJogador = document.getElementById("form-jogador");


async function carregarTimes() {
    const resposta = await fetch(API + "/times");
    const times = await resposta.json();

    const tabela = document.getElementById("tabela-times");
    const select = document.getElementById("jogador-time");
    tabela.innerHTML = "";
    select.innerHTML = "";

    for (const time of times) {
        tabela.innerHTML += `
            <tr>
                <td>${time.id}</td>
                <td>${time.nome}</td>
                <td>${time.cidade}</td>
                <td>${time.ano_fundacao || "-"}</td>
                <td>
                    <button onclick="editarTime(${time.id})">Editar</button>
                    <button class="excluir" onclick="excluirTime(${time.id})">Excluir</button>
                </td>
            </tr>`;

        select.innerHTML += `<option value="${time.id}">${time.nome}</option>`;
    }
}

async function carregarJogadores() {
    const resposta = await fetch(API + "/jogadores");
    const jogadores = await resposta.json();

    const tabela = document.getElementById("tabela-jogadores");
    tabela.innerHTML = "";

    for (const jogador of jogadores) {
        tabela.innerHTML += `
            <tr>
                <td>${jogador.id}</td>
                <td>${jogador.nome}</td>
                <td>${jogador.posicao}</td>
                <td>${jogador.idade || "-"}</td>
                <td>${jogador.time_nome}</td>
                <td>
                    <button onclick="editarJogador(${jogador.id})">Editar</button>
                    <button class="excluir" onclick="excluirJogador(${jogador.id})">Excluir</button>
                </td>
            </tr>`;
    }
}


formTime.addEventListener("submit", async (evento) => {
    evento.preventDefault();

    const id = document.getElementById("time-id").value;
    const ano = document.getElementById("time-ano").value;

    const time = {
        nome: document.getElementById("time-nome").value,
        cidade: document.getElementById("time-cidade").value,
        ano_fundacao: ano ? Number(ano) : null,
    };

    const resposta = await fetch(id ? `${API}/times/${id}` : `${API}/times`, {
        method: id ? "PUT" : "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(time),
    });

    if (!resposta.ok) {
        const erro = await resposta.json();
        alert(erro.detail);
        return;
    }

    formTime.reset();
    document.getElementById("time-id").value = "";
    carregarTimes();
    carregarJogadores();
});

async function editarTime(id) {
    const resposta = await fetch(`${API}/times/${id}`);
    const time = await resposta.json();

    document.getElementById("time-id").value = time.id;
    document.getElementById("time-nome").value = time.nome;
    document.getElementById("time-cidade").value = time.cidade;
    document.getElementById("time-ano").value = time.ano_fundacao || "";
}

async function excluirTime(id) {
    if (!confirm("Excluir este time?")) return;

    const resposta = await fetch(`${API}/times/${id}`, { method: "DELETE" });

    if (!resposta.ok) {
        const erro = await resposta.json();
        alert(erro.detail);
        return;
    }

    carregarTimes();
}


formJogador.addEventListener("submit", async (evento) => {
    evento.preventDefault();

    const id = document.getElementById("jogador-id").value;
    const idade = document.getElementById("jogador-idade").value;

    const jogador = {
        nome: document.getElementById("jogador-nome").value,
        posicao: document.getElementById("jogador-posicao").value,
        idade: idade ? Number(idade) : null,
        time_id: Number(document.getElementById("jogador-time").value),
    };

    const resposta = await fetch(id ? `${API}/jogadores/${id}` : `${API}/jogadores`, {
        method: id ? "PUT" : "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(jogador),
    });

    if (!resposta.ok) {
        const erro = await resposta.json();
        alert(erro.detail);
        return;
    }

    formJogador.reset();
    document.getElementById("jogador-id").value = "";
    carregarJogadores();
});

async function editarJogador(id) {
    const resposta = await fetch(`${API}/jogadores/${id}`);
    const jogador = await resposta.json();

    document.getElementById("jogador-id").value = jogador.id;
    document.getElementById("jogador-nome").value = jogador.nome;
    document.getElementById("jogador-posicao").value = jogador.posicao;
    document.getElementById("jogador-idade").value = jogador.idade || "";
    document.getElementById("jogador-time").value = jogador.time_id;
}

async function excluirJogador(id) {
    if (!confirm("Excluir este jogador?")) return;

    await fetch(`${API}/jogadores/${id}`, { method: "DELETE" });
    carregarJogadores();
}


carregarTimes();
carregarJogadores();
