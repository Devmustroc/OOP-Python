from typing import Union, Optional, Tuple, List, Callable

def test_function(a: int) -> int: # type hinting
    return a  # return type


def test_print(a: str) -> None:  # type hinting
    print(a)  # return type


def test_print2(a: float) -> None:  # type hinting
    print(a)  # return type


def test_print3(a: tuple) -> None:  # type hinting
    print(a)  # return type


def division(a: int, b: Optional[int]) -> Union[int, Optional[float]]:
    if b is None: # check if b is None
        return a   # return type
    if b != 0:  # check if b is not 0
        return a / b  # return type
    return 1    # return 1 if b is 0


def test_unpack(input_val: list[str], index: int) -> Tuple[str, int]:
    return (input_val[index], index)  # return tuple


def test_unpack1(input_val: list[str], index: int) -> List[str]:
    return [input_val[index], index]  # return list


return_val = test_function(1)  # return type
# print(return_val) # print return type

# test_print("testing string to print")  # print string

# test_print2(1.1)  # print float

# test_print3(("1", 2, 3))  # print tuple

# print(division(3, 0))  # print division by 0
# print(division(3, 2))  # print division by 2

return_val = test_unpack(["val_1", "val2", "val3"], 2)  # unpack list
print(return_val)

return_val = test_unpack1(["val_1", "val2", "val3"], 2)  # unpack list
print(return_val)  # print unpacked list