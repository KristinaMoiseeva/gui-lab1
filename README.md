# Лабораторная работа №1 — PyQt5

## Задание

Создать графическое окно, кнопку и надпись.  
При нажатии на кнопку надпись должна заменяться изображением.

## Описание программы

Программа написана на Python с использованием библиотеки PyQt5.

После запуска открывается окно, в котором находятся:

- надпись `QLabel`;
- кнопка `QPushButton`.

При нажатии на кнопку **«Показать изображение»** текст в `QLabel`
заменяется изображением из файла `assets/label.png`.

Для обработки нажатия используется механизм сигналов и слотов Qt:

```python
self.button.clicked.connect(self.show_image)
```

## Структура проекта

```text
gui-lab1/
├── assets/
│   └── label.png
├── main.py
├── README.md
└── requirements.txt
```

## Используемые технологии

- Python 3
- PyQt5
- QWidget
- QLabel
- QPushButton
- QPixmap
- сигналы и слоты Qt

## Установка

На Windows в PowerShell, находясь в папке проекта:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

## Запуск

```powershell
.\.venv\Scripts\python.exe main.py
```

После запуска нажмите кнопку **«Показать изображение»** — надпись в окне
заменится картинкой.
