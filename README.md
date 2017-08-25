# CVTask_OdiCats
Решение задачи анализа видео потока команды OdiCats

## План
  1. Детектирование светофора на изображении (Haar cascades)
  2. [Классификация найденого светофора на 2 класса (CNN)](https://github.com/nicklyu/CVTask_OdiCats#cnn)
  3. Анализ входящего видеопотока и нахождение кадров изменения светофора([OpenCV](http://opencv.org/) + бин. поиск(`нужно обсудить`))



#### Предварительная выборка
  * [Зеленые светофоры](https://drive.google.com/drive/folders/0B3fRcmqWqN0sczA5T2VkTlgwZ0U)
  * [Красные светофоры](https://drive.google.com/drive/folders/0B3fRcmqWqN0sQzJLWnYtaGtvd3c)
  * [Без светофоров](https://drive.google.com/drive/folders/0B3fRcmqWqN0sN3Zkem5kdjZFRVU)
  
#### Обучающая выборка
  * [Зеленые светофоры](https://drive.google.com/drive/folders/0B7QqEdYg-_31LWI5QzRxRmRMb28)
  * [Красные светофоры](https://drive.google.com/drive/folders/0B3fRcmqWqN0sREtLMlNwU0Rzb1E)

### CNN
##### Подготовка данных: [create_data.py](https://github.com/nicklyu/CVTask_OdiCats/blob/master/CNN/create_data.py)
Для запуска используется команда `python create_data.py directory target_directory extension weight height`
* *directory* - Имя директории с данными
* *target_directory* - Имя директории для сохранения
* *extension* - Расширение изображений
* *weight* - Ширина конечного изображения
* *height* - Высота конечного изображения

##### Изменение расширений изображений в выборке: [extension_changer.py](https://github.com/nicklyu/CVTask_OdiCats/blob/master/CNN/extension_changer.py)
Для запуска используется команда `python extension_changer.py directory target_directory from_ex to_ex`
* *directory* - Имя директории с данными
* *target_directory* - Имя директории для сохранения
* *from_ex* - Исходное расширение
* *to_ex* - Расширение после преобразования

##### Обучение классификатора: [train_model.py](https://github.com/nicklyu/CVTask_OdiCats/blob/master/CNN/train_model.py)
Для запуска используется команда `python train_model.py red_dir green_dir extension epochs`
* *red_dir* - Имя директории с красными светофорами
* *green_dir* - Имя директории с зелеными светофорами
* *extension* - Расширение изображений
* *epochs* - Кол-во эпох для обучения
