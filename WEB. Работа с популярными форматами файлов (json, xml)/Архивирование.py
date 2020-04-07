import zipfile
import os
import datetime
def make_reserve_arc(source, dest):
   now = datetime.datetime.now()
   d = now.day
   y = now.year
   m = now.month
   h = now.hour
   mn = now.minute
   s = now.second
   os.chdir(dest)
   z = zipfile.ZipFile(f'{d}_{m}_{y}_{h}{mn}{s}.zip', 'w')
   os.chdir(source)
   for root, dirs, files in os.walk(source):
      for file in files:
         if len(file) > 4:
            if file[-4:] == '.zip':
               continue
         z.write(os.path.join(root, file))
   z.close()
print('Привет!')
print('Формат ввода пути("C:\\folder1\\folder")')
print('Введите путь к папки, которую нужно заархивировать: ')
source = input()
print('Введите конечный путь: ')
dest = input()
make_reserve_arc(source, dest)