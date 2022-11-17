/*
 * CS3210 - Principles of Programming Languages - Fall 2022
 * Instructor: Thyago Mota
 * Student: Emily Carrillo-Ramirez
 * Description: Homework 02 - Diamond Problem
 */

#include <iostream>
#include <string>

using namespace std;

class Device {
    protected: 
        string manufacturer;
    
    public:
        Device(string manufacturer) {
            //cout << "Class Device constructore called"<< endl;
            this->manufacturer = manufacturer;
        }
        
        string getString(){
            return manufacturer;
        }
        friend ostream& operator<<(ostream&, const Device&);
};

ostream& operator<<(ostream& os, const Device& device)
{
    os << device.manufacturer;
    return os;
}

class Printer: virtual public Device {
    
    protected:    
        string type;
        
    public: 
        Printer(string manufacturer, string type): Device(manufacturer) {
            //cout << "Class Printer constructor called"<< endl;
            this->type = type;
        }
        
        friend ostream& operator<<(ostream&, const Printer&);
};

ostream& operator<<(ostream& os, const Printer& printer)
{
    os << printer.manufacturer << ", " << printer.type;
    return os;
}

class Scanner: virtual public Device {
    
    protected:    
        string dpi;
        
    public: 
        Scanner(string manufacturer, string dpi): Device(manufacturer) {
            //cout << "Class Scanner constructor called"<< endl;
            this->dpi = dpi;
        }
        
        
        friend ostream& operator<<(ostream&, const Scanner&);
};

ostream& operator<<(ostream& os, const Scanner& scanner)
{
    os << scanner.manufacturer << ", " << scanner.dpi;
    return os;
}

class MultifunctionPrinter: public Printer, public Scanner {
        
    public: 
        MultifunctionPrinter(string manufacturer, string type, string dpi): Printer(manufacturer, type), Scanner(manufacturer, dpi), Device(manufacturer){
            //cout << "Class MP constructor called"<< endl;
        }
        
        friend ostream& operator<<(ostream&, const MultifunctionPrinter&);
};

ostream& operator<<(ostream& os, const MultifunctionPrinter& multifunctionPrinter)
{
    os << multifunctionPrinter.manufacturer << ", " << multifunctionPrinter.type << ", " << multifunctionPrinter.dpi;
    return os;
}

int main() {
    MultifunctionPrinter ts6300("Canon", "Inkjet", "600");
    std::cout << ts6300;

    return 0;
}
