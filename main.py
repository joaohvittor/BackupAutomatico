import os
import datetime
import shutil


def verificar_ou_criar_pasta(caminho_pasta):
    if not os.path.exists(caminho_pasta):
        os.mkdir(caminho_pasta)
        print(f"Pasta criada em: {caminho_pasta}")
    else:
        print(f"Pasta já existe: {caminho_pasta}")


def gerar_nome_log():
    agora = datetime.datetime.now()
    data_formatada = agora.strftime("%Y-%m-%d-%H-%M-%S")
    nome_log = f"log_{data_formatada}.txt"
    print(f"Nome da log gerado: {nome_log}")
    return nome_log


def coletar_informacoes():
    usuario = os.environ.get("USER") or os.environ.get("USERNAME")
    diretorio_atual = os.getcwd()
    data_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    arquivos = os.listdir(diretorio_atual)

    conteudo = "===== LOG DE EXECUÇÃO =====\n"
    conteudo += f"Usuário: {usuario}\n"
    conteudo += f"Diretório de execução: {diretorio_atual}\n"
    conteudo += f"Data e hora: {data_hora}\n\n"
    conteudo += "Arquivos encontrados:\n"

    for arquivo in arquivos:
        conteudo += f"- {arquivo}\n"

    return conteudo


def criar_log(caminho_log, conteudo):
    with open(caminho_log, "w") as arquivo:
        arquivo.write(conteudo)
    print(f"Log salvo em: {caminho_log}")


def main():
    # Diretório onde o script está localizado
    diretorio_base = os.path.dirname(os.path.abspath(__file__))

    # Criando caminhos absolutos das pastas
    pasta_logs = os.path.join(diretorio_base, "logs")
    pasta_backup = os.path.join(diretorio_base, "backup")

    # Garantir que as pastas existam
    verificar_ou_criar_pasta(pasta_logs)
    verificar_ou_criar_pasta(pasta_backup)

    # Gerar nome do log
    nome_log = gerar_nome_log()

    # Caminhos completos do log e backup
    caminho_log = os.path.join(pasta_logs, nome_log)
    caminho_backup = os.path.join(pasta_backup, nome_log)

    # Coletar informações
    conteudo = coletar_informacoes()

    # Criar log
    criar_log(caminho_log, conteudo)

    # Criar backup
    shutil.copy(caminho_log, caminho_backup)
    print(f"Backup criado em: {caminho_backup}")


if __name__ == "__main__":
    main()