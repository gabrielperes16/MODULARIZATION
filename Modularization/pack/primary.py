import Module
def main():
    arq = 'Test_Arquivo.txt'
    if not Module.arq_existe(arq):
        Module.criarArquivo(arq)

    people = Module.carregar_arquivo(arq)
if __name__ == "__main__":
    main()
