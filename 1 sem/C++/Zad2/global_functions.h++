#ifndef GLOBAL_FUNCTIONS_HPP
#define GLOBAL_FUNCTIONS_HPP
#include <iostream>
#include <cmath>
#include "classes.h++"

double factor_a(Odcinek a);

bool if_Segment_perpendicular(Odcinek a, Odcinek b);

bool if_Segment_equally(Odcinek a, Odcinek b);

bool if_seprate_Tri(Trojkat a, Trojkat b);

bool if_contain_Tri(Trojkat a, Trojkat b);

double distance(Punkt a, Punkt b);

double pole_global(Punkt a, Punkt b, Punkt c);

#endif
