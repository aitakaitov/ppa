import random
import matplotlib.pyplot as plt
   

def generate_random_array(n: int, min: int, max: int) -> list[int]:
    values = []
    for i in range(n):
        values.append(random.randint(min, max))
    
    return values
    # jednořádková alternativa
    # return [random.randint(min, max) for _ in range(n)]


def input_array(n: int) -> list[int]:
    values = []
    for _ in range(n):
        while True:
            try:
                # input načte string ze vstupu
                in_str = input('zadejte cislo: ')
                
                # pokud nelze převést string a int, vyhodí výjimku - jsme v try bloku, takže se výjimka zachytí
                val = int(in_str)

                # pokud dostaneme validní vstup, přidáme číslo do listu a ukončíme while cyklus
                values.append(val)
                break
            except Exception:
                # pokud dojde k výjimce, vypíšeme zprávu a zkoušíme znova
                print('nebylo zadano cislo')

    return values


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

    # najdeme rozsah
    data_min = min(data)
    data_max = max(data)

    values = []
    # vynegerujeme všechny celočíselné hodnoty z intervalu
    for i in range(data_min, data_max + 1):
        values.append(i)

    # jednořádková alternativa
    # values = [i for i in range(data_min, data_max + 1)]
    
    # pro každou hodnotu začínáme s 0 výskyty
    counts = []
    for i in range(len(values)):
        counts.append(0)

    # jednořádková alternativa
    # counts = [0 for i in range(len(values))]

    # trocha chytré matematiky
    # pokud interval je <-5, 5>, hodnota -4 půjde na index i = -4 - (-5) = 1
    for value in data:
        counts[value - data_min] += 1
    
    return values, counts


def ints_to_strings(ints: list[int]) -> list[str]:
    """
    Převede list intů na list odpovídajících stringů
    
    Př.:
    ints = [-1, 0, 1, 2, 3]
    strings = ints_to_strings(ints)
    print(strings)
    > ['-1', '0', '1', '2', '3']
    """
    # alternativně
    # strings = [str(i) for i in ints]
    strings = []
    for i in ints:
        strings.append(str(i))
    
    return strings    
    # alternativně, jednořádkově
    # return [str(i) for i in ints]



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
    # potřebujeme zjistit jak široký musí být sloupec
    max_width = 0
    for label in labels:
        if len(label) > max_width:
            max_width = len(label)

    # jednořádková alternativa
    # max_width = max([len(l) for l in labels])

    # jeden label pro každý řádek
    for i in range(len(labels)):
        # buffer pro řádek
        buffer = ''
        label = labels[i]
        value = values[i]
        
        # zarovnání zleva na maximální délku sloupce pro labels
        for padding in range(len(label), max_width):
            buffer += ' '
        
        # přidáme label a mezeru
        buffer += label + ' '

        # alternativně lze použít formátování celých čísel (pokud jsou labely celá čísla)
        # buffer += f'{label:label_column_width}' 
        # což udělá padding zleva

        # vypíšeme bloky
        for block in range(value):
            buffer += '█'

        # alternativně
        # buffer += '█' * value
        
        print(buffer)


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
    # vypisujeme odshora řádek po řádku
    # potřebujeme tedy vědět jak vysoký graf bude
    chart_height = max(values)

    # potřebujeme zjistit jak široký musí být sloupec
    max_width = 0
    for label in labels:
        if len(label) > max_width:
            max_width = len(label)

    # jednořádková alternativa
    # max_width = max([len(l) for l in labels])

    # přidáme +1 aby yly sloupce oddělené
    max_width += 1

    # nejprve vykreslíme sloupce řádek po řádku odshora dolů
    for row in range(chart_height, 0, -1):
        buffer = ''
        # pro každý rádek musíme zkontrolovat jestli pro daný sloupec máme vykreslit hodnotu nebo ne
        for l in values:
            # pokud ano, přidáme blok, jinak necháme mezeru
            if l >= row:
                buffer += '█'
            else:
                buffer += ' '
            # sloupec musíme doplnit o padding do šířky sloupce
            for _ in range(1, max_width):
                buffer += ' '
        # řádek vykreslíme
        print(buffer)

    # máme vykreslený sloupce, teď potřebujeme labely pod sloupci
    buffer = ''
    # mechanismus je obdobný - vykreslíme label, přidáme padding do šířky sloupce
    for label in labels:
        buffer += label
        for _ in range(len(label), max_width):
            buffer += ' '
    print(buffer)


if __name__ == '__main__':
    data = generate_random_array(10, -5, 5)
    values, counts = get_values_counts(data)
    labels = ints_to_strings(values)

    print_line_chart(labels=labels, values=counts)
    print('\n\n')
    print_bar_chart(labels=labels, values=counts)

    # --- pomocí matplotlibu ---
    # bins specifikuje kolik binů se použije
    # bin je interval, počty výskytů se počítají pro biny
    # pokud hodnota spadá do intervalu binu, počet pro daný bin se inkrementuje
    # můžeme udělat tolik binů kolik je unikátních hodnot
    plt.hist(x=data, bins=10)
    plt.show()

    plt.hist(x=data, bins=len(list(set(data))))
    plt.show()