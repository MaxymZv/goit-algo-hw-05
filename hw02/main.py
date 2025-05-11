from typing import Callable, Generator


def generator_numbers(text: str) -> Generator[float, None, None]: #Creating function to generate float from str
    for word in text.split():                                     #Spliting text 
        try:                                                      #Trying to yield float
            yield float(word)
        except ValueError:                                        #If we have ValueError we continue
            continue


def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]): #Creating function to sum numbers from text
    return sum(func(text))                                                      #Returning sum from function with text

text = 'Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів.'

total_income = sum_profit(text, generator_numbers)

print(total_income)

