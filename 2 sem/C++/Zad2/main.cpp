#include <iostream>
#include "classes.h++"
#include "global_functions.h++"

using namespace std;

int main()
{
    Wektor w1, w2;
    Punkt p1, p2, p3, p4, p5, p6;
    Odcinek o1, o2, o3;
    Trojkat t1, t2;

    w1.set_Vector(3,3);
    cout<<"Wektor w1: "<<w1.get_vector_X()<<","<<w1.get_vector_Y()<<endl;
    w2.set_Vector(1,2);
    cout<<"Wektor w2: "<<w2.get_vector_X()<<","<<w2.get_vector_Y()<<endl;

    p1.set_Point(0, 0);
    cout<<"Punkt p1: "<<p1.getX()<<","<<p1.getY()<<endl;
    p2.set_Point(5, 5);
    cout<<"Punkt p2: "<<p2.getX()<<","<<p2.getY()<<endl;
    p3.set_Point(3, 4);
    cout<<"Punkt p3: "<<p3.getX()<<","<<p3.getY()<<endl;
    p4.set_Point(5, 6);
    cout<<"Punkt p4: "<<p4.getX()<<","<<p4.getY()<<endl;
    p5.set_Point(2, 2);
    cout<<"Punkt p5: "<<p5.getX()<<","<<p5.getY()<<endl;
    p6.set_Point(10, 10);
    cout<<"Punkt p6: "<<p6.getX()<<","<<p6.getY()<<endl;

    o1.set_Segment(p1, p2);
    cout<<"Odcinek o1: "<<o1.get_PointA().getX()<<","<<o1.get_PointA().getY()<<" - "<<o1.get_PointB().getX()<<","<<o1.get_PointB().getY()<<endl;
    o2.set_Segment(p3, p4);
    cout<<"Odcinek o2: "<<o2.get_PointA().getX()<<","<<o2.get_PointA().getY()<<" - "<<o2.get_PointB().getX()<<","<<o2.get_PointB().getY()<<endl;
    o3.set_Segment(p5, p6);
    cout<<"Odcinek o3: "<<o3.get_PointA().getX()<<","<<o3.get_PointA().getY()<<" - "<<o3.get_PointB().getX()<<","<<o3.get_PointB().getY()<<endl;

    t1.set_Tri(p1, p2, p3);
    cout<<"Trojkat t1: "<<p1.getX()<<","<<p1.getY()<<" - "<<p2.getX()<<","<<p2.getY()<<" - "<<p3.getX()<<","<<p3.getY()<<endl;
    t2.set_Tri(p4, p5, p6);
    cout<<"Trojkat t2: "<<p4.getX()<<","<<p4.getY()<<" - "<<p5.getX()<<","<<p5.getY()<<" - "<<p6.getX()<<","<<p6.getY()<<endl;

    p4.copy_Point(p1);
    cout<<"P4 po skopiowaniu od p1: "<<p4.getX()<<","<<p4.getY()<<endl;

    p4.move_Point(w1);
    cout<<"P4 po przesunieciu o wektor w1: "<<p4.getX()<<","<<p4.getY()<<endl;

    p4.reflection_Point_Point(p2);
    cout<<"P4 po symetrii wzgledem p2: "<<p4.getX()<<","<<p4.getY()<<endl;

    p4.reflection_Axis_Point();
    cout<<"P4 po symetrii wzgledem osi: "<<p4.getX()<<","<<p4.getY()<<endl;

    p4.rotate_by_angle_Point(p1, 3.1416);
    cout<<"P4 po przesunieciu o kat wzgledem p1: "<<p4.getX()<<","<<p4.getY()<<endl;

    cout<<"Odleglosc miedzy p1, a p3: "<<distance(p1, p3)<<endl;

    if (o3.if_in_Segment(p2)) cout<<p2.getX()<<","<<p2.getY()<<" nalezy do "<<o3.get_PointA().getX()<<","<<o3.get_PointA().getY()<<" - "<<o3.get_PointB().getX()<<","<<o3.get_PointB().getY()<<endl;
    else cout<<p2.getX()<<","<<p2.getY()<<" nie nalezy do "<<o3.get_PointA().getX()<<","<<o3.get_PointA().getY()<<" - "<<o3.get_PointB().getX()<<","<<o3.get_PointB().getY()<<endl;

    if (o3.if_in_Segment(p1)) cout<<p1.getX()<<","<<p1.getY()<<" nalezy do "<<o3.get_PointA().getX()<<","<<o3.get_PointA().getY()<<" - "<<o3.get_PointB().getX()<<","<<o3.get_PointB().getY()<<endl;
    else cout<<p1.getX()<<","<<p1.getY()<<" nie nalezy do "<<o3.get_PointA().getX()<<","<<o3.get_PointA().getY()<<" - "<<o3.get_PointB().getX()<<","<<o3.get_PointB().getY()<<endl;

    if (o3.if_in_Segment(p3)) cout<<p3.getX()<<","<<p3.getY()<<" nalezy do "<<o3.get_PointA().getX()<<","<<o3.get_PointA().getY()<<" - "<<o3.get_PointB().getX()<<","<<o3.get_PointB().getY()<<endl;
    else cout<<p3.getX()<<","<<p3.getY()<<" nie nalezy do "<<o3.get_PointA().getX()<<","<<o3.get_PointA().getY()<<" - "<<o3.get_PointB().getX()<<","<<o3.get_PointB().getY()<<endl;

    cout<<"Pole trojkata t2: "<<t2.get_PointA_Tri().getX()<<","<<t2.get_PointA_Tri().getY()<<" - "<<t2.get_PointB_Tri().getX()<<","<<t2.get_PointB_Tri().getY()<<" - "<<t2.get_PointC_Tri().getX()<<","<<t2.get_PointC_Tri().getY()<<" ";
    cout<<"wynosi: "<<t2.pole_Tri()<<endl;

    cout<<"Pole trojkata t1: "<<t1.get_PointA_Tri().getX()<<","<<t1.get_PointA_Tri().getY()<<" - "<<t1.get_PointB_Tri().getX()<<","<<t1.get_PointB_Tri().getY()<<" - "<<t1.get_PointC_Tri().getX()<<","<<t1.get_PointC_Tri().getY()<<" ";
    cout<<"wynosi: "<<t1.pole_Tri()<<endl;

    cout<<p3.getX()<<","<<p3.getY()<<endl;
    if (t2.point_in_Tri(p3)) cout<<p3.getX()<<","<<p3.getY()<<" nalezy do t2"<<endl;
    else cout<<p3.getX()<<","<<p3.getY()<<" nie nalezy do t2"<<endl;

    if (t1.point_in_Tri(p1)) cout<<p1.getX()<<","<<p1.getY()<<" nalezy do t1"<<endl;
    else cout<<p1.getX()<<","<<p1.getY()<<" nie nalezy do t1"<<endl;

    cout<<"Odcinek o1: "<<o1.get_PointA().getX()<<","<<o1.get_PointA().getY()<<" - "<<o1.get_PointB().getX()<<","<<o1.get_PointB().getY()<<" i ";
    cout<<"Odcinek o2: "<<o2.get_PointA().getX()<<","<<o2.get_PointA().getY()<<" - "<<o2.get_PointB().getX()<<","<<o2.get_PointB().getY()<<" ";
    if (if_Segment_equally(o1, o2)) cout<<"sa rownolegle i ";
    else cout<<"nie sa rownolegle i ";
    if (if_Segment_perpendicular(o1, o2)) cout<<"sa prostopadle"<<endl;
    else cout<<"nie sa prostopadle"<<endl;

    cout<<"Trojkat t2: "<<t2.get_PointA_Tri().getX()<<","<<t2.get_PointA_Tri().getY()<<" - "<<t2.get_PointB_Tri().getX()<<","<<t2.get_PointB_Tri().getY()<<" - "<<t2.get_PointC_Tri().getX()<<","<<t2.get_PointC_Tri().getY()<<" oraz ";
    cout<<"Trojkat t1: "<<t1.get_PointA_Tri().getX()<<","<<t1.get_PointA_Tri().getY()<<" - "<<t1.get_PointB_Tri().getX()<<","<<t1.get_PointB_Tri().getY()<<" - "<<t1.get_PointC_Tri().getX()<<","<<t1.get_PointC_Tri().getY()<<" ";
    if (if_seprate_Tri(t1, t2)) cout<<"sa rozlaczne i ";
    else cout<<"nie sa rozlaczne i ";
    if (if_contain_Tri(t1, t2)) cout<<"sa zawieraja sie"<<endl;
    else cout<<"nie nie zawieraja sie"<<endl;

}
