from flask import Flask, render_template, request, jsonify, session
import random
import model
import os

flask = Flask(__name__)
# Em produção, use uma variável de ambiente; para testes locais, pode usar uma string fixa
#flask.secret_key = os.environ.get("SECRET_KEY", "uma-chave-secreta-fixa-para-dev")
flask.config['SECRET_KEY'] = os.environ['SECRET_KEY']

@flask.before_request
def inicializar_progresso():
  if "progresso" not in session:
    session["progresso"] = {
        "frutas": 0,
        "animais": 0,
        "cores": 0,
        "universo": 0,
    }

def escolher_palavra_específica(palavra, cor):
    var_frutas = 644
    id_nicho = 1


    palavra_escolhida = palavra

    silabas_escolhidas = palavra_escolhida.split("&")

    cor_escolhida = cor

    silabas_escolhidas_finais = [(silaba, cor_escolhida,  ) for silaba in silabas_escolhidas]


    return silabas_escolhidas_finais



#def pegar_lista

@flask.route('/')
def home():
    return render_template('home.html')

@flask.route('/temas')
def temas():
    return render_template('temas.html')

@flask.route('/puzzle_completo', methods=['POST'])
def puzzle_completo():

    data = request.get_json()

    if not data:
        return jsonify({
            "success": False,
            "message": "Nenhum dado recebido"
        }), 400

    puzzle = int(data.get('puzzle', 0))
    nicho = int(data.get('nicho', 0))

    session['puzzle'] = puzzle
    session['ultimo_nicho'] = nicho

    mapa = {
        1: 'frutas',
        2: 'animais',
        3: 'cores',
        4: 'universo'
    }

    session['progresso'][mapa[nicho]] += 1
    session.modified = True

    return jsonify({
        "success": True
    }), 200

@flask.route('/acerto')
def tela_acerto():

    id_nicho = session.get('ultimo_nicho', 1)

    return render_template(
        'acerto.html',
        id_nicho=id_nicho
    )


@flask.route('/nicho/<string:num>')
def mostrar_nicho(num):

    var = 0
    id_palavra = 0

    if num == '1':
        var = 644
        id_palavra = session['progresso']['frutas']

    elif num == '2':
        var = 669
        id_palavra = session['progresso']['animais']

    elif num == '3':
        var = 694
        id_palavra = session['progresso']['cores']

    elif num == '4':
        var = 719
        id_palavra = session['progresso']['universo']

    id_nicho = int(num)

    palavra = model.pegar_palavra_por_id(
        id_nicho,
        var,
        id_palavra
    )[0]

    var_palavra = palavra['palavra']
    var_palavra2 = palavra['palavra'].lower()
    var_imagem = palavra['img']
    var_cor = palavra['cor']

    silabas_específicas = []

    for silaba in palavra['silaba'].split('&'):
        silabas_específicas.append(
            (silaba, palavra['cor'])
        )

    todas_palavras = model.pegar_palavras_nicho(id_nicho)

    silabas_aleatórias = []

    for item in todas_palavras:

        if item['id_palavra'] != palavra['id_palavra']:

            for silaba in item['silaba'].split('&'):

                silabas_aleatórias.append(
                    (silaba, item['cor'])
                )

    while len(silabas_aleatórias) + len(silabas_específicas) > 9:

        silabas_aleatórias.pop(
            random.randrange(len(silabas_aleatórias))
        )

    silabas = silabas_aleatórias + silabas_específicas

    random.shuffle(silabas)

    puzzle_id = palavra['id_palavra']

    return render_template(
        'level.html',
        silabas=silabas,
        silabas_específicas=silabas_específicas,
        var_imagem=var_imagem,
        var_palavra=var_palavra,
        var_palavra2=var_palavra2,
        var_cor=var_cor,
        puzzle_id=puzzle_id,
        id_nicho=id_nicho
    )

@flask.route('/progresso')
def progresso():
    return render_template('progresso.html')

@flask.route('/principal')
def principal():
    return render_template('principal.html')

# def run():
#     flask.run(debug=True)

# run()

def run():
    port = int(os.environ.get("PORT", 10000))
    flask.run(host="0.0.0.0", port=port, debug=False)

if __name__ == "__main__":
    run()
