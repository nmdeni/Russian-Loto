import pandas as pd
import numpy as np
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

def main():
    # Подкласс QMainWindow для настройки главного окна приложения
    class MainWindow(QMainWindow):
        def __init__(self):
            super().__init__()

            # Наполняем окно виджетами
            self.setWindowTitle("RUSSIAN LOTO")
            button_1 = QPushButton("but  1")
            button_2 = QPushButton("but 2")

            # Устанавливаем центральный виджет Window.
            self.setCentralWidget(button_1)

    num_list = []
    user_num_list = []
    user_scores = 0
    # Приложению нужен один (и только один) экземпляр QApplication.
    # Передаём sys.argv, чтобы разрешить аргументы командной строки для приложения.
    # Если не будете использовать аргументы командной строки, QApplication([]) тоже работает
    app = QApplication(sys.argv)
    # Создаём виджет Qt — окно.
    window = MainWindow()
    # Важно: окно по умолчанию скрыто.
    window.show()

    #  генерируем числа (боченки)
    for i in range(0,101):
        num_list.append(i)

    #  генерируем числа у юзера
    for i in range(5):
        user_num_list.append(int(np.random.randint(0, 100)))
    
    # Приложение пойдет дальше, пока вы не выйдете и цикл
    # событий не остановится.
    # Запускаем цикл событий.
    app.exec()
if __name__ == '__main__':
    main()

# загруэаем данные из json с п. pandas и ставим разделитель \t
# loaded_data = pd.read_json('./data_ml.json')