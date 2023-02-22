import pandas as pd
import numpy as np
import sys
from PyQt6.QtWidgets import (
    QApplication, 
    QMainWindow, 
    QPushButton, 
    QLabel, 
    QWidget, 
    QVBoxLayout 
)
from PyQt6.QtCore import Qt, QSize

def main():
    # Подкласс QMainWindow для настройки главного окна приложения
    class MainWindow(QMainWindow):
        def __init__(self):
            super(MainWindow, self).__init__()

            num_list = []
            user_num_list = []
            user_scores = 0

            #  генерируем числа (боченки)
            for i in range(0,101):
                num_list.append(i)

            #  генерируем числа у юзера
            for i in range(5):
                user_num_list.append(int(np.random.randint(0, 100)))

            # Наполняем окно виджетами
            self.setWindowTitle("RUSSIAN LOTO")
            scores_label = QLabel(
                f"Ваши боченки - {' | '.join([str(item) for item in user_num_list])}\nВаши очки - {user_scores}"
            )
            
            button_1 = QPushButton("ДОСТАТЬ БОЧОНОК")
            

            # Вставляем остальные 
            layout = QVBoxLayout()
            layout.addWidget(scores_label)
            layout.addWidget(button_1)

            # Устанавливаем виджеты от центра поумолчанию
            widget = QWidget()
            widget.setLayout(layout)
            self.setFixedSize(QSize(400,300))
            self.setCentralWidget(widget)

    # Приложению нужен один (и только один) экземпляр QApplication.
    # Передаём sys.argv, чтобы разрешить аргументы командной строки для приложения.
    # Если не будете использовать аргументы командной строки, QApplication([]) тоже работает
    app = QApplication(sys.argv)
    # Создаём виджет Qt — окно.
    window = MainWindow()
    # Важно: окно по умолчанию скрыто.
    window.show()
    # Приложение пойдет дальше, пока вы не выйдете и цикл
    # событий не остановится.
    # Запускаем цикл событий.
    app.exec()
if __name__ == '__main__':
    main()

# загруэаем данные из json с п. pandas и ставим разделитель \t
# loaded_data = pd.read_json('./data_ml.json')