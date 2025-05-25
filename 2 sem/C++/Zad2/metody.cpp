#include "classes.h++"
using namespace std;

Wektor::Wektor()
{
    x = 0;
    y = 0;
}

double Wektor::get_vector_X()  { return x; }

double Wektor::get_vector_Y()  { return y; }

void Wektor::set_Vector(double a, double b)  { x = a; y = b; }

Punkt::Punkt()
{
    x = 0;
    y = 0;
}

double Punkt::getX()  { return x; }

double Punkt::getY()  { return y; }

void Punkt::copy_Point(Punkt a) { x = a.getX(); y = a.getY(); }

void Punkt::set_Point(double a, double b)  { x = a; y = b; }

void Punkt::move_Point(Wektor w)  { x = x + w.get_vector_X(); y = y + w.get_vector_Y(); }

void Punkt::reflection_Point_Point(Punkt p)    {x = (2 * p.getX() - x); y = (2 * p.getY() - y);}

void Punkt::reflection_Axis_Point()   { x = -x; y = -y; }

void Punkt::rotate_by_angle_Point(Punkt p, double angle)
{
    x = (x - p.getX()) * cos(angle) - (y - p.getY()) * sin(angle) + p.getX();
    y = (x - p.getX()) * sin(angle) - (y - p.getY()) * cos(angle) + p.getY();
}

Odcinek::Odcinek()
{
    a = Punkt();
    b = Punkt();
}

Punkt Odcinek::get_PointA()  { return a; }

Punkt Odcinek::get_PointB()  { return b; }

void Odcinek::set_Segment(Punkt a1, Punkt b1)
{
    if (a1.getX() == b1.getX() and a1.getY() == b1.getY())  throw invalid_argument("nie mozna utworzyc odcinka o dlugosci 0");
    else a = a1; b = b1;
}

void Odcinek::copy_Segment(Odcinek s) { a = s.get_PointA(); b = s.get_PointB(); }

void Odcinek::move_Segment(Wektor w)  { a.move_Point(w); b.move_Point(w); }

double Odcinek::get_distance()   { return distance(a, b); }

void Odcinek::reflection_Point_Segment(Punkt p)    { a.reflection_Point_Point(p); b.reflection_Point_Point(p); }

void Odcinek::reflection_Axis_Segment()   { a.reflection_Axis_Point(); b.reflection_Axis_Point(); }

bool Odcinek::if_in_Segment(Punkt p)
{
    double wyznacznik = (a.getX() * b.getY()) + (b.getX() * p.getY()) + (p.getX() * a.getY()) - (b.getY() * p.getX()) - (p.getY() * a.getX()) - (a.getY() * b.getX());
    if( wyznacznik == 0)
    {
        if( (p.getX() >= min(a.getX(), b.getX())) && (p.getX() <= max(a.getX(), b.getX())) && (p.getY() >= min(a.getY(), b.getY())) && (p.getY() <= max(a.getY(), b.getY())) ) return true;
        else return false;
    }
    else return false;
}

void Odcinek::rotate_by_angle_Segment(Punkt p, double angle)
{
    a.rotate_by_angle_Point(p, angle);
    b.rotate_by_angle_Point(p, angle);
}

Trojkat::Trojkat()
{
    a = Punkt();
    b = Punkt();
    c = Punkt();
}

Punkt Trojkat::get_PointA_Tri()  { return a; }

Punkt Trojkat::get_PointB_Tri()  { return b; }

Punkt Trojkat::get_PointC_Tri()  { return c; }

void Trojkat::set_Tri(Punkt a1, Punkt b1, Punkt c1)
{
    if (a1.getX() == b1.getX() and b1.getX() == c1.getX() )  throw invalid_argument("nie mozna utworzyc trojkata o takich bokach");
    else if (a1.getY() == b1.getY() and b1.getY() == c1.getY())  throw invalid_argument("nie mozna utworzyc trojkata o takich bokach");
    else
    {
        double wspolczynnik_a = (b1.getY() - a1.getY()) / (b1.getX() - a1.getX());
        double wspolczynnik_b = (c1.getY() - a1.getY()) / (c1.getX() - a1.getX());
        if (wspolczynnik_a == wspolczynnik_b)  throw invalid_argument("nie mozna utworzyc trojkata o takich bokach");
        else a = a1; b = b1; c = c1;
    }

}

void Trojkat::copy_Tri(Trojkat s) { a = s.get_PointA_Tri(); b = s.get_PointB_Tri(); c = s.get_PointC_Tri(); }

void Trojkat::move_Tri(Wektor w)  { a.move_Point(w); b.move_Point(w); c.move_Point(w); }

void Trojkat::reflection_Point_Tri(Punkt p)    { a.reflection_Point_Point(p); b.reflection_Point_Point(p); c.reflection_Point_Point(p); }

void Trojkat::reflection_Axis_Tri()   { a.reflection_Axis_Point(); b.reflection_Axis_Point(); c.reflection_Axis_Point(); }

double Trojkat::region_Tri()
{
    return distance(a, b) + distance(b, c) + distance(c, a);
}

double Trojkat::pole_Tri()
{
    return (abs((b.getX() - a.getX()) * (c.getY() - a.getY()) - (b.getY() - a.getY()) * (c.getX() - a.getX())))/2;
}

void Trojkat::rotate_by_angle_Tri(Punkt p, double angle)
{
    a.rotate_by_angle_Point(p, angle);
    b.rotate_by_angle_Point(p, angle);
    c.rotate_by_angle_Point(p, angle);
}

bool Trojkat::point_in_Tri(Punkt p)
{
    double t1, t2, t3;
    t1 = pole_global(a, b, p);
    t2 = pole_global(a, p, c);
    t3 = pole_global(p, b, c);
    if(pole_Tri() == (t1 + t2 + t3)) return true;
    else return false;
}