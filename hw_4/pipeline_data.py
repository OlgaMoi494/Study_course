from data.array_data import task_lst
from modules.data_handling import quick_sort, odd_numbers, odd_indexes, write_data


sorted_lst = quick_sort(task_lst)

write_data(sorted_lst, odd_numbers(sorted_lst), odd_indexes(sorted_lst))
