class Calculator:
    # Статическое поле для хранения последней операции
    last = None

    def __init__(self):
        # Инициализируем историю операций
        self.history_list = []

    def sum(self, a, b):
        result = a + b
        operation = f"sum({a}, {b}) == {result}"
        self.history_list.append(operation)
        Calculator.last = operation  # Обновляем последнюю операцию
        return result

    def sub(self, a, b):
        result = a - b
        operation = f"sub({a}, {b}) == {result}"
        self.history_list.append(operation)
        Calculator.last = operation
        return result

    def mul(self, a, b):
        result = a * b
        operation = f"mul({a}, {b}) == {result}"
        self.history_list.append(operation)
        Calculator.last = operation
        return result

    def div(self, a, b, mod=False):
        if mod:
            result = a % b
            operation = f"div({a}, {b}) == {result}"  # Не записываем параметр mod
        else:
            result = a / b
            operation = f"div({a}, {b}) == {result}"
        self.history_list.append(operation)
        Calculator.last = operation
        return result

    def history(self, n):
        # Возвращаем строку с операцией по индексу n
        if 1 <= n <= len(self.history_list):
            return self.history_list[-n]  # Возвращаем n-ю операцию от конца
        return None  # Если n вне диапазона

    @classmethod
    def clear(cls):
        cls.last = None