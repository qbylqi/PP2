def reverse_sentence(sentence):
    return ' '.join(sentence.split()[::-1])

# Пример использования
print(reverse_sentence('We are ready'))  # Вывод: ready are We
"""
Объяснение: функция разбивает строку на слова, разворачивает их и соединяет обратно в предложение.
"""