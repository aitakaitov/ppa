# Soubory

## Line endings

Znaky pro ukončení řádky
* <code>\n</code>, aka LF (line feed)
* <code>\r</code>, aka CR (carriage return)

V Linuxu jsou řádky ukončeny znakem <code>\n</code>. We Windows sekvencí <code>\r\n</code>.

## Statické metody

Statické metody 
* nevyžadují instanci třídy aby bylo možné je zavolat
* mohou být zavolány i pomocí instance (v Pythonu)
* nemají jako první parametr <code>self</code>
* musí mít anotaci <code>@staticmethod</code>
* statické metody mohou volat pouze jiné statické metody třídy

```python
class SomeClass:
    def __init__(self):
        self.something = 'something'

    def non_static_method(self):
        print('non static method')

    @staticmethod
    def static_method():
        print('static method')

some_class = SomeClass()

# OK
some_class.non_static_method()

# OK
some_class.static_method()

# Error
SomeClass.non_static_method()

# OK
SomeClass.static_method()
```

## Otevření a zavření souborů

Metoda <code>open()</code> vrátí objekt reprezentující soubor - <code>_io.TextIOWrapper</code>. Má tři podstatné parametry:
* cesta k souboru
* mód
  * <code>"r"</code> - pouze čtení
  * <code>"w"</code> - pouze zápis
  * <code>"w+"</code> - zápis + vytvoření
  * <code>"a"</code> - zápis na konec souboru
  * <code>"rb", "wb", "wb+", "ab"</code> - binární verze, nezapisují se znaky, ale byty
* <code>encoding</code>
  * <code>"utf-8"</code> by default v Linuxu
  * <code>"cp1252"</code> by default ve Windows

```python
f = open("some_file.txt", "r", encoding="utf-8")

# False
f.closed
```

Otevřený soubor je potřeba zavřít, pokud už ho nepotřebujeme

```python
f.close()

# True
f.closed
```

Je ale lepší způsob jak alokovat a uvolňovat zdroje - kontext <code>with</code>. <code>with</code> je kontrukce v Pythonu, která mimo jiné umožňuje monitorovat operace, provedené v kontextu, ale také zajistí uvolnění zdrojů za nás.

```python
with open("some_file.txt", "r", encoding="utf-8") as f:
    # do something with file
    text = f.read()

# (now file is freed - f.close() was called when we exited the context)

# True
f.closed
```

## Čtení souboru

Přečtení celého souboru - metoda <code>read()</code>, vrací string
```python
with open("some_file.txt", "r", encoding="utf-8") as f:
    text = f.read()
```

Přečtení řádky - metoda <code>readline()</code>
```python
with open("some_file.txt", "r", encoding="utf-8") as f:
    line = f.readline()
```

Přečtení všech řádek
```python
with open("some_file.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
```

## Zápis do souboru

Metoda <code>write()</code>
```python
with open("some_file.txt", "w+", encoding="utf-8") as f:
    # write won't insert a newline, so we need to insert it ourselves
    f.write("Some text...\n")
```

Metoda <code>writelines()</code> - zapíše seznam stringů do souboru, každý string jako jednu řádku. Automaticky přidá konce řádek.

```python
lines = ["line1", "line2"]
with open("some_file.txt", "w+", encoding="utf-8") as f:
    f.writelines(lines)
```

## *(Pozice v souboru)*
Objekt souboru je spojený s pozicí v souboru - odkud čteme, resp. kam zapisujeme. V `r`, `w`, `w+` módech je pozice nastavena na `0` - začátek souboru.

S pozicí lze iteragovat pomocí metod
* `tell() -> int` - vrátí pozici v souboru
* `seek(int)` - nastaví pozici v souboru
* ``

## Souborový systém

To aktuálně podstatné je v knihovně `os` *(užitečné věci jsou také v knihovně `shutil`)*.

Získání seznamu souborů a složek v adresáři - funkce `os.listdir("...")`

```python
import os

# returns a list of strings - no parameter means current working directory
dirs = os.listdir()

# Lists directories in the C drive root
c_dirs = os.listdir("C:/")
```

`os.path.join()` - umožňuje vytvořit cestu ze stringů. Bere v potaz platformu. Může být hezčí než `p1 + '/' + p2 + ...`

`os.path.join()` má neomezený počet parametrů
```python
import os

# accepts an arbitrary number of parameters
# returns "part1/part2/part3/part4" Path object - not a string
p = os.path.join("part1", "part2", "part3", "part4")

# can be directly used in open()
with open(p, "w+", encoding="utf-8") as f:
    ...
```