# Atividade - Arvores Binarias
# Aluno: Arthur Vettorazzo de Souza

# 4. Estrutura do no
class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None


# Funcoes auxiliares para validar tokens
def eh_operador(token):
    return token in ('+', '-', '*', '/', '^')


def eh_numero(token):
    if not token or token in ('-', '.', '-.'):
        return False
    # se for negativo, tira o sinal da frente so para checar os digitos
    if token[0] == '-':
        token = token[1:]
    if token.count('.') > 1:
        return False
    limpo = token.replace('.', '')
    return limpo.isdigit() and len(limpo) > 0


# 5. Tokenizacao
def tokenizar(expressao):
    if expressao is None or expressao.strip() == "":
        raise ValueError("Expressao vazia.")

    tokens = []
    i = 0
    n = len(expressao)

    # controle do menos unario antes de parenteses: -(expr) vira (0 - (expr))
    profundidade = 0
    fechar_em = []          # profundidades que precisam de um ')' extra
    unario_pendente = False

    while i < n:
        char = expressao[i]

        # ignora espacos
        if char.isspace():
            i += 1
            continue

        # parenteses
        if char in ('(', ')'):
            if char == ')' and len(tokens) > 0 and tokens[-1] == '(':
                raise ValueError("Parenteses vazios nao sao validos.")
            tokens.append(char)
            if char == '(':
                profundidade += 1
                if unario_pendente:
                    fechar_em.append(profundidade)
                    unario_pendente = False
            else:
                # fecha tambem o parentese extra criado pelo menos unario
                if fechar_em and fechar_em[-1] == profundidade:
                    tokens.append(')')
                    fechar_em.pop()
                profundidade -= 1
            i += 1
            continue

        # trata sinal negativo unario (no comeco, depois de '(' ou depois de outro operador)
        if char == '-' and (len(tokens) == 0 or tokens[-1] == '(' or eh_operador(tokens[-1])):
            j = i + 1
            while j < n and expressao[j].isspace():
                j += 1

            if j >= n:
                raise ValueError("Sinal '-' solto no final da expressao.")

            # se vier numero logo depois, junta o '-' com o numero (ex: -5)
            if expressao[j].isdigit() or expressao[j] == '.':
                numero = '-'
                i = j
                pontos = 0
                while i < n and (expressao[i].isdigit() or expressao[i] == '.'):
                    if expressao[i] == '.':
                        pontos += 1
                        if pontos > 1:
                            raise ValueError("Numero decimal invalido.")
                    numero += expressao[i]
                    i += 1
                if not eh_numero(numero):
                    raise ValueError(f"Numero invalido: {numero}")
                tokens.append(numero)
                continue

            # se for -(expressao), transforma em (0 - (expressao))
            elif expressao[j] == '(':
                tokens.extend(['(', '0', '-'])
                unario_pendente = True
                i += 1
                continue

        # operadores normais (+, -, *, /, ^)
        if eh_operador(char):
            tokens.append(char)
            i += 1
            continue

        # numeros inteiros ou decimais
        if char.isdigit() or char == '.':
            numero = ''
            pontos = 0
            while i < n and (expressao[i].isdigit() or expressao[i] == '.'):
                if expressao[i] == '.':
                    pontos += 1
                    if pontos > 1:
                        raise ValueError("Numero decimal com mais de um ponto.")
                numero += expressao[i]
                i += 1

            if not eh_numero(numero):
                raise ValueError(f"Numero mal formatado: {numero}")

            tokens.append(numero)
            continue

        # qualquer outro caractere da erro
        raise ValueError(f"Caractere nao aceito: '{char}'")

    return tokens


# 6. Precedencia
def precedencia(operador):
    if operador == '^':
        return 3
    if operador in ('*', '/'):
        return 2
    if operador in ('+', '-'):
        return 1
    return 0


# 7. Converter infixa para pos-fixa
def para_posfixa(tokens):
    if not tokens:
        raise ValueError("Nenhum token para converter.")

    saida = []
    pilha = []
    espera_operando = True

    for token in tokens:
        if eh_numero(token):
            if not espera_operando:
                raise ValueError(f"Falta um operador antes de '{token}'.")
            saida.append(token)
            espera_operando = False

        elif token == '(':
            if not espera_operando:
                raise ValueError("Falta um operador antes de '('.")
            pilha.append(token)
            espera_operando = True

        elif token == ')':
            if espera_operando:
                raise ValueError("Expressao incompleta antes de ')'.")
            while len(pilha) > 0 and pilha[-1] != '(':
                saida.append(pilha.pop())
            if len(pilha) == 0:
                raise ValueError("Parenteses incompativeis: fechou ')' sem abrir '('.")
            pilha.pop()  # tira o '(' da pilha
            espera_operando = False

        elif eh_operador(token):
            if espera_operando:
                raise ValueError(f"Operador '{token}' fora de lugar.")
            # ^ tem associatividade a direita, os outros a esquerda
            while len(pilha) > 0 and pilha[-1] != '(':
                topo = pilha[-1]
                if (token != '^' and precedencia(topo) >= precedencia(token)) or (
                    token == '^' and precedencia(topo) > precedencia(token)
                ):
                    saida.append(pilha.pop())
                else:
                    break
            pilha.append(token)
            espera_operando = True

        else:
            raise ValueError(f"Token invalido: {token}")

    if espera_operando:
        raise ValueError("A expressao terminou esperando um numero.")

    while len(pilha) > 0:
        op = pilha.pop()
        if op in ('(', ')'):
            raise ValueError("Parenteses incompativeis: abriu '(' e nao fechou.")
        saida.append(op)

    return saida


# 8. Construir a arvore
def construir_arvore(posfixa):
    pilha = []

    for token in posfixa:
        if eh_numero(token):
            pilha.append(No(token))
        elif eh_operador(token):
            if len(pilha) < 2:
                raise ValueError("Expressao invalida na montagem da arvore.")
            # primeiro pop e o filho da direita, segundo e o da esquerda
            no_dir = pilha.pop()
            no_esq = pilha.pop()

            novo_no = No(token)
            novo_no.esquerda = no_esq
            novo_no.direita = no_dir
            pilha.append(novo_no)

    if len(pilha) != 1:
        raise ValueError("Erro ao montar a arvore: sobraram elementos na pilha.")

    return pilha[0]


# 9. Percursos
# Relacao entre os percursos e as notacoes:
# - Pre-ordem (Raiz, Esquerda, Direita): gera a notacao prefixa (operador vem antes dos numeros).
# - Em ordem (Esquerda, Raiz, Direita): gera a notacao infixa tradicional (operador fica no meio).
# - Pos-ordem (Esquerda, Direita, Raiz): gera a notacao pos-fixa (operador vem depois dos numeros).

def pre_ordem(no):
    if no is None:
        return []
    return [str(no.valor)] + pre_ordem(no.esquerda) + pre_ordem(no.direita)


def em_ordem(no):
    if no is None:
        return []
    return em_ordem(no.esquerda) + [str(no.valor)] + em_ordem(no.direita)


def pos_ordem(no):
    if no is None:
        return []
    return pos_ordem(no.esquerda) + pos_ordem(no.direita) + [str(no.valor)]


# 10. Reconstruir a expressao
def gerar_expressao(no):
    if no is None:
        return ""
    # se for folha (numero), retorna so o valor
    if no.esquerda is None and no.direita is None:
        return str(no.valor)
    esq = gerar_expressao(no.esquerda)
    dir = gerar_expressao(no.direita)
    return f"({esq} {no.valor} {dir})"


# 11. Calcular pela arvore
def calcular(no):
    if no is None:
        return 0

    # se for folha, converte o token para numero
    if no.esquerda is None and no.direita is None:
        val = float(no.valor)
        return int(val) if val.is_integer() and '.' not in str(no.valor) else val

    esq = calcular(no.esquerda)
    dir = calcular(no.direita)

    op = no.valor
    if op == '+':
        res = esq + dir
    elif op == '-':
        res = esq - dir
    elif op == '*':
        res = esq * dir
    elif op == '/':
        if dir == 0:
            raise ZeroDivisionError("Erro: divisao por zero nao permitida.")
        res = esq / dir
    elif op == '^':
        if esq == 0 and dir < 0:
            raise ZeroDivisionError("Erro: zero elevado a expoente negativo gera divisao por zero.")
        if esq < 0 and not float(dir).is_integer():
            raise ValueError("Erro: base negativa com expoente nao inteiro nao e permitida.")
        res = esq ** dir
    else:
        raise ValueError(f"Operador desconhecido: {op}")

    # se o resultado for inteiro exato (ex: 16.0), mostra como int (16)
    if isinstance(res, float) and res.is_integer():
        return int(res)
    return res


# 16. Desafio opcional (contagens e exibicao da arvore no terminal)
def contar_nos(no):
    if no is None:
        return 0
    return 1 + contar_nos(no.esquerda) + contar_nos(no.direita)


def contar_folhas(no):
    if no is None:
        return 0
    if no.esquerda is None and no.direita is None:
        return 1
    return contar_folhas(no.esquerda) + contar_folhas(no.direita)


def altura(no):
    if no is None:
        return 0
    return 1 + max(altura(no.esquerda), altura(no.direita))


def mostrar_arvore(no, nivel=0, lado="Raiz"):
    if no is not None:
        indent = "   " * nivel
        print(f"{indent}|__ [{lado}] {no.valor}")
        if no.esquerda is not None or no.direita is not None:
            mostrar_arvore(no.esquerda, nivel + 1, "E")
            mostrar_arvore(no.direita, nivel + 1, "D")


# 12. Funcao para rodar tudo e mostrar a saida pedida
def executar_expressao(expressao):
    print("\n--------------------------------------------------")
    print(f"Expressao: {expressao}")
    try:
        tokens = tokenizar(expressao)
        posfixa = para_posfixa(tokens)
        raiz = construir_arvore(posfixa)

        print("Tokens reconhecidos:", tokens)
        print("Pos-fixa:           ", " ".join(posfixa))
        print("Pre-ordem:          ", " ".join(pre_ordem(raiz)))
        print("Em ordem:           ", " ".join(em_ordem(raiz)))
        print("Pos-ordem:          ", " ".join(pos_ordem(raiz)))
        print("Expressao gerada:   ", gerar_expressao(raiz))

        resultado = calcular(raiz)
        print("Resultado:          ", resultado)

        print(f"Nos: {contar_nos(raiz)} | Folhas: {contar_folhas(raiz)} | Altura: {altura(raiz)}")
        print("Arvore:")
        mostrar_arvore(raiz)
        return resultado

    except (ValueError, ZeroDivisionError, OverflowError) as e:
        print("Erro:", e)
        return None


# 13. Testes obrigatorios + testes de validacao e potencia
if __name__ == "__main__":
    print("=== EXECUTANDO TESTES OBRIGATORIOS ===")
    testes = [
        "8 + 4 * 2",
        "(8 + 4) * 2",
        "((15 - 3) / 4) + (2 * 5)",
        "((20 / 5) + 3) * (9 - (2 + 1))",
        "12.5 + 2.5 * 4",
        "2 + 3 * 2 ^ 3",      # teste do ponto extra (potencia)
        "(-5 + 3) * 2 ^ 2",   # teste opcional (negativo + potencia)
        "2 * -(3 + 1)",       # menos unario antes de parenteses: -8
        "5 - -(2)",           # 7
        "2 ^ -(1 + 1)",       # 0.25
        "8 / -(2)",           # -4
        "-(2 + 3) * 2"        # -10
    ]

    for t in testes:
        executar_expressao(t)

    print("\n=== TESTES DE VALIDACAO (ERROS ESPERADOS) ===")
    erros = [
        "10 / (4 - 4)",   # divisao por zero
        "((8 + 4) * 2",   # parenteses incompativeis
        "   ",            # expressao vazia
        "8 + 4 @ 2",      # caractere nao aceito
        "(-8) ^ 0.5",     # base negativa com expoente nao inteiro
        "2.5 ^ 10000"     # overflow tratado
    ]

    for e in erros:
        executar_expressao(e)

    # Loop para digitar novas expressoes sem reiniciar
    print("\n=== MODO INTERATIVO ===")
    while True:
        try:
            entrada = input("\nDigite uma expressao (ou 'sair' para encerrar): ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nPrograma encerrado.")
            break
        if entrada.lower() == "sair" or entrada == "":
            print("Programa encerrado.")
            break
        executar_expressao(entrada)


# -------------------------------------------------------------------------
# 15. QUESTOES DE ANALISE
# -------------------------------------------------------------------------
# 1. Por que a expressao precisa ser tokenizada?
# R: Porque a expressao vem como uma string unica. Se percorrermos caractere por
# caractere sem tokenizar, numeros com mais de um digito (como 15) ou decimais
# (como 12.5) seriam lidos separados ('1' e '5'), quebrando a logica do calculo.
#
# 2. Por que uma pilha e adequada para operadores e parenteses?
# R: Porque na conversao para pos-fixa os operadores precisam esperar os operandos
# e respeitar a ordem de prioridade e os parenteses mais internos. Como a pilha
# funciona no esquema LIFO (ultimo que entra e o primeiro que sai), o operador mais
# recente ou de maior precedencia e desempilhado primeiro.
#
# 3. Por que o primeiro pop na construcao da arvore corresponde ao filho direito?
# R: Porque na notacao pos-fixa o operando da esquerda e empilhado antes do operando
# da direita. Assim, o operando da direita fica no topo da pilha. Quando fazemos o
# primeiro pop(), tiramos quem esta no topo (direita), e no segundo pop() tiramos o
# da esquerda. Se inverter isso, subtracao, divisao e potencia dao resultado errado.
#
# 4. Qual a relacao entre pos-ordem e notacao pos-fixa?
# R: O percurso em pos-ordem visita primeiro a esquerda, depois a direita e por
# ultimo a raiz (o operador). Isso gera exatamente a mesma sequencia da notacao
# pos-fixa, onde os numeros aparecem antes do operador deles.
#
# 5. Para uma arvore com n nos, qual a complexidade de tempo para calcular toda a expressao? Justifique.
# R: A complexidade e O(n). Isso acontece porque a funcao recursiva calcular() passa
# por cada um dos n nos da arvore exatamente uma vez, fazendo apenas uma operacao
# basica de tempo constante O(1) em cada no.
#
# 6. O que determina a quantidade maxima de chamadas recursivas simultaneas?
# R: A altura da arvore. Como a recursao vai descendo pelos filhos ate chegar numa
# folha antes de voltar, o maximo de chamadas abertas ao mesmo tempo na memoria
# equivale ao maior caminho da raiz ate uma folha (altura h).
