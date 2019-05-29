import re

while True:
    LANGUAGE = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

    text = str(input('Введите фразу для шифрования/дешиврования \n\n')).upper().replace(" ", "")
    key_phrase = str(input('\nВведитетекст фразу для шифровки \n\n')).upper().replace(" ", "")
    text = re.sub(r'[^А-Я]', '', text)
    key_phrase = re.sub(r'[^А-Я]', '', key_phrase)


    new_code = []
    for i in key_phrase:
        if i not in new_code:
            new_code.append(i)

    for i in LANGUAGE:
        if i not in new_code:
            new_code.append(i)

    while True:
        try:
            inp = int(input('шифруем или расшифровываем? (1/2)'))
        except ValueError:
            continue
        else:
            break

    final = ''

    if inp == 1:
        for i in text:
            if len(final) % 5 == 0:
                final += ' '
            final = final + LANGUAGE[new_code.index(i)]
    else:
        for i in text:
            if len(final) % 5 == 0:
                final += ' '
        final = final + new_code[LANGUAGE.index(i)]

    print(final)