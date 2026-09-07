# 🎭 Playwright Book

> Учебный проект по автоматизации веб-приложений на **Python + Pytest + Playwright**.

Проект предназначен для изучения UI-автоматизации, написания автотестов и практической работы с браузером через Playwright.

В проекте используются **Chromium**, **Pytest** и **Playwright Python API**. Тесты демонстрируют переходы между страницами, работу с элементами, ввод данных, нажатия клавиш, загрузки и другие базовые сценарии UI-автоматизации.

---

## 🛠 Стек

| Технология    | Назначение                              |
| ------------- | --------------------------------------- |
| 🐍 Python     | Основной язык проекта                   |
| 🧪 Pytest     | Запуск и организация тестов             |
| 🎭 Playwright | Управление браузером и UI-автоматизация |
| 🌐 Chromium   | Браузер для выполнения тестов           |

Зависимости проекта находятся в `requirements.txt`:

```text
pytest
playwright
pytest-playwright
```

Playwright позволяет автоматизировать Chromium, Firefox и WebKit через единый API.

---

## 📁 Структура проекта

```text
Playwright_book/
│
├── tests/
│   ├── __init__.py
│   └── test.py
│
├── .gitattributes
├── .gitignore
├── README.md
├── main.py
└── requirements.txt
```

### `main.py`

Пример использования Playwright через `sync_playwright()`.

В скрипте:

* запускается Chromium;
* открывается TodoMVC;
* создаются задачи;
* выполняются действия с элементами страницы;
* переключаются фильтры;
* после завершения закрываются `context` и браузер.

### `tests/test.py`

Пример автотеста, использующего Pytest и Playwright.

Тест демонстрирует:

* запуск браузера;
* создание browser context;
* открытие страницы;
* поиск элементов через `get_by_role()`;
* работу с `get_by_test_id()`;
* ввод текста;
* нажатие `Enter`;
* ожидание скачивания файла;
* закрытие браузера.

---

# 🚀 Установка

## 1. Клонировать репозиторий

```bash
git clone https://github.com/redrepublics/Playwright_book.git
```

Перейти в проект:

```bash
cd Playwright_book
```

---

## 2. Создать виртуальное окружение

### Windows PowerShell

```powershell
python -m venv .venv
```

Активировать:

```powershell
.venv\Scripts\Activate.ps1
```

После активации в терминале появится:

```text
(.venv)
```

---

## 3. Установить зависимости

```powershell
pip install -r requirements.txt
```

---

## 4. Установить браузеры Playwright

```powershell
playwright install
```

Эта команда устанавливает браузерные бинарники, необходимые Playwright для работы.

Если нужен только Chromium:

```powershell
playwright install chromium
```

---

# ▶️ Запуск Playwright

В проекте есть два основных способа запуска:

1. **обычный Python-скрипт** через `main.py`;
2. **автотесты через Pytest** из директории `tests`.

---

## 🐍 Запуск `main.py`

Запуск обычного Playwright-скрипта:

```powershell
python main.py
```

В `main.py` используется:

```python
with sync_playwright() as playwright:
    run(playwright)
```

Браузер запускается в обычном режиме:

```python
browser = playwright.chromium.launch(headless=False)
```

Поэтому при запуске открывается окно Chromium.

---

# 🧪 Запуск Pytest

Запустить все тесты:

```powershell
pytest
```

Более подробный вывод:

```powershell
pytest -v
```

Запустить конкретный файл:

```powershell
pytest tests/test.py
```

Запустить конкретный тест:

```powershell
pytest tests/test.py::TestMainPage::test_create_todo
```

Запустить тест с подробным выводом:

```powershell
pytest -v tests/test.py::TestMainPage::test_create_todo
```

---

# 🎭 Playwright CLI

Playwright имеет собственный CLI.

Посмотреть доступные команды:

```powershell
playwright --help
```

---

## 🌐 Установка браузеров

Установить все браузеры:

```powershell
playwright install
```

Только Chromium:

```powershell
playwright install chromium
```

Только Firefox:

```powershell
playwright install firefox
```

Только WebKit:

```powershell
playwright install webkit
```

---

# 🔎 Codegen

Одна из самых полезных возможностей Playwright — **Codegen**.

Codegen открывает браузер и позволяет выполнять действия вручную, одновременно генерируя код Playwright.

Например:

```powershell
playwright codegen https://demo.playwright.dev/todomvc/#/
```

После запуска можно:

1. кликать по элементам;
2. вводить текст;
3. переходить между страницами;
4. выбирать элементы;
5. получать готовый Playwright-код.

Это особенно удобно при изучении Playwright и поиске правильных локаторов.

---

# 🧭 Основные Playwright-команды

## Запуск браузера

Chromium:

```python
browser = playwright.chromium.launch()
```

Firefox:

```python
browser = playwright.firefox.launch()
```

WebKit:

```python
browser = playwright.webkit.launch()
```

Запуск с отображением браузера:

```python
browser = playwright.chromium.launch(headless=False)
```

---

## Создание Context

```python
context = browser.new_context()
```

Context можно рассматривать как отдельную изолированную сессию браузера.

---

## Создание страницы

```python
page = context.new_page()
```

---

## Переход на страницу

```python
page.goto("https://example.com")
```

---

# 🎯 Локаторы

Playwright предоставляет несколько удобных способов поиска элементов.

### По роли

```python
page.get_by_role("button", name="Submit").click()
```

### По тексту

```python
page.get_by_text("Login").click()
```

### По `test-id`

```python
page.get_by_test_id("text-input").click()
```

### CSS-селектор

```python
page.locator("#username").fill("admin")
```

### XPath

```python
page.locator('//input[@name="username"]').fill("admin")
```

Предпочтительно использовать устойчивые локаторы вроде `get_by_role()`, `get_by_label()` и `get_by_test_id()`, когда они доступны.

---

# ⌨️ Работа с элементами

## Клик

```python
page.get_by_role("button", name="Submit").click()
```

## Ввод текста

```python
page.get_by_role("textbox").fill("Hello")
```

## Нажатие клавиши

```python
page.get_by_role("textbox").press("Enter")
```

## Очистка поля

```python
page.get_by_role("textbox").fill("")
```

---

# 📥 Работа со скачиванием

Playwright позволяет явно ожидать скачивание файла.

```python
with page.expect_download() as download_info:
    page.get_by_role("link", name="Download").click()

download = download_info.value
```

После этого объект `download` содержит информацию о скачанном файле.

---

# 🖥️ Headless и Headed режим

## Headed

Браузер отображается на экране:

```python
browser = playwright.chromium.launch(headless=False)
```

Удобно во время разработки и отладки.

## Headless

Браузер работает без окна:

```python
browser = playwright.chromium.launch(headless=True)
```

Удобно для CI/CD и автоматического запуска тестов.

---

# 🧹 Закрытие браузера

После выполнения теста необходимо закрывать ресурсы:

```python
context.close()
browser.close()
```

При использовании `sync_playwright()` Playwright также автоматически завершает свою сессию после выхода из блока:

```python
with sync_playwright() as playwright:
    ...
```

---

# 🧪 Полезные команды Pytest

### Все тесты

```powershell
pytest
```

### Подробный режим

```powershell
pytest -v
```

### Ещё более подробный вывод

```powershell
pytest -vv
```

### Остановиться после первой ошибки

```powershell
pytest -x
```

### Запустить только тесты с определённым именем

```powershell
pytest -k "todo"
```

### Показать `print()` в консоли

```powershell
pytest -s
```

### Комбинация

```powershell
pytest -v -s
```

---

# 🐞 Отладка

Для разработки удобно запускать браузер в видимом режиме:

```python
browser = playwright.chromium.launch(headless=False)
```

Также можно использовать:

```python
page.pause()
```

Например:

```python
page.goto("https://example.com")
page.pause()
```

Playwright остановит выполнение и позволит исследовать страницу.

---

# 📚 Что изучается в проекте

Проект можно использовать как практическую базу для изучения:

* Python UI automation;
* Pytest;
* Playwright;
* Browser Context;
* Page;
* Locators;
* `get_by_role()`;
* `get_by_test_id()`;
* CSS selectors;
* ввод текста;
* keyboard actions;
* navigation;
* downloads;
* Headless / Headed mode;
* Codegen;
* запуск отдельных тестов;
* организацию тестового проекта.

---

# 🔄 Типовой workflow

После клонирования проекта последовательность работы выглядит так:

```text
Clone repository
       ↓
Create virtual environment
       ↓
Install requirements
       ↓
Install Playwright browsers
       ↓
Write / edit test
       ↓
Run pytest
       ↓
Debug
       ↓
Commit changes
       ↓
Push to GitHub
```

Команды:

```powershell
git clone https://github.com/redrepublics/Playwright_book.git
cd Playwright_book

python -m venv .venv
.venv\Scripts\Activate.ps1

pip install -r requirements.txt
playwright install

pytest -v
```

---

# 📌 Быстрая шпаргалка

| Задача                        | Команда                                                |
| ----------------------------- | ------------------------------------------------------ |
| Установить зависимости        | `pip install -r requirements.txt`                      |
| Установить браузеры           | `playwright install`                                   |
| Только Chromium               | `playwright install chromium`                          |
| Запустить Python-скрипт       | `python main.py`                                       |
| Все тесты                     | `pytest`                                               |
| Тесты подробно                | `pytest -v`                                            |
| Конкретный файл               | `pytest tests/test.py`                                 |
| Конкретный тест               | `pytest tests/test.py::TestMainPage::test_create_todo` |
| Остановиться на первой ошибке | `pytest -x`                                            |
| Показать `print()`            | `pytest -s`                                            |
| Codegen                       | `playwright codegen <URL>`                             |
| Помощь Playwright CLI         | `playwright --help`                                    |

---

# 🔗 Полезные ссылки

* 📦 **Репозиторий:** [Playwright_book](https://github.com/redrepublics/Playwright_book)
* 🎭 **Playwright:** [playwright.dev](https://playwright.dev/)
* 🧪 **Pytest:** [pytest.org](https://pytest.org/)

---

## 📄 License

Учебный проект. Используется для изучения Python, Pytest и Playwright.
