import os
import subprocess
import psycopg2
import psycopg2.extras
from psycopg2 import sql

HOST = "localhost"
PORT = "5432"
DB_NAME = "jogo_das_silabas"
USER = "postgres"
PASSWORD = "postgres"

# Conexão com o banco
def get_conn():
    return psycopg2.connect(
        host=HOST,
        port=PORT,
        dbname=DB_NAME,
        user=USER,
        password=PASSWORD
    )

def comando(comando):
    conn = get_conn()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    cur.execute(comando)

    resultado = cur.fetchall()

    cur.close()
    conn.close()

    return resultado

def pegar_palavras_nicho(id_nicho):
    return comando(f"SELECT * FROM palavras where id_nicho = {id_nicho}")

def pegar_palavra_por_id(id_nicho, var_index, var_id_palavra):
    return comando(f"SELECT * FROM palavras where id_nicho = {id_nicho} and id_palavra = {var_index + var_id_palavra};")

#print(pegar_palavras_nicho(2))












# Opção 2: restaurar o sql
def restaurar_backup(arquivo="conecta_facil_bck.sql"):

    if not os.path.exists(arquivo):
        print(f"Arquivo '{arquivo}' não encontrado.")
        return

    subprocess.run(
        [
            "psql",
            "-h", HOST,
            "-p", PORT,
            "-U", USER,
            "-d", DB_NAME,
            "-f", arquivo
        ],
        env={**os.environ, "PGPASSWORD": PASSWORD},
        check=True
    )

    print("Backup restaurado com sucesso.")

# CRUD
def DDDs():
    conn = get_conn()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    cur.execute("SELECT * FROM ddds;")

    resultado = cur.fetchall()

    cur.close()
    conn.close()

    return resultado

def buscar_usuário(username, password):
    conn = get_conn()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    cur.execute(f"SELECT * FROM usuario WHERE username = '{username}' AND password = '{password}';")

    resultado = cur.fetchall()

    cur.close()
    conn.close()

    if len(resultado) > 0:
        return resultado[0]['id']
    else:
        return 0
        
def contatos(id):
    conn = get_conn()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    cur.execute(f"SELECT * FROM contatos WHERE user_id={id};")

    resultado = cur.fetchall()

    cur.execute(f"SELECT * FROM contatos WHERE user_id={id};")


    #cur.execute(f"SELECT * FROM ddds WHERE id={resultado};")

    cur.close()
    conn.close()

    return resultado

def cadastrar(password, username, telefone, ddd_us):
    conn = get_conn()
    cur = conn.cursor()

    cur.execute(
        f"INSERT INTO usuario (password, username, telefone, ddd_us) VALUES ('{password}','{username}',{telefone},{ddd_us});"
    )

    conn.commit()
    cur.close()
    conn.close()

def pegar_contato(id, session_id):
    conn = get_conn()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    cur.execute(
        f"SELECT * FROM contatos WHERE id={id} AND user_id = {session_id};"
    )

    contato = cur.fetchone()

    cur.close()
    conn.close()

    return contato

def ver_num(session_id, ddd, telefone):
    conn = get_conn()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    cur.execute(f"SELECT * FROM contatos WHERE user_id={session_id} AND telefone='{telefone}' AND ddd='{ddd}';")

    resultado = cur.fetchall()

    cur.close()
    conn.close()

    if len(resultado) <= 0:
        return "ok"
    elif len(resultado) > 0:
        return "Erro!"

def excluir(id, session_id):
    conn = get_conn()
    cur = conn.cursor()

    cur.execute(
        f"DELETE FROM contatos WHERE id = {id} and user_id = {session_id}"
    )

    conn.commit()
    cur.close()
    conn.close()

def adicionar_contato(user_id, ddd, telefone, ctt_name):
    conn = get_conn()
    cur = conn.cursor()

    cur.execute(
        f"INSERT INTO contatos (user_id, ddd, telefone, ctt_name) VALUES ({user_id}, {ddd}, {telefone}, '{ctt_name}')"
    )

    conn.commit()
    cur.close()
    conn.close()

def editar_contato(id, user_id, ddd, telefone, nome):
    conn = get_conn()
    cur = conn.cursor()

    cur.execute(
        f"""
        UPDATE contatos
        SET ddd = {ddd}, telefone = {telefone}, ctt_name = '{nome}'
        WHERE id = {id} AND user_id = {user_id};
        """
    )

    conn.commit()
    cur.close()
    conn.close()

def atualizar(id, titulo, autor):
    conn = get_conn()
    cur = conn.cursor()

    cur.execute(
        "UPDATE livro SET titulo = , autor =  WHERE id = ",
        (titulo, autor, id)
    )

    conn.commit()
    cur.close()
    conn.close()




#buscar_usuário("Hirohito","senha1")
#contatos(2)
#cadastrar("senha67", "Jeffrey Epstein", 666666666, 11)