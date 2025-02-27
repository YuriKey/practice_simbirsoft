## Инструкция для запуска автоматизированных тест-кейсов.

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
    git clone https://github.com/YuriKey/internship_simbirsoft.git
    ```
    
    и перейдите в директорию проекта:
    
    ```plaintext
    cd internship_simbirsoft
    ```
    
4.  Создайте виртуальное окружение командой:
    
    *   для Windows:
        
        ```plaintext
        python -m venv venv
        ```
        
    *   для MacOS:
        
        ```plaintext
        python3 -m venv venv
        ```
        
        и активируйте его:
        
    *   для Windows:
    
    ```plaintext
    venv\Scripts\activate
    ```
    
    ```plaintext
    source venv/bin/activate
    ```
    
5.  Установите зависимости, указанные в файле **requirements.txt**:
    
    ```plaintext
    pip install -r requirements.txt
    ```
    
6.  Запустите тесты в консоли командой:
    
    ```python
    pytest
    ```