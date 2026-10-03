import sys
from pathlib import Path

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QMessageBox, QPushButton, QWidget


BASE_DIR = Path(__file__).resolve().parent
IMAGE_PATH = BASE_DIR / "assets" / "label.png"


class LabWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Лабораторная работа №1")
        self.resize(600, 400)

        self.label = QLabel("Надпись", self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setGeometry(150, 60, 300, 210)
        self.label.setStyleSheet(
            "QLabel {"
            "border: 1px solid #bdbdbd;"
            "font-size: 20px;"
            "}"
        )

        self.button = QPushButton("Показать изображение", self)
        self.button.setGeometry(190, 300, 220, 45)

        # Сигнал нажатия кнопки подключаем к обработчику.
        self.button.clicked.connect(self.show_image)

    def show_image(self):
        pixmap = QPixmap(str(IMAGE_PATH))

        if pixmap.isNull():
            QMessageBox.warning(
                self,
                "Ошибка",
                f"Не удалось загрузить изображение:\n{IMAGE_PATH}",
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


def main():
    app = QApplication(sys.argv)

    window = LabWindow()
    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
