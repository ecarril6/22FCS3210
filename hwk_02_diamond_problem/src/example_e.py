'''
 * CS3210 - Principles of Programming Languages - Fall 2022
 * Instructor: Thyago Mota
 * Student: Emily Carrillo-Ramirez
 * Description: Homework 02 - Diamond Problem
'''

class Device: 

    def __init__(self, manufacturer) -> None:
        self.manufacturer = manufacturer
        print('Device Constructor')

    def __str__(self) -> str:
        return self.manufacturer

class Printer(Device): 

    def __init__(self, manufacturer, type) -> None:
        self.type = type
        super().__init__(self, manufacturer)        
        print('Printer constructor')

    def __str__(self) -> str:
        return f'{self.type}'

class Scanner(Device): 

    def __init__(self, manufacturer, dpi) -> None:
        super().__init__(manufacturer) 
        self.dpi = dpi
        print('Scanner constructor')

    def __str__(self) -> str:
        return f'{self.dpi}'

class MultifunctionPrinter(Printer, Scanner): 

    def __init__(self, manufacturer, type, dpi) -> None:
        Printer.__init__(self, manufacturer, type)
        Scanner.__init__(self, manufacturer, dpi)

    def __str__(self) -> str:
        return f'{self.manufacturer,self.type, self.dpi}'

if __name__ == '__main__':
    ts6300 = MultifunctionPrinter("Canon", "Inkjet", "600")
    print(ts6300)
