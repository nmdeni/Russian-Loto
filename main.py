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

# Подкласс QMainWindow для настройки главного окна приложения
class MainWindow(QMainWindow):
    layout = QVBoxLayout()
    barrels_table_text = ''
    num_list = []
    show_barells = []
    user_num_list = []
    user_scores = 0
    count = 0
    
         

    def get_barell(self):
        self.count += 1
        barell = self.num_list[np.random.randint(0,100)]
        barrels = self.show_barells
        
        if len(barrels) == 0:
            barrels.append(barell)
            self.barrels_table_text = f'Бочонки: {barrels}'
            self.barrels_table.setText(self.barrels_table_text)
            
            for k in self.user_num_list:
                if k == barell:
                    self.user_scores += 1
                    self.scores_label.setText(str(self.user_scores))

        elif len(barrels) >= 10:
            print('ВСЕ')

        else:
            for i in barrels:
                if barell == i:
                    barell = self.num_list[np.random.randint(0,100)]
                else:
                    barrels.append(barell)
                    self.barrels_table_text = f'Бочонки: {barrels}'
                    self.barrels_table.setText(self.barrels_table_text)

                    for k in self.user_num_list:
                        if k == barell:
                            self.user_scores += 1
                            self.scores_label.setText(str(self.user_scores))

                    break
                        

    def __init__(self):
        super().__init__()

        #  генерируем числа (боченки)
        for i in range(0,101):
            self.num_list.append(i)

        #  генерируем числа у юзера
        for i in range(5):
            self.user_num_list.append(int(np.random.randint(0, 100)))

        # Наполняем окно виджетами
        self.setWindowTitle("RUSSIAN LOTO")
        self.scores_label = QLabel(
            f"Ваши боченки - {' | '.join([str(item) for item in self.user_num_list])}\nВаши очки - {self.user_scores}"
        )
        self.barrels_table = QLabel(f"{self.barrels_table_text}")
        
        button_1 = QPushButton("ДОСТАТЬ БОЧОНОК", self)
        button_1.clicked.connect(self.get_barell)

        # Вставляем остальные 
        self.layout.addWidget(self.scores_label)
        self.layout.addWidget(self.barrels_table)
        self.layout.addWidget(button_1)

        # Устанавливаем виджеты от центра поумолчанию
        widget = QWidget()
        widget.setLayout(self.layout)
        self.setFixedSize(QSize(400,300))
        self.setCentralWidget(widget)

    

if __name__ == '__main__':
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