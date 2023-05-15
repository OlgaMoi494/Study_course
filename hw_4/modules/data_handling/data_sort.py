def quick_sort(lst_for_sorting: list) -> list:
    if len(lst_for_sorting) < 2:
        return lst_for_sorting
    
    dividing_point = lst_for_sorting[0]
    gt_lst = []
    lt_lst = []

    for number in lst_for_sorting[1:]:
        if number <= dividing_point:
            lt_lst.append(number)
        else:
            gt_lst.append(number)

    return  quick_sort(lt_lst) + [dividing_point] + quick_sort(gt_lst)


def odd_numbers(sorted_lst: list) -> list:
    return [element for element in sorted_lst if element % 2 != 0]


def odd_indexes(sorted_lst: list) -> list:
    return [element for index, element in enumerate(sorted_lst) if index % 2 != 0]


def write_data(sorted_lst:list, odd_numbers_lst: list, odd_indexes_lst: list) -> None:
    with open('results/array_processed.txt', 'w',  encoding='utf-8') as wr_file:
        wr_file.write("Sorted list: \n")
        wr_file.write(str(sorted_lst))
        wr_file.write("\n\nFunction 2. Odd numbers list: \n")
        wr_file.write(str(odd_numbers_lst))
        wr_file.write("\n\nFunction 3. Odd indexes list: \n")
        wr_file.write(str(odd_indexes_lst))
