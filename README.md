# CVTask_OdiCats
Решение задачи анализа видео потока команды OdiCats

## План
  1. Детектирование светофора на изображении (Haar cascades)
  2. Классификация найденого светофора на 2 класса (CNN)
  3. Анализ входящего видеопотока и нахождение кадров изменения светофора([OpenCV](http://opencv.org/) + бин. поиск(`нужно обсудить`))



#### Выборка, подготовленная Ильей
  * [Зеленые светофоры](https://drive.google.com/drive/folders/0B3fRcmqWqN0sczA5T2VkTlgwZ0U)
  * [Красные светофоры](https://drive.google.com/drive/folders/0B3fRcmqWqN0sQzJLWnYtaGtvd3c)
  * [Без светофоров](https://drive.google.com/drive/folders/0B3fRcmqWqN0sN3Zkem5kdjZFRVU)


### CNN
##### Подготовка данных: create_data.py
Для запуска используется команда `python create_data.py directory target_directory extension height weight`
* *directory* - Имя директории с данными
* *target_directory* - Имя директории для сохранения
* *extension* - Расширение изображений
* *height* - Высота конечного изображения
* *weight* - Ширина конечного изображения
