#ifndef LISTA5_KOLOR_H
#define LISTA5_KOLOR_H
class Kolor
{
protected:
    int R;
    int G;
    int B;
public:
    Kolor();
    Kolor(int t, int g, int b);
    int getR();
    int getG();
    int getB();
    void setR(int);
    void setG(int);
    void setB(int);
    void przyciemnij(double);
    void polacz(Kolor);

};
#endif
