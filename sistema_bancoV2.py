def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques, nome_usuario):
    if valor <= 0:

        return saldo, extrato, """
===== Valor de saque inválido. Informe uma valor valido ===== 
=====    O valor deve ser positivo e maior que zero     =====
"""
    if numero_saques >= limite_saques:
        return saldo, extrato, "\n===== Limite de saques excedido ====="
    
    if saldo >= valor and valor <= limite:
        saldo -= valor
        extrato.append(f"{nome_usuario}: Saque:    - R$ {valor:.2f}")
        numero_saques += 1
        return saldo, extrato, None
    
    elif saldo < valor:
        return saldo, extrato, "\n===== Saldo insuficiente ====="
    
    else:
        return saldo, extrato, "\n===== Valor de saque excedeu o limite ====="

def deposito(saldo, valor, extrato, nome_usuario, /):
    if valor <= 0:    

        print("""
===== Valor de deposito inválido. Informe uma valor valido ===== 
=====    O valor deve ser positivo e maior que zero     =====
""")
        return saldo, extrato
    saldo += valor
    extrato.append(f"{nome_usuario}: Depósito: + R$ {valor:.2f}")
    print("\n===== Depósito realizado com sucesso! =====")
    return saldo, extrato

usuarios = []

def criar_usuario(nome, data_nascimento, cpf, endereco):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            print("\n===== Usuário já cadastrado com esse CPF =====")
            return
    usuarios.append({"nome": nome,
                     "data_nascimento": data_nascimento,
                     "cpf": cpf,
                     "endereco": endereco})
    
    print("\n===== Usuário criado com sucesso! =====")
    
contas = []
numero_conta = 1

def criar_conta(usuario):
    global numero_conta

    conta = {"agencia": "0001",
             "numero_conta": numero_conta,
             "usuario": usuario, "saldo": 0,
             "extrato": []
             }
    
    contas.append(conta)
    numero_conta += 1
    print("\n===== Conta criada com sucesso! =====") 
    print(f"Conta Nº {conta['numero_conta']} - Usuário: {usuario}")

def exibir_extrato(extrato, /, *, saldo):
    print("\n================ EXTRATO ================")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        for transacao in extrato:
            print(transacao)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def main():
    saldo = 0
    limite = 500
    extrato = []
    numero_saques = 0
    LIMITE_SAQUES = 3
    nome_usuario = ""

    while True:
        menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[nc] Nova Conta
[nu] Novo Usuário
[q] Sair
=> """
        opcao = input(menu)

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: R$ "))
            saldo, extrato = deposito(saldo, valor, extrato, nome_usuario)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: R$ "))
            saldo, extrato, msg = saque(
                
                saldo = saldo,
                valor = valor,
                extrato = extrato,
                limite = limite,
                numero_saques = numero_saques,
                limite_saques = LIMITE_SAQUES,
                nome_usuario = nome_usuario
            )
            if msg:
                print(msg)
            else:
                num = 3
                numero_saques += 1 
                print(f"""
===== Saque realizado com sucesso! =====
===== Saldo em conta: R$ {saldo:.2f}    =====
===== Saques restantes: {num - numero_saques}          =====
""")              
        elif opcao == "nc":
            if len(usuarios) == 0:
                print("===== Antes de criar uma conta, é necessário cadastrar um usuário =====")
            else:
                cpf = input("Informe o CPF do usuário para associar à nova conta: ")
                usuario_encontrado = False
                for usuario in usuarios:
                    if usuario["cpf"] == cpf:
                        criar_conta(nome_usuario)
                        usuario_encontrado = True
                        break
                if not usuario_encontrado:
                    print("\n===== Usuário não encontrado com o CPF informado =====")

        elif opcao == "nu":
            cpf = input("Informe o CPF do usuário (somente o número): ")
            for usuario in usuarios:
                if usuario["cpf"] == cpf:
                    print("\n===== Usuário já cadastrado com esse CPF =====")
                    break
            else:  # Se não houver usuário com o mesmo CPF
                nome_usuario = input("Informe o nome do usuário: ")
                data_nascimento = input("Data de nascimento (DD/MM/AAAA): ")
                endereco = input("Informe o endereço (Conjunto - Nº, Bairro, Cidade-UF): ")
                criar_usuario(nome_usuario, data_nascimento, cpf, endereco)

        elif opcao == "e":
            exibir_extrato(extrato, saldo = saldo)

        elif opcao == "q":
            print("\n===== Obrigado por utilizar nosso banco =====")
            break

        else:
            print("\n===== Operação inválida, por favor selecione novamente a operação desejada =====")

if __name__ == "__main__":
    main()
