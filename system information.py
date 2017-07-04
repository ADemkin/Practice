# задача написать скрипт, который выводит информацию о системе:
# имя текущей дирректории, OS, кодировка файловой системы, имя пользователя (логин), количество CPU.
# домашнее задание для курса geekbrains.ru


import os
import sys

c_dir = os.getcwd()
c_os = sys.platform
c_os_other = os.name
c_fs_enc = sys.getfilesystemencoding()
c_user = os.getlogin()
c_cpu = os.cpu_count()

print("Текущая рабочая директория: %s \nТекущая ОС: %s или %s \nКодировка файловой системы: %s \nТекущий "
      "пользователь: %s \nКол-во CPU: %s "
      % (c_dir, c_os,
         c_os_other, c_fs_enc,
         c_user, c_cpu))
