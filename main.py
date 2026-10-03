import sys
from pathlib import Path

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPixmap
from PyQt5.QtWidgets import (
    QApplication,
    QFileDialog,
    QLabel,
    QMessageBox,
    QPushButton,
    QWidget,
)


BASE_DIR = Path(__file__).resolve().parent
LABEL_IMAGE = BASE_DIR / "assets" / "label.png"


class LabWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Лабораторная работа №1")
        self.resize(640, 420)

        self.window_background = None

        self.label = QLabel("Надпись", self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setGeometry(170, 70, 300, 190)
        self.label.setStyleSheet(
            "QLabel {"
            "background: rgba(255, 255, 255, 190);"
            "border: 1px solid #b8b8b8;"
            "border-radius: 8px;"
            "font-size: 18px;"
            "}"
        )

        self.button_image = QPushButton("Кнопка 1", self)
        self.button_image.setGeometry(150, 300, 150, 45)

        self.button_shape = QPushButton("Кнопка 2", self)
        self.button_shape.setGeometry(340, 300, 150, 45)

        # Сигнал clicked связывается со слотами-обработчиками.
        self.button_image.clicked.connect(self.show_image_in_label)
        self.button_shape.clicked.connect(self.load_window_shape)

    def show_image_in_label(self):
        """Заменяет текст QLabel на изображение."""
        pixmap = QPixmap(str(LABEL_IMAGE))

        if pixmap.isNull():
            QMessageBox.warning(
                self,
                "Ошибка",
                f"Не удалось загрузить изображение:\n{LABEL_IMAGE}",
            )
            return

        self.label.setText("")
        self.label.setPixmap(
            pixmap.scaled(
                self.label.size(),
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation,
            )
        )

    def load_window_shape(self):
        """Загружает PNG и использует его прозрачность как форму окна."""
        file_name, _ = QFileDialog.getOpenFileName(
            self,
            "Выберите полупрозрачный PNG",
            str(BASE_DIR / "assets"),
            "PNG images (*.png)",
        )

        if not file_name:
            return

        pixmap = QPixmap(file_name)
        if pixmap.isNull():
            QMessageBox.warning(self, "Ошибка", "Не удалось загрузить PNG-файл.")
            return

        # Масштабируем PNG до текущего размера окна.
        self.window_background = pixmap.scaled(
            self.size(),
            Qt.IgnoreAspectRatio,
            Qt.SmoothTransformation,
        )

        # Делаем системную рамку прозрачной и задаём маску по alpha-каналу PNG.
        self.setWindowFlag(Qt.FramelessWindowHint, True)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setMask(self.window_background.mask())

        # После изменения WindowFlag окно нужно показать повторно.
        self.show()
        self.update()

    def paintEvent(self, event):
        """Рисует выбранный PNG как фон окна."""
        if self.window_background is not None:
            painter = QPainter(self)
            painter.drawPixmap(self.rect(), self.window_background)

        super().paintEvent(event)


def main():
    app = QApplication(sys.argv)

    window = LabWindow()
    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
