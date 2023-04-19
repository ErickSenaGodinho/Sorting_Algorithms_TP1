import re
import sort_algorithms
import sorting_data


def main(debug_mode=False):
    sort_algorithm, array, type_, size = menu()
    sort_algorithm_name, time, comp, swaps = sort(sort_algorithm, array)
    time = time.total_seconds()
    print("Time: {}s".format(time))
    print("Comp:", comp)
    print("Swaps:", swaps)
    sorting_data.save_data(sort_algorithm_name, type_, size, time, comp, swaps)

    if debug_mode:
        sorted_ = True
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                sorted_ = False
        print(array)
        print(sorted_)


def menu():
    sort_algorithm = sort_menu()
    file_path = "./instances_pt_br/"
    file_name = file_menu()

    match_obj = re.search("Dicionario", file_name)
    is_text = match_obj is not None
    size = re.search("\d+", file_name).group(0)
    type_ = re.search("^([^\W\d]+)", file_name).group(0)

    array = load_file(file_path + file_name, is_text)
    return sort_algorithm, array, type_, size


def sort_menu():
    while True:
        print("Escolha o método de ordenação:\n")
        print("1-Bubble Sort")
        print("2-Shell Sort")
        print("3-Selection Sort")
        print("4-Insertion Sort")
        print("5-Quick Sort")
        print("6-Merge Sort")
        answer = (int)(input())
        if answer > 0 and answer < 7:
            break
    return answer


def file_menu():
    while True:
        print("Escolha o tipo do arquivo:\n")
        print("1-Aleatório")
        print("2-Ordenado")
        print("3-Quase Ordenado")
        print("4-Inversamente Ordenado")
        file_type = (int)(input())
        if file_type > 0 and file_type < 5:
            break
    return select_file_menu(file_type)


def select_file_menu(file_type):
    while True:
        if file_type == 1:
            files = {
                1: "DicionarioAleatorio-261791.txt",
                2: "DicionarioAleatorio-29855.txt",
                3: "ListaAleatoria-1000.txt",
                4: "ListaAleatoria-10000.txt",
                5: "ListaAleatoria-100000.txt",
                6: "ListaAleatoria-1000000.txt",
            }
        elif file_type == 2:
            files = {
                1: "DicionarioOrdenado-261791.txt",
                2: "DicionarioOrdenado-29855.txt",
                3: "ListaOrdenada-1000.txt",
                4: "ListaOrdenada-10000.txt",
                5: "ListaOrdenada-100000.txt",
                6: "ListaOrdenada-1000000.txt",
            }
        elif file_type == 3:
            files = {
                1: "ListaQuaseOrdenada-1000.txt",
                2: "ListaQuaseOrdenada-10000.txt",
                3: "ListaQuaseOrdenada-100000.txt",
                4: "ListaQuaseOrdenada-1000000.txt",
            }
        elif file_type == 4:
            files = {
                1: "DicionarioInversamenteOrdenado-261791.txt",
                2: "DicionarioInversamenteOrdenado-29855.txt",
                3: "ListaInversamenteOrdenada-1000.txt",
                4: "ListaInversamenteOrdenada-10000.txt",
                5: "ListaInversamenteOrdenada-100000.txt",
                6: "ListaInversamenteOrdenada-1000000.txt",
            }
        if file_type > 0 and file_type <= len(files):
            break
    for key, file_name in files.items():
        print(key, "-", file_name)

    key = (int)(input())
    return files.get(key)


def load_file(file_name, is_text):
    file_ = open(file_name, encoding="utf8").read().splitlines()
    array_lines = []
    for line in file_:
        value = line if is_text else (int)(line)
        array_lines.append(value)
    return array_lines


def sort(sort_algorithm, array):
    print("sorting...")
    if sort_algorithm == 1:
        time, comp, swaps = sort_algorithms.bubble_sort(array)
        sort_algorithm_name = "Bubble Sort"
    elif sort_algorithm == 2:
        time, comp, swaps = sort_algorithms.shell_sort(array)
        sort_algorithm_name = "Shell Sort"
    elif sort_algorithm == 3:
        time, comp, swaps = sort_algorithms.selection_sort(array)
        sort_algorithm_name = "Selection Sort"
    elif sort_algorithm == 4:
        time, comp, swaps = sort_algorithms.insertion_sort(array)
        sort_algorithm_name = "Insertion Sort"
    elif sort_algorithm == 5:
        time, comp, swaps = sort_algorithms.quick_sort(array)
        sort_algorithm_name = "Quick Sort"
    elif sort_algorithm == 6:
        time, comp, swaps = sort_algorithms.merge_sort(array)
        sort_algorithm_name = "Merge Sort"
    return sort_algorithm_name, time, comp, swaps


main(debug_mode=True)
