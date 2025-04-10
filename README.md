## 1. Файловая структура проекта

---

```plaintext
├── .github/
    ├── workflows                       # Директория для конфигурациионных файлов CI/CD
├── api_tests/                          # Директория для хранения фреймворка для тестов API.
    ├── backend/                        # Бэкенд для тестирования API.
        ├── ...
    ├── data/                           # Директория для хранения данных.
        ├── data_generator/             # Генератор тестовых данных.
            ├── base_generator.py       # Класс и методы базового генератора.
            ├── item_generator.py       # Класс и методы экземпляра генератора.
        ├── dataclasses/                # Директория для хранения Pydantic-моделей.
           ├── item_data.py             # Модуль для модели данных item.
        ├── urls.py                     # Файл для хранения url. 
    ├── tests/                          # Исполняемые тесты API. 
        ├── ...
    ├── utils/                          # Вспомогательные утилиты для API тестов.
        ├── assertions.py               # Модуль для методов проверок ожиданий.
    ├── conftest.py                     # Конфигурационный файл для запуска тестов API. 
├── ui_tests/                           # Директория для хранения фреймворка для тестов GUI.
    ├── data/                           # Директория для хранения данных.
        ├── urls.py                     # Файл для хранения url.
    ├──locators/                        # Директория для хранения локаторов страниц.
        ├── add_customer_locators.py    # Файл с локаторами объектов страницы добавления клиента.
        ├── customer_list_locators.py   # Файл с локаторами объектов страницы со списком клиентов.
    ├── pages/                          # Директория с модулями страниц.
        ├── add_customer_page.py        # Класс и методы страницы добавления клиента. 
        ├── base_page.py                # Класс и методы базовой страницы.
        ├── customer_list_page.py       # Класс и методы страницы со списком клиентов.
    ├── tests/                          # Исполняемые тесты GUI.
        ├── ...
    ├── utils/                          # Вспомогательные утилиты для GUI тестов.
        ├── ...
    ├── conftest.py                     # Конфигурационный файл для инициализации драйвера тестов GUI.
    ├── test_cases.md                   # Список тест-кейсов для автоматизации.
├── .gitignore
├── pytest.ini                          # Конфигурационный файл для запуска тестов.
├── README.md                           # Информационный файл. Вы находитесь здесь:)
├── requirements.txt                    # Список используемых библиотек и плагинов.


```

---


## 2. Инструкция для запуска автоматизированных тест-кейсов на локальной машине.

---

1.  Убедитесь, что на Вашем компьютере установлен Python. В терминале выполните команду:
    
    *   для Windows:
        
        ```plaintext
        python --version
        ```
        
    *   для MacOS:
        
        ```plaintext
        python3 --version
        ```

    Если Python установлен, то вы увидите сообщение с версией.
    
    Если он не установлен, то установите с официального [сайта Python](https://www.python.org/downloads/), выбрав подходящую версию для Вашей операционной системы, и пройдите шаг сначала. В процессе установки обязательно поставьте галочку в чекбоксе "Add python.exe to PATH". Иначе, у Вас не будет корректно отображаться версия Python.

    
2.  Откройте терминал, перейдите в нужную Вам директорию с помощью команды:
    
    ```plaintext
    cd <здесь укажите путь до директории с проектом>
    ```
    
3.  Склонируйте к себе репозиторий, в котором хранится проект тестового задания, через выполнение команды в терминале:
    
    ```plaintext
    git clone https://github.com/YuriKey/practice_simbirsoft.git
    ```
    
    и перейдите в директорию проекта:
    
    ```plaintext
    cd practice_simbirsoft
    ```
    
4.  Создайте виртуальное окружение командой:
    
    *   для Windows:
        
        ```plaintext
        python -m venv .venv
        ```
        
    *   для MacOS:
        
        ```plaintext
        python3 -m venv .venv
        ```
        
        и активируйте его:
        
    *   для Windows:
    
    ```plaintext
    .venv\Scripts\activate
    ```
    
    ```plaintext
    source .venv/bin/activate
    ```
    
5.  Установите зависимости, указанные в файле **requirements.txt**:
    
    ```plaintext
    pip install -r requirements.txt
    ```
     
6. Раскомментируйте в файле ui_tests/conftest.py блок кода "Local launch". 

    Закомментируйте блок кода "CI/CD Launch".


7. Запустите тесты в консоли командой:
    
    ```python
    pytest
    ```

8. После завершения тестов выполните в консоли команду:

    ```python
    allure serve allure_result
    ```