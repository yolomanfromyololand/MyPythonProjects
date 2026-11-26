# Lab07_Pandas_and_Matplotlib

Pandas и Matplotlib.

**Цель:** Series, DataFrame, фильтрация, CSV, анализ журналов и построение графиков.

## Задания

| Исходный файл | Новый файл | Что делаю |
| --- | --- | --- |
| `task1.py` | [task01_create_and_index_pandas_series.py](task01_create_and_index_pandas_series.py) | Создать Series из списка, массива и словаря; выбрать значения по позиции и метке. |
| `task2.py` | [task02_build_and_explore_dataframes.py](task02_build_and_explore_dataframes.py) | Создать таблицу книг и выбрать столбцы, первые строки, размер и отдельную ячейку. |
| `task3.py` | [task03_filter_and_sort_student_grades.py](task03_filter_and_sort_student_grades.py) | Отфильтровать и отсортировать оценки, добавить логический столбец Honours. |
| `task4.py` | [task04_analyse_security_log_csv.py](task04_analyse_security_log_csv.py) | Прочитать CSV журнала безопасности, выбрать события и проанализировать блокировки, сервисы и объём передач. |
| `task5.py` | [task05_plot_styled_line_charts.py](task05_plot_styled_line_charts.py) | Построить две линии с разным оформлением, подписями осей, легендой и сеткой. |
| `task6.py` | [task06_plot_bar_scatter_and_histogram.py](task06_plot_bar_scatter_and_histogram.py) | Построить столбчатую диаграмму, диаграмму рассеяния и гистограмму. |
| `task7.py` | [task07_visualise_security_events.py](task07_visualise_security_events.py) | Объединить Pandas и Matplotlib: показать события по сервисам и времени на двух графиках. |

## Запуск

Из корня репозитория:

```powershell
cd Lab07_Pandas_and_Matplotlib
python task01_create_and_index_pandas_series.py
```

Для другого задания замените имя скрипта на нужное из таблицы. Запускайте скрипты из этой папки, чтобы относительные пути к данным работали. Зависимости устанавливаются командой `python -m pip install -r requirements.txt` из корня репозитория.
