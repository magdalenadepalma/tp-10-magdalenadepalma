def find_max_value(d):
    mayor_score = 0
    mayor_alumno = ""
    for clave, valor in d.items():
        if valor > mayor_score:
            mayor_score = valor
            mayor_alumno = clave
    return mayor_alumno


def reverse_dict(d):
    reverse = {}
    for clave, valor in d.items():
        if valor in reverse:
            reverse[valor] = f'{reverse[valor]}{clave}'
        else:
            reverse[valor] = clave
    return reverse


def word_freq_counter(words):
    nada = ""
    dic_vacio = {}
    valor = 0
    for word in words:
        if word == nada:
            vacio = {}
            return vacio
        else:
            if word not in dic_vacio:
                valor = 1
                dic_vacio[word] = valor
            else:
                valor = dic_vacio[word]
                valor = valor + 1
                dic_vacio[word] = valor
    return dic_vacio


def find_biggest_expense(diccionario):
    max_avg = 0
    biggest_expense = ""
    for expense, costs in diccionario.items():
        total = 0
        count = 0
        for cost in costs:
            total = total + cost
            count = count + 1
        if count > 0:
            avg = total / count
            if avg > max_avg:
                max_avg = avg
                biggest_expense = expense
    return biggest_expense


def sum_of_expenses(expenses):
    result = {}
    for category, costs in expenses.items():
        total = 0
        for cost in costs:
            total = total + cost
        result[category] = total
    return result


def sum_of_expenses_by_type(expenses):
    result = {}
    for costs in expenses.values():
        for cost in costs:
            type = cost[0]
            amount = cost[1]
            if type in result:
                result[type] = result[type] + amount
            else:
                result[type] = amount
    return result
