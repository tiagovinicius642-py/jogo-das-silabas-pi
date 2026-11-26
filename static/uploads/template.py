from flask import Flask, render_template, request, jsonify
import random

flask = Flask(__name__)

palavras = [
        #"O&to&rri&no&la&rin&go&lo&gis&ta",
        #"Car&dio&lo&gis&ta",
        #"Der&ma&to&lo&gis&ta",
        #"Neu&ro&lo&gis&ta",
        #"Pe&di&a&tra",
        "Ba&na&na",
        "Goi&a&ba",
        "A&ba&po&ru",
        "Re&nan&play",
        "C&thu&lhu",
        "Sho&ggoth"
    ]

colors = [
    "#FF0000","#00FF00","#0000FF","#FFFF00","#00FFFF",
    "#FF00FF","#FFA500","#800080","#FFC0CB","#A52A2A",
    "#808080","#FFFFFF","#008000","#000080",
    "#800000","#008080","#C0C0C0","#FFD700","#4B0082",
]

# ==================================================================================================
# Funções
# ==================================================================================================

# A palavra escolhida

def escolher_palavra_específica(palavra, cor):

    palavra_escolhida = palavra

    silabas_escolhidas = palavra_escolhida.split("&")

    cor_escolhida = cor

    silabas_escolhidas_finais = [(silaba, cor_escolhida,  ) for silaba in silabas_escolhidas]


    return silabas_escolhidas_finais


def escolher_palavras_aleatórias(lista_palavras, palavra_escolhida, cor_escolhida):
    list = []

    for palavra in lista_palavras:
        if palavra != palavra_escolhida:
            #list.extend(escolher_palavra_específica(i, random.choice(colors)))
            cor = random.choice([color for color in colors if color != cor_escolhida])

            for silaba in palavra.split('&'):
                list.append((silaba, cor))

    return list

    #print(f"\n\nLista das palavras aleatórias:\n\n{list}")


def printar(def1, def2):

    if not def2 or def2 == "":
        def2 = []

    print(f"\n\nLista da palavra escolhida:\n\n{def1}")
    print(f"\n\nLista das palavras escolhidas:\n\n{def2}")

# ==================================================================================================
# Rotas
# ================================================================================================== 

puzzle = 0

@flask.route('/puzzle_completo', methods=['POST'])
def puzzle_completo():
    global puzzle
    data = request.get_json()
    puzzle = int(data.get('puzzle', 0))
    if not data:
        return jsonify({"success": False, "message": "Nenhum dado recebido"}), 400
    
    return jsonify({"success": True, "message": "Requisição processada com sucesso"}), 200

@flask.route('/')
def index():
    global puzzle

    palavras = [
        "Ja&ya&ne",
        "Cla&ri&nha",
        "E&du&ar&da",
        "Ti&a&go"
    ]

    colors2 = [
        "#FFC0CB", "#FF4747","#FFC14D","#6AFF6A"
    ]

    #data = puzzle_completo()

    if int(puzzle) > 3:
        return render_template('sucesso.html')
    
    else:

        palavra_escolhida = palavras[int(puzzle)]

        cor_escolhida = colors2[int(puzzle)]

        var_imagem = f"static/images/{palavras[int(puzzle)].replace("&", "")}.png"

        var_palavra = palavra_escolhida.replace("&", "")

        puzzle_id = int(puzzle + 1)

        meter = f"{ '🟢' * int(puzzle)} {'🔘' * (4 - int(puzzle))}"

        silabas_específicas = escolher_palavra_específica(
            palavra_escolhida,
            cor_escolhida
        )

        silabas_aleatórias = escolher_palavras_aleatórias(
            palavras,
            palavra_escolhida,
            cor_escolhida
        )

        while len(silabas_aleatórias) + len(silabas_específicas) > 9:
            silabas_aleatórias.pop(
                random.randrange(len(silabas_aleatórias))
            )

        silabas = silabas_aleatórias + silabas_específicas

        random.shuffle(silabas)
                
        #while len(silabas) > 8:
                #silabas.remove(random.choice(silabas_aleatórias))

        random.shuffle(silabas)
        print(silabas)
        print(puzzle_id)

        return render_template(
            'index(meu).html',
            silabas=silabas,
            silabas_específicas=silabas_específicas,
            var_imagem=var_imagem,
            var_palavra=var_palavra,
            var_cor=cor_escolhida,
            puzzle_id=puzzle_id
        )

def run():
    flask.run(debug=True)

run()