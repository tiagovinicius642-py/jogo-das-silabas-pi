let silabaArrastada = null;
let copiaArraste = null;

function ativarArraste() {

    const silabas = document.querySelectorAll(".silaba");

    silabas.forEach(silaba => {

        if (silaba.dataset.arrasteAtivado) return;

        silaba.dataset.arrasteAtivado = "true";

        silaba.addEventListener("pointerdown", iniciarArraste);

    });
}
function iniciarArraste(evento) {

    evento.preventDefault();

    silabaArrastada = evento.currentTarget;

    if (silabaArrastada.classList.contains("usada")) {
        silabaArrastada = null;
        return;
    }

    copiaArraste = silabaArrastada.cloneNode(true);

    copiaArraste.classList.add("flutuante");

    copiaArraste.style.width =
        silabaArrastada.offsetWidth + "px";

    copiaArraste.style.height =
        silabaArrastada.offsetHeight + "px";

    document.body.appendChild(copiaArraste);

    silabaArrastada.classList.add("arrastando");

    moverCopia(evento);

    document.addEventListener("pointermove", moverCopia);
    document.addEventListener("pointerup", finalizarArraste);
}

function moverCopia(evento) {

    if (!copiaArraste) return;

    copiaArraste.style.left = evento.clientX + "px";
    copiaArraste.style.top = evento.clientY + "px";
}

function finalizarArraste(evento) {

    if (!silabaArrastada || !copiaArraste) return;

    copiaArraste.remove();

    silabaArrastada.classList.remove("arrastando");

    document.removeEventListener("pointermove", moverCopia);
    document.removeEventListener("pointerup", finalizarArraste);

    const elemento = document.elementFromPoint(
        evento.clientX,
        evento.clientY
    );

    const espaco = elemento?.closest(".espaco");

    if (espaco && !espaco.classList.contains("preenchido")) {

        espaco.textContent = silabaArrastada.textContent;

        espaco.style.backgroundColor =
            getComputedStyle(silabaArrastada).backgroundColor;

        espaco.classList.add("preenchido");

        silabaArrastada.classList.add("usada");
    }

    silabaArrastada = null;
    copiaArraste = null;
}
const observador = new MutationObserver(() => {
    ativarArraste();
});

observador.observe(
    document.getElementById("painelSilabas"),
    {
        childList: true
    }
);