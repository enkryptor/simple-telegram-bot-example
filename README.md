# Simple telegram bot example

"Продавец слонов" — простой пример телеграм-бота на пайтоне без внешних библиотек.

### Файлы:

 - api.py — модуль работы с api (получение-отправка запросов)
 - extract.py — модуль сопутствующих вычислений (трансформация данных, полученных через api)
 - main.py — модуль с бизнес-логикой бота

### Как запустить:

 0. Создать нового бота через @BotFather (если ещё не создан)
 1. Скачать к себе репозиторий: `git clone https://github.com/enkryptor/simple-telegram-bot-example.git`
 2. В файле api.py указать api-токен бота, созданного на шаге 0
 3. Запустить код бота командой `python main.py`
