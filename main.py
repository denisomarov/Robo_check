# Обработка pdf файлов, поиск необходимой информации, сбор, сохранение и формарование чек-листа
import find_files
import text_work

# отбираем папки, наименование которых состоит только из цифр
# dir_list = dir_check()
# chek_set = set('0123456789')
#
# list_ = []
# for dir_ in dir_list:
#     if set(dir_)<=chek_set:
#         list_.append(dir_)
# dir_list = list_

# читаем текст из файла
readtext = find_files.read_files('728886', 'Тендерная_документация_728886_2022-07-26.pdf')

# очищаем текст от лишних пробелов
text_work.text_space_clear(readtext)

# ищем и удаляем лишние строки
extra_text = find_files.find_trash('728886', 'Тендерная_документация_728886_2022-07-26.pdf')
readtext = text_work.line_clear(readtext, extra_text)

# сокращаем текст до русского варианта
readtext = text_work.text_rus_cut(readtext)

# соединяем разорванные строки
readtext = text_work.link_lines(readtext)
print(readtext)

findtext = text_work.text_find(readtext, 'Заказчик', 'Организатор')
print(findtext)




# for line_ in text:
#     print(line_)

# обработка всех папок
# for dir_ in dir_list:
#     for file_ in files_check(dir_, 'pdf'):
#         read_files(dir_, file_)
