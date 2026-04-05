pieces = []
boxes = []
current_box = []


def evaluate_piece(weight, color, length):
    reasons = []

    if not (95 <= weight <= 105):
        reasons.append("Peso fora do padrão")

    if color.lower() not in ["azul", "verde"]:
        reasons.append("Cor inválida")

    if not (10 <= length <= 20):
        reasons.append("Comprimento fora do padrão")

    if len(reasons) == 0:
        return "APROVADA", []
    else:
        return "REPROVADA", reasons

def add_piece():
    id = input("ID da peça: ")
    weight = float(input("Peso (g): "))
    color = input("Cor: ")
    length = float(input("Comprimento (cm): "))

    status, reasons = evaluate_piece(weight, color, length)

    piece = {
        "id": id,
        "weight": weight,
        "color": color,
        "length": length,
        "status": status,
        "reasons": reasons
    }

    pieces.append(piece)

    if status == "APROVADA":
        print("Peça APROVADA")

        global current_box
        current_box.append(piece)

        if len(current_box) == 10:
            boxes.append(current_box)
            print("Caixa fechada com 10 peças!")
            current_box = []

    else:
        print("Peça REPROVADA")
        print("Motivos:", ", ".join(reasons))


def list_pieces():
    if not pieces:
        print("Nenhuma peça cadastrada")
        return

    for p in pieces:
        print(f"ID: {p['id']} | Status: {p['status']}")


def remove_piece():
    id = input("ID da peça para remover: ")

    global pieces
    pieces = [p for p in pieces if p["id"] != id]

    print("Peça removida (se existia)")


def list_boxes():
    if not boxes:
        print("Nenhuma caixa fechada")
        return

    for i, box in enumerate(boxes, start=1):
        print(f"Caixa {i} com {len(box)} peças")

def report():
    aprovadas = sum(1 for p in pieces if p["status"] == "APROVADA")
    reprovadas = [p for p in pieces if p["status"] == "REPROVADA"]

    print("\n--- RELATÓRIO FINAL ---")
    print(f"Total aprovadas: {aprovadas}")
    print(f"Total reprovadas: {len(reprovadas)}")
    print(f"Caixas utilizadas: {len(boxes)}")

    if reprovadas:
        print("\nDetalhes das reprovadas:")
        for p in reprovadas:
            print(f"ID: {p['id']} -> {', '.join(p['reasons'])}")

        
def menu():
    while True:
        print("\n1 - Cadastrar peça")
        print("2 - Listar peças")
        print("3 - Remover peça")
        print("4 - Listar caixas fechadas")
        print("5 - Gerar relatório")
        print("0 - Sair")

        op = input("Escolha: ")

        if op == "1":
            add_piece()
        elif op == "2":
            list_pieces()
        elif op == "3":
            remove_piece()
        elif op == "4":
            list_boxes()
        elif op == "5":
            report()
        elif op == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida")


menu()