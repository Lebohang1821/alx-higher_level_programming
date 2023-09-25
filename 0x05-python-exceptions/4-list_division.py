#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    """It divides two lists element by element.

    Args:
        my_list_1 (list): First list.
        my_list_2 (list): Second list.
        list_length (int): Number of elements to divide.

    Returns:
        New list of length list_length containing all the divisions.
    """
    _list = []
    for i in range(0, list_length):
        try:
            if i < len(my_list_1) and i < len(my_list_2):
                elem_1 = my_list_1[i]
                elem_2 = my_list_2[i]
                
                if isinstance(elem_1, (int, float)) and isinstance(elem_2, (int, float)):
                    if elem_2 != 0:
                        div = elem_1 / elem_2
                    else:
                        div = 0
                        print("division by 0")
                else:
                    div = 0
                    print("wrong type")
            else:
                div = 0
                print("out of range")
        except Exception as e:
            div = 0
            print("An unexpected error occurred:", e)
        finally:
            _list.append(div)
    return (_list)
