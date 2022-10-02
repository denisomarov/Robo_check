# модуль обработки текста, полученного из pdf файла

def text_space_clear(text: list):
    # очистка списка text от лишних пробелов, которые могли
    # быть в начале или конце строк или внутри текста

    for i in range(len(text)):
        text[i] = text[i].strip()
    return text

def text_rus_cut(text: list):
    # сокращаем документ до русского варианта

    if text[0] == 'ТЕХНИКАЛЫҚ СИПАТТАМА':
        text = text[text.index('ТЕХНИЧЕСКАЯ СПЕЦИФИКАЦИЯ'):]

    if text[0] == 'ЭЛЕКТРОНДЫ САТЫП АЛУ ТУРАЛЫ ХАБАРЛАНДЫРУ':
        text = text[text.index('ОБЪЯВЛЕНИЕ ОБ ЭЛЕКТРОННЫХ ЗАКУПКАХ СПОСОБОМ'):]

    if text[0] == 'Электрондық тендерлік құжаттама':
        text = text[text.index('ЭЛЕКТРОННАЯ ТЕНДЕРНАЯ ДОКУМЕНТАЦИЯ'):]

    return text

def line_clear(text: list, extra_text: list):
    # удаляем лишние строки со страниц
    pdf_text = []

    for txtline_ in text:
        if txtline_ not in extra_text:
            pdf_text.append(txtline_)

    return pdf_text

def link_lines(text: list):
    # соединяем разорванные строки

    text_ = []

    # убираем пустые строки
    for line_ in text:
        if line_ != '':
            text_.append(line_)

    # соединяем разорванные строки
    list_ = text[0]

    for i in range(len(text)-1):
        if text[i][-2:] == ' -' and text[i+1][0].islower():
            list_ = list_[:-2] + text[i+1]
        elif text[i][-1:] == '-' and text[i+1][0].islower():
            list_ = list_[:-1] + text[i + 1]
        else:
            list_ = list_ + ' ' + text[i+1]

    list_ = list_.replace('  ', ' ')

    return list_

def text_find(text: str, start_text: str, end_text: str):
    # поиск текста между двумя фразами

    start_index = text.find(start_text)
    end_index = text.find(end_text)

    if (start_index == -1) or (end_index == -1) or (start_index>=end_index):
        return ''
    else:
        return text[start_index+len(start_text):end_index].strip()