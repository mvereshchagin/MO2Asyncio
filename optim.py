from dataclasses import dataclass, field, asdict
from datetime import date
from pympler import asizeof
import time

def sizeof_fmt(num, suffix="B"):
    for unit in ["", "Ki", "Mi", "Gi", "Ti", "Pi", "Ei", "Zi"]:
        if abs(num) < 1024.0:
            return f"{num:3.1f}{unit}{suffix}"
        num /= 1024.0
    return f"{num:.1f}Yi{suffix}"


def main():
    alexey = Person(name='Алексей', surname='Парахин')
    # print(asdict(alexey))

    alexey.gender = 'мужской'

    # start = time.time()
    # persons = []
    # for i in range(1000 * 1000):
    #     persons.append(Person(name='name_' + str(i), surname=f'surname_' + str(i)))
    # print(f"Size of persons: {sizeof_fmt(asizeof.asizeof(persons))}, time: {time.time() - start}")

    name = 'Vasya'
    surname = 'Ivanov'
    my_string = f'Hello, {name} {surname}'

    # start = time.time()
    # res = []
    # step = 10
    # for i in range(10000 * 10000):
    #     res.append(step * i)
    # print(f"time 1: {time.time() - start}")
    #
    # start = time.time()
    # res = []
    # cur_value = 0
    # step = 10
    # for i in range(10000 * 10000):
    #     res.append(cur_value)
    #     cur_value = cur_value + step
    # print(f"time 2: {time.time() - start}")

    a, b, c = 1, 2, 3
    start = time.time()
    x = 0
    for i in range(1000 * 1000 * 10):
        x += a * i * i + b * i + c
    print(f"x = {x}; time 1: {time.time() - start}")

    # optimization through induction
    start = time.time()
    p = a + b
    x = c
    res = x
    for i in range(1, 1000 * 1000 * 10):
        x = x + p
        p = p + 2 * a
        res += x
    print(f"x = {res}; time 2: {time.time() - start}")

    # start = time.time()
    # persons = [Person(name=f'name_{i}', surname=f'surname_{i}') for i in range(1000 * 1000)]
    # print(f"Size of persons 2: {sizeof_fmt(asizeof.asizeof(persons))}, time: {time.time() - start}")

    print("Size of alexey:", asizeof.asizeof(alexey))

    vasily = Person2(name='Василий', surname='Уткин')
    print("Size of vasily:", asizeof.asizeof(vasily))


    # dariya = Person(name='Дарья', surname='Казакова', gender='Женский',
    #                 date_of_birth=date(1999, 6, 16))
    #
    # print("Size of dariya:", asizeof.asizeof(dariya))
    #
    # if alexey == dariya:
    #     print('They are the same person')
    # else:
    #     print('They are two different people')



# @dataclass(eq=False)
class Person:
    # region props
    __name: str
    __surname: str
    __gender: str
    email: str = field(init=False, repr=False, default=None)
    phone: str = field(init=False, repr=False, default=None)
    # endregion

    __slots__ = ('__name', '__surname', '__gender')

    def __init__(self, name: str, surname: str, gender: str = 'Мужской'):
        self.__name = name
        self.__surname = surname
        self.__gender = gender

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

    @property
    def gender(self) -> str:
        return self.__gender

    @gender.setter
    def gender(self, gender: str) -> None:
        self.__gender = gender

@dataclass
class Person2:
    name: str
    surname: str
    # gender: str = field(init=False, repr=False, default='Женский')

    __slots__ = ('name', 'surname')


if __name__ == '__main__':
    main()