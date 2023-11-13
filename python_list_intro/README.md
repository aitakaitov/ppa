# Intro do Python listů (a funkcí)

## Listy

### Inicializace
Obojí je možné

```
my_list = []

my_list = [0, 1, 2, 3]

my_list = list()
```

<code>list()</code> lze použít i pro přetypování kolekce na list, např.
```
> my_list = list(range(10))

> print(my_list) 

> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

Iterování přes list pomocí indexu
```
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(len(my_list)):
    print(my_list[i])
```

Iterování přes prvky listu (for each)
```
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for value in my_list:
    print(value)
```

List comprehensions - vložením for cyklu do listu vygenerujeme hodnoty listu 
```
> my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

> my_list_times_two = [value * 2 for value in my_list]

> print(my_list_times_two)

> [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
```

Built-in operace pro listy - <code>min</code>, <code>max</code>
```
> my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

> print(max(my_list))

> 9

> print(min(my_list))

> 0
```

## Funkce

Definice funkce přes hlavičku a tělo, definice typu parametrů a návratových hodnot
```
def func(param1: type, param2: type) -> type:
    ...
```

Vrácení více návratových hodnot - tuple
```
def func() -> tuple[str, str]:
    return 'string1', 'string2'

value1, value2 = func() 
print(value1)   # 'string1'
print(value2)   # 'string2'

```

Výchozí hodnoty parametrů, předávání pojmenovaných parametrů
```
def randn(mean: float = 0, stdev: float = 1) -> float:
    random_number = ...
    # kód vynegeruje náhodnou hodnotu z normálního rozdělení s předanou st5edn9 hodnotou a směrodatnou odchylkou
    return random_number

# vrátí číslo z rozdělení s mean = 0 a stdev = 1
random_number = randn() 

# vrátí číslo z rozdělení s mean = 10 a stdev = 5 
random_number = randn(10, 5)

# vrátí číslo z rozdělení s mean = 10 a stdev = 5
# pokud při predávání hodnoty řekneme pro jaký parametr, nezáleží na pořadí
random_number = randn(mean=10, stdev=5)
random_number = randn(stdev=5, mean=10)

# nepojmenované parametry (ty závislé na pozici) je potřeba specifikovat před pojmenovanými
# vrátí číslo z rozdělení s mean = 10 a stdev = 5 
random_number = randn(10, stdev=5)

# SyntaxError: positional argument follows keyword argument
random_number = randn(mean=10, 5)
```

Komentáře k funkcím
```
def func(param1: int) -> float:
    """
    Ukázkový komentář

    Param:
        param1: první parametr

    Returns:
        návratová hodnota
    """
```

# Příklady

## Funkce na generování polí
```
# načte z klávesnice pole zadané délky a vrátí jej
def input_array(n: int) -> list[int]:
    ...

# vygeneruje pole zadané délky, naplněné hodnotami od first s krokem step
def generate_range(n: int, first: int, step: int) -> list[int]:
    ...

# vygeneruje pole zadané délky naplněné náhodnými čísly z intervalu <min, max>
def generate_random_array(n: int, min: int, max: int) -> list[int]:
    ...
```

## Histogram
Historam zjednodušíme - pokud je počet výskytů 0, tak hodnotu do histogramu nezahrneme. 
Histogram klasicky obsahuje sloupec i pro hodnoty co se v datech nevyskytují.
```
def get_values_counts(data: list[int]) -> tuple[list[int], list[int]]:
    """
    Najde všechny unikátní hodnoty z listu data,
    pro každou unikátní hodnotu spočte počet výskytů.

    List values musí být vzestupně seřazený. 

    Pro hodnotu na indexu i v poli values musí být v poli counts na indexu i odpovídající hodnota. 

    Př.:    
    data = [1, 2, 3, 1, 2, 1, 3]
    values = [1, 2, 3]
    counts = [3, 2, 2]
    return values, counts
    """
    ...


def ints_to_strings(ints: list[int]) -> list[str]:
    """
    Převede list intů na list odpovídajících stringů
    
    Př.:
    ints = [-1, 0, 1, 2, 3]
    strings = ints_to_strings(ints)
    print(strings)
    > ['-1', '0', '1', '2', '3']
    """


def print_line_chart(labels: list[str], values: list[int]):
    """
    Vypíše na konzoli graf, kde pro každou hodnotu z listu labels a její odpovídající hodnotu z listu values 
    bude jeden řádek ve formátu

    <label> <█ x value>

    tedy pokud label='5' a value=4, řádek bude

    5 ████

    Labels musí být zarovnané doprava.

    Př.:
    labels = ['3', '8', '14']
    values = [3, 8, 14]
    print_line_chart(labels, values)
    >  3 ███
    >  8 ████████
    > 14 ███████████
    """
    ...


def print_bar_chart(labels: list[str], values: list[int]):
    """
    Vypíše na konzoli sloupcový graf, kde pro každou hodnotu z listu labels a její odpovídající hodnotu z listu values 
    bude jeden sloupec.

    Labels (popisky sloupců) musí být zarovnané, resp. každý sloupec musí mít stejnou šířku

    Př.:
    labels = ['3', '8', '14']
    values = [3, 8, 14]
    print_bar_chart(labels, values)

          █
          █
          █
          █
          █
          █
       █  █
       █  █
       █  █
       █  █
       █  █
    █  █  █
    █  █  █
    █  █  █
    3  8  14 
    """
    ...


# vynegerujte pole hodnot
data = generate_random_array(n=100, min=0, max=20)
unique_values, counts = get_values_counts(data)
labels = ints_to_strings(unique_values)

print_line_chart(labels=labels, values=counts)
print_bar_chart(labels=labels, values=values)
```

## Histogram pomocí matplotlib

Do terminálu zadat

<code>pip install matplotlib</code>

v kódu

```
import matplotlib.pyplot as plt

data = generate_random_array(n=100, min=0, max=20)

# bins specifikuje kolik binů se použije
# bin je interval, počty výskytů se počítají pro biny
# pokud hodnota spadá do intervalu binu, počet pro daný bin se inkrementuje
plt.hist(x=data, bins=100)
plt.show()

# alternativně, pokud chceme zobrazit počty výskytů jednotlivých hodnot, 
# můžeme nastavit počet binů na počet unikátních hodnot
values, counts = get_values_counts(data)
plt.hist(x=data, bins=len(values))
plt.show()
```