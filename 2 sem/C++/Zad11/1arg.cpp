#include "1arg.h++"
#include <cmath>

Un::Un(string x) : Operator(x)
{}
Abs::Abs()
    :Un("abs")
{}

Sgn::Sgn()
        :Un("sgn")
{}

Floor::Floor()
        :Un("floor")
{}

Ceil::Ceil()
        :Un("ceil")
{}

Frac::Frac()
        :Un("frac")
{}

Sin::Sin()
        :Un("sin")
{}

Cos::Cos()
        :Un("cos")
{}

Atan::Atan()
        :Un("atan")
{}

Acot::Acot()
        :Un("acot")
{}

Ln::Ln()
        :Un("ln")
{}

Exp::Exp()
        :Un("exp")
{}