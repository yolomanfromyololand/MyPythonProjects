# Lab06_Exceptions_and_NumPy

Исключения и NumPy.

**Цель:** Обработка ошибок try/except/finally, raise, массивы NumPy, статистика, индексация и изменение формы.

## Задания

| Исходный файл | Новый файл | Что делаю |
| --- | --- | --- |
| `task1.py` | [task01_handle_input_and_division_errors.py](task01_handle_input_and_division_errors.py) | Обработать неверный числовой ввод и деление на ноль. |
| `task2.py` | [task02_handle_file_errors_with_finally.py](task02_handle_file_errors_with_finally.py) | Обработать отсутствующий файл и некорректное число; выполнить finally. |
| `task3.py` | [task03_validate_withdrawals_with_raise.py](task03_validate_withdrawals_with_raise.py) | Выбросить ValueError для недопустимого снятия денег и обработать его в вызывающей функции. |
| `task4.py` | [task04_create_and_inspect_numpy_arrays.py](task04_create_and_inspect_numpy_arrays.py) | Создать обычные и специальные массивы NumPy, проверить ndim, shape, size и dtype. |
| `task5.py` | [task05_array_arithmetic_and_statistics.py](task05_array_arithmetic_and_statistics.py) | Выполнить поэлементную арифметику, broadcasting и вычислить статистику массива. |
| `task6.py` | [task06_index_slice_and_reshape_arrays.py](task06_index_slice_and_reshape_arrays.py) | Выбрать строки, столбцы и срезы матрицы, подсчитать суммы по осям и проверить reshape. |
| `task7.py` | [task07_analyse_packet_sizes.py](task07_analyse_packet_sizes.py) | Загрузить размеры пакетов из файла, обработать ошибки и отобрать крупные пакеты булевой маской. |

## Запуск

Из корня репозитория:

```powershell
cd Lab06_Exceptions_and_NumPy
python task01_handle_input_and_division_errors.py
```

Для другого задания замените имя скрипта на нужное из таблицы. Запускайте скрипты из этой папки, чтобы относительные пути к данным работали. Зависимости устанавливаются командой `python -m pip install -r requirements.txt` из корня репозитория.
