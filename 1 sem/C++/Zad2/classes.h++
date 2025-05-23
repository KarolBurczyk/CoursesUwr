#ifndef CLASSES_HPP
#define CLASSES_HPP
#include <iostream>
#include <cmath>

using namespace std;

class Wektor
{
private:
    double x;
    double y;

public:
    Wektor();

    double get_vector_X();
    double get_vector_Y();
    void set_Vector(double a, double b);
};



class Punkt
{
private:
    double x;
    double y;

public:
    Punkt();

    double getX();
    double getY();
    void copy_Point(Punkt a);
    void set_Point(double a, double b);
    void move_Point(Wektor w);
    void reflection_Point_Point(Punkt p);
    void reflection_Axis_Point();
    void rotate_by_angle_Point(Punkt p, double angle);
};

double distance(Punkt a, Punkt b);
double pole_global(Punkt a, Punkt b, Punkt c);

class Odcinek
{
private:
    Punkt a;
    Punkt b;

public:
    Odcinek();

    Punkt get_PointA();
    Punkt get_PointB();
    void set_Segment(Punkt a1, Punkt b1);
    void copy_Segment(Odcinek s);
    void move_Segment(Wektor w);
    double get_distance();
    void reflection_Point_Segment(Punkt p);
    void reflection_Axis_Segment();
    bool if_in_Segment(Punkt p);
    void rotate_by_angle_Segment(Punkt p, double angle);
};

class Trojkat
{
private:
    Punkt a;
    Punkt b;
    Punkt c;

public:
    Trojkat();

    Punkt get_PointA_Tri();
    Punkt get_PointB_Tri();
    Punkt get_PointC_Tri();
    void set_Tri(Punkt a1, Punkt b1, Punkt c1);
    void copy_Tri(Trojkat s);
    void move_Tri(Wektor w);
    void reflection_Point_Tri(Punkt p);
    void reflection_Axis_Tri();
    double region_Tri();
    double pole_Tri();
    void rotate_by_angle_Tri(Punkt p, double angle);
    bool point_in_Tri(Punkt p);
};

#endif
