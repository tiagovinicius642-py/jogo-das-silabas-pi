const frutas = [
    { emoji: "🍌", nome: "BANANA", status: "concluida" },
    { emoji: "🍓", nome: "MORANGO", status: "concluida" },
    { emoji: "🍒", nome: "CEREJA", status: "andamento" },
    { emoji: "🍇", nome: "UVA", status: "pendente" },
    { emoji: "🍊", nome: "LARANJA", status: "pendente" },
    { emoji: "🥑", nome: "ABACATE", status: "pendente" },
    { emoji: "🥭", nome: "MANGA", status: "pendente" },
    { emoji: "🍉", nome: "MELANCIA", status: "pendente" }
];

const lista = document.getElementById("listaFrutas");

// Mostrar as frutas na tela
function mostrarFrutas() {

    lista.innerHTML = "";

    frutas.forEach((fruta, index) => {

        const item = document.createElement("div");
        item.className = "fruta";

        let indicador = "";

        if (fruta.status === "concluida") {
            indicador = '<div class="status concluida">✓</div>';
        }

        else if (fruta.status === "andamento") {
            indicador = '<div class="status andamento"></div>';
        }

        else {
            indicador = '<div class="status pendente"></div>';
        }

        item.innerHTML = `
            <span class="emoji">${fruta.emoji}</span>
            <span class="nome">${fruta.nome}</span>
            ${indicador}
        `;

        lista.appendChild(item);

    });
}

// Alterar o progresso de uma fruta
function atualizarProgresso(nome, novoStatus) {

    const fruta = frutas.find(item => item.nome === nome);

    if (fruta) {
        fruta.status = novoStatus;
        mostrarFrutas();
    }
}

// Exibir a tela inicialmente
mostrarFrutas();