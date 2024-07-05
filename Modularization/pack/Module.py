def decoration(msg):
    print("\033[32m==\033[m" * 30)
    print(msg)
    print("\033[32m==\033[m" * 30)

def validator(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value in [1, 2, 3]:
                return value
            else:
                print("Invalid choice. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def menu():
    print("\033[32m==" * 30)
    print('''                1- View registered people
                2- Register new person
                3- Exit the system\033[m'''.center(100))
    print("\033[32m==\033[m" * 30)

def view_registered_people(people):
    if not people:
        print("No people registered yet.")
    else:
        print('\033[32m=='*50)
        print("THE LIST OF REGISTERED PEOPLE IS:".center(94))
        print('=='*50)
        for person in people:
            print(f"\033[1;36mNAME: {person['name']}")
            print(f"AGE: {person['age']}")
            print(f"GENDER: {person['gender']}\033[m\033[32m")
            print('=='*50)
    print("\033[m")

def register_new_person(people):
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    while True:
        gender = input("Enter your gender [MALE] or [FEMALE]: ").upper().strip()
        if gender in ['MALE', 'FEMALE']:
            break
        else:
            print("Error: enter correctly!")

    person = {
        'name': name,
        'age': age,
        'gender': gender
    }
    people.append(person)
    print("Data successfully recorded:", person)

def arq_existe(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print("ERRO! na criação do arquivo")
    else:
        print(f"Arquivo {nome} criado com sucesso")

def salvar_arquivo(nome, people):
    try:
        with open(nome, 'wt') as f:
            for person in people:
                f.write(f"{person['name']},{person['age']},{person['gender']}\n")
    except:
        print("ERRO! ao salvar os dados no arquivo")

def carregar_arquivo(nome):
    people = []
    try:
        with open(nome, 'rt') as f:
            for line in f:
                name, age, gender = line.strip().split(',')
                people.append({'name': name, 'age': int(age), 'gender': gender})
    except:
        print("ERRO! ao carregar os dados do arquivo")
    return people

# Programa principal
arq = 'Test_Arquivo.txt'
if not arq_existe(arq):
    criarArquivo(arq)

people = carregar_arquivo(arq)

while True:
    menu()
    choice = validator("Your Choice: ")

    if choice == 1:
        view_registered_people(people)

    elif choice == 2:
        register_new_person(people)

    elif choice == 3:
        print("\033[32mEND OF PROGRAM. SEE YOU LATER!\033[m")
        print("\033[32m==" * 30)
        salvar_arquivo(arq, people)
        break
def lerArquivo(nome):
    try:
        a=open(nome,'rt')
    except:
        print("Erro ao ler o arquivo!")
    else:
        choice('Pessoas Cadastradas')
        print(a.readlines())