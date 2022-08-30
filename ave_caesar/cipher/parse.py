__all__ = ['get_parse']


def get_parse(text_input: str) -> list[str]:
    """Преобразует строку текста в список.
    Знаки пунктуации, числа отделяет от текста.
    """

    marks = '!"#$%&()*+,-./:;<=>?@[]^_`{|}~' + "\'"
    text_output = []
    text_temp = ''

    for char in text_input:

        if char.isspace() or char in marks:

            if text_temp:
                text_output.append(text_temp)
                text_temp = ''

            text_output.append(char)

        elif char.isalnum():

            if not text_temp:
                text_temp += char

            else:

                if char.isalpha() and text_temp.isalpha():
                    text_temp += char

                else:
                    text_output.append(text_temp)
                    text_temp = ''
                    text_temp += char

    text_output.append(text_temp)

    return text_output
