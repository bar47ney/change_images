import requests
import os
from PIL import Image

# массив ссылок на картинки
urls = ["https://example.com/example1.jpg", 
"https://example.com/example/example2.jpg", 
"https://example.com/example/example3.jpg",]



# # создание директории для сохранения файлов
# if not os.path.exists('images333'):
#     os.makedirs('images333')

# # скачивание картинок
# for url in urls:
#     response = requests.get(url)
#     filename = url.split('/')[-1]
#     with open(f'images333/{filename}', 'wb') as file:
#         file.write(response.content)
#         print(f'{filename} has been downloaded')

# получаем список файлов в папке result
files = os.listdir('images')
if not os.path.exists('result'):
    os.makedirs('result')

# обходим каждый файл
for file in files:
    # открываем файл с помощью Pillow
    img = Image.open('images/' + file)
    # получаем текущие размеры картинки
    width, height = img.size
    # задаем новую ширину (например, 500 пикселей)
    new_width = 396
    # вычисляем новую высоту с сохранением пропорций
    new_height = int((new_width / width) * height)
    # изменяем размер картинки с помощью метода resize
    img = img.resize((new_width, new_height))
    # сохраняем измененную картинку в ту же папку    
    img.save('result/' + file)