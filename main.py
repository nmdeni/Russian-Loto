import pandas as pd
import numpy as np

def main():
    num_list = []
    user_num_list = []
    user_scores = 0

    #  генерируем числа
    for i in range(0,101):
        num_list.append(i)

    for i in range(5):
        user_num_list.append(int(np.random.randint(0, 100)))
        
if __name__ == '__main__':
    main()

# загруэаем данные из json с п. pandas и ставим разделитель \t
# loaded_data = pd.read_json('./data_ml.json')