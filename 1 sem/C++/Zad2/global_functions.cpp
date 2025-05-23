#include "global_functions.h++"
#include <iostream>
#include <cmath>

double factor_a(Odcinek a)
{
    Punkt a1 = a.get_PointA();
    Punkt a2 = a.get_PointB();
    double wspolczynnik_a = (a2.getY() - a1.getY()) / (a2.getX() - a1.getX());
    return wspolczynnik_a;
}

bool if_Segment_perpendicular(Odcinek a, Odcinek b)
{
    double wspolczynnik_a = factor_a(a);
    double wspolczynnik_b = factor_a(b);
    if (wspolczynnik_a * wspolczynnik_b == -1) return true;
    else return false;
}

bool if_Segment_equally(Odcinek a, Odcinek b)
{
    double wspolczynnik_a = factor_a(a);
    double wspolczynnik_b = factor_a(b);
    if (wspolczynnik_a == wspolczynnik_b) return true;
    else return false;
}

bool if_seprate_Tri(Trojkat a, Trojkat b)
{
    if (a.point_in_Tri(b.get_PointA_Tri()) or a.point_in_Tri(b.get_PointB_Tri()) or a.point_in_Tri(b.get_PointC_Tri())) return false;
    else if (b.point_in_Tri(a.get_PointA_Tri()) or b.point_in_Tri(a.get_PointB_Tri()) or b.point_in_Tri(a.get_PointC_Tri())) return false;
    else return true;
}

bool if_contain_Tri(Trojkat a, Trojkat b)
{
    if (a.point_in_Tri(b.get_PointA_Tri()) and a.point_in_Tri(b.get_PointB_Tri()) and a.point_in_Tri(b.get_PointC_Tri())) return true;
    else if (b.point_in_Tri(a.get_PointA_Tri()) and b.point_in_Tri(a.get_PointB_Tri()) and b.point_in_Tri(a.get_PointC_Tri())) return true;
    else return false;
}

double distance(Punkt a, Punkt b)
{
    return sqrt( pow(abs(a.getX() - b.getX()), 2) + pow(abs(a.getY() - b.getY()), 2));
}

double pole_global(Punkt a, Punkt b, Punkt c)
{
    return (abs((b.getX() - a.getX()) * (c.getY() - a.getY()) - (b.getY() - a.getY()) * (c.getX() - a.getX())))/2;
}

