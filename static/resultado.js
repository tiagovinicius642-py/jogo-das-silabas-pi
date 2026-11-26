
(() => {
    const params = new URLSearchParams(window.location.search);

    const status = document.querySelector('.tela')?.dataset.status;

    const imagem = params.get('imagem') || localStorage.getItem('imagemAtual') || '';
    const palavra = params.get('palavra') || localStorage.getItem('palavraAtual') || '';
    const proxima = params.get('proxima') || localStorage.getItem('proximaPagina') || 'jogo.html';
    const paginaJogo = params.get('jogo') || localStorage.getItem('paginaJogo') || 'jogo.html';

    const img = document.getElementById('imagem-palavra');
    const fallback = document.getElementById('imagem-fallback');

    if (imagem && img) {
        img.src = imagem;
        img.hidden = false;

        if (fallback) fallback.hidden = true;

        img.addEventListener('error', () => {
            img.hidden = true;
            if (fallback) fallback.hidden = false;
        });
    }

    const nome = document.getElementById('nomeElemento');

    if (palavra && nome) {
        nome.textContent = palavra.trim().toLocaleUpperCase('pt-BR');
        nome.hidden = false;
    }

    if (status === 'acerto') {
        const areaConfetes = document.getElementById('confetes');

    const coresExplosao = ['#ffd400', '#1598ff', '#ff1744', '#08c95b'];

for (let i = 0; i < 65; i++) {
    const particula = document.createElement('span');

    const angulo = Math.random() * Math.PI * 2;
    const distancia = 90 + Math.random() * 190;

    const x = Math.cos(angulo) * distancia;
    const y = Math.sin(angulo) * distancia;

    particula.classList.add('explosao-confete');

    particula.style.backgroundColor =
        coresExplosao[Math.floor(Math.random() * coresExplosao.length)];

    particula.style.setProperty('--x', `${x}px`);
    particula.style.setProperty('--y', `${y}px`);
    particula.style.setProperty('--rotacao', `${Math.random() * 720}deg`);

    areaConfetes.appendChild(particula);

    particula.addEventListener('animationend', () => {
        particula.remove();
    });
}

        if (areaConfetes) {
            const cores = ['amarelo', 'azul', 'vermelho', 'verde'];
            const quantidade = 40;

            for (let i = 0; i < quantidade; i++) {
                const confete = document.createElement('span');

                const cor = cores[Math.floor(Math.random() * cores.length)];
                const duracao = 3 + Math.random() * 4;
                const atraso = Math.random() * 5;
                const tamanho = 6 + Math.random() * 7;
                const deslocamento = (Math.random() - 0.5) * 100;

                confete.classList.add('confete', `confete--${cor}`);

                confete.style.setProperty('--posicao', `${Math.random() * 100}%`);
                confete.style.setProperty('--duracao', `${duracao}s`);
                confete.style.setProperty('--atraso', `${atraso}s`);
                confete.style.setProperty('--tamanho', `${tamanho}px`);
                confete.style.setProperty('--deslocamento', `${deslocamento}px`);

                areaConfetes.appendChild(confete);
            }
        }
    }

    document.getElementById('botao-proxima')?.addEventListener('click', () => {
        window.location.href = proxima;
    });

    document.getElementById('botao-tentar')?.addEventListener('click', () => {
        window.location.href = paginaJogo;
    });

})();
