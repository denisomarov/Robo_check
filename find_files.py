# модуль работы с файлами: поиска, сортировка, чтение, анализ
import os
import os.path
import pdfplumber

def files_check(dirName: str, ext: str):
    # получение имени файлов в указанной папке dirName
    # с расширением ext

    file_list = os.listdir(dirName)
    ext = '.'+ext

    if ext=='*':
        sorted_list = []
        if os.path.isfile(os.path.join(dirName, file)):
            sorted_list.append(file)
    else:
        sorted_list = []
        for file in file_list:
            if os.path.isfile(os.path.join(dirName, file)) and file.endswith(ext):
                sorted_list.append(file)

    return sorted_list

def dir_check(dirName = '.'):
    # получение списка папок в папке dirName

    dir_list = os.listdir(dirName)

    sorted_list = []
    for file in dir_list:
        if os.path.isdir(os.path.join(dirName, file)):
            sorted_list.append(file)

    return sorted_list

def read_files(dirName: str, fileName: str):
    # чтение текста из файла

    pdfReader = []

    with pdfplumber.open(dirName+'\\'+fileName) as pdf:
        for pages_ in pdf.pages:
            pdfReader.extend(pages_.extract_text().split('\n'))

    # закрытие файла
    pdf.close()

    return pdfReader


def find_trash(dirName: str, fileName: str):
    # ищем лишние строки - повторяющуюся и не несущую полезную нагрузку информацию

    with pdfplumber.open(dirName + '\\' + fileName) as pdf:

        # определяем число страниц в файле
        numPages = len(pdf.pages)

        # чтение информации из 1 и 2 страниц, для определения повторений
        if numPages == 1:
            extra_text = []
        else:
            page1 = pdf.pages[0].extract_text().split('\n')
            page2 = pdf.pages[1].extract_text().split('\n')

            # определяем лишние строк - обычно это колонтитулы
            # обрабатываем верхние колонтитулы
            extra_text = []

            for i in range(len(page1)):
                for k in range(len(page2)):
                    if (page1[i] == page2[k]) \
                            and (i == k) and (page1[i] != ' ') and (i < 3):
                        extra_text.append(page1[i])

            # обрабатываем нижние колонтитулы и особые колонтитулы
            for i in range(len(page1)):
                for k in range(len(page2)):
                    if (page1[i] == page2[k]) \
                            and ((len(page1) - i) == (len(page2) - k)) \
                            and (page1[i] != ' '):
                        extra_text.append(page1[i])

    # очищаем список от лишних пробелов - в начале и в конце
    for i in range(len(extra_text)):
        extra_text[i] = extra_text[i].strip()

    pdf.close()

    return extra_text



