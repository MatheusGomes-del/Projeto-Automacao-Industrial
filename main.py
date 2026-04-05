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


