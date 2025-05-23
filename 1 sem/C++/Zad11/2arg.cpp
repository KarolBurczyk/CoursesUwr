#include "2arg.h++"
#include <cmath>

Bin::Bin(string x)
    :Operator(x)
{}

Add::Add()
    :Bin("+")
{}

Sub::Sub()
    :Bin("-")
{}

Mult::Mult()
        :Bin("*")
{}

Div::Div()
        :Bin("/")
{}

Mod::Mod()
        :Bin("%")
{}

Min::Min()
        :Bin("min")
{}

Max::Max()
        :Bin("max")
{}

Log::Log()
        :Bin("log")
{}

Pow::Pow()
        :Bin("pow")
{}


