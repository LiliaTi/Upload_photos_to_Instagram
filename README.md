# Космический инстаграм
Проект для автоматической публикации в [Инстаграм](https://www.instagram.com/) фотографий [SpaceX](https://www.spacex.com/) с запусками ракет и фотографий с телескопа [Хаббл](https://hubblesite.org/)

## Как установить
Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть есть конфликт с Python2) для установки зависимостей:

```python
pip install -r requirements.txt
```
## Как запустить

### Скачивание фотографий SpaceX
Используйте скрипт `fetch_spacex.py`:

```python
python fetch_spacex.py
```
Фотографии будут находится в каталоге `\Images` (если каталог еще не создан, он создастся автоматически)

### Скачивание фотографий Hubble
Используйте скрипт `fetch_hubble.py`:

```python
python fetch_hubble.py collection
```
Где, `collection` - название коллекции фотографий. Названия некоторых коллекций: `gallery`, `news`, `printshop`, `spacecraft`, `wallpaper`.

Фотографии будут находится в каталоге `\Images` (если каталог еще не создан, он создастся автоматически)

### Публикация в Instagram
Создайте в корне проекта файл `.env` и заполните Ваши данные(имя пользователя и пароль от Instagram):
```python
INSTA_LOGIN=YOUR_LOGIN
INSTA_PASSWORD=YOUR_PASSWORD
```
Далее используйте скрипт `upload.py`:
```python
python upload.py
```
Фотографии будут загружаться из каталога `\Images`

## Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/modules/)




