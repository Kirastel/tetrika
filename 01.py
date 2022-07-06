def task_1(array: str) -> int:
    search_element = array.find('0')
    return search_element


def task_2(array: str) -> int:
    return array.index('0')


def task_3(array: str) -> int:
    return eval('+'.join(array))


