# Intro do Python listů (a funkcí)

## Listy

### Inicializace
Obojí je možné

```python
my_list = []

my_list = [0, 1, 2, 3]

my_list = list()
```

<code>list()</code> lze použít i pro přetypování kolekce na list, např.
```python
my_list = list(range(10))

print(my_list) 
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

Iterování přes list pomocí indexu
```python
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(len(my_list)):
    print(my_list[i])
```

Iterování přes prvky listu (for each)
```python
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for value in my_list:
    print(value)
```

List comprehensions - vložením for cyklu do listu vygenerujeme hodnoty listu 
```python
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

my_list_times_two = [value * 2 for value in my_list]

print(my_list_times_two)
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
```

Built-in operace pro listy - <code>min</code>, <code>max</code>
```python
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(max(my_list))
# 9

print(min(my_list))
# 0
```

## Funkce

Definice funkce přes hlavičku a tělo, definice typu parametrů a návratových hodnot
```python
def func(param1: type, param2: type) -> type:
    ...
```

Vrácení více návratových hodnot - tuple
```python
def func() -> tuple[str, str]:
    return 'string1', 'string2'

value1, value2 = func() 
print(value1)   
# 'string1'
print(value2)   
# 'string2'
```

Výchozí hodnoty parametrů, předávání pojmenovaných parametrů
```python
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
```python
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
```python
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
```python
def get_values_counts(data: list[int]) -> tuple[list[int], list[int]]:
    """
    Připraví data pro histogram. Z listu hodnot vytvoří dva listy
    list values, který bude obsahovat hodnoty
    list counts, který bude obsahovat počty výskytů hodnot v listu data

    Pokud se hodnota v seznamu nevyskytuje, bude mít počet výskytů 0
    List values by tedy měl obsahovat všechny hodnoty v intervalu <min(data), max(data)> 

    Př.:    
    data = [1, 2, 3, 1, 2, 1, 3, 5]
    values = [1, 2, 3, 4, 5]
    counts = [3, 2, 2, 0, 1]
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

```python
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

# Něco málo navíc

## <code>list</code> vs <code>tuple</code>

<code>list</code> lze modifikovat, <code>tuple</code> ne. <code>tuple</code> je n2kdy rychlej39

```python
t = tuple(1, 2, 3)

# ekvivalentní
t = (1, 2, 3)

# TypeError: 'tuple' object does not support item assignment
t[0] = 10
```

## <code>dictionary</code>

<code>dictionary</code> je slovník s páry <code>key, value</code>.

```python
d = dict()

# ekvivalentní
d = {}

# s počátečními hodnotami
d = {'key1': 'value1', ...}

# přiřazení
d['some_key'] = 'some_value'

# kontrola jestli je klíč ve slovníku
if 'some_key' in d.keys():
    ...

# získání klíčů
keys = d.keys()

# získání hodnot
values = d.values()

# získání dvojic klíč, hodnota
# v podstatě kolekce tuples (key1, value1), (key2, value2), ...
items = d.items()
for key, value in items:
    ...

# ekvivalent
for key, value in zip(d.keys(), d.values()):
    ...

# ekvivalent
# dict.keys a dict.values nejsou indexovatelné, takže d.keys()[i] vyhodí chybu
keys = list(d.keys())
values = list(d.values())
for i in range(len(keys)):
    key = keys[i]
    value = values[i]
```

