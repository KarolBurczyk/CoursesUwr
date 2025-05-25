#ifndef LISTA5_PIKSEL_H
#define LISTA5_PIKSEL_H
class Piksel
{
protected:
    int x;
    int y;
    constexpr static int wymiary[] = {1920, 1080};
public:
    Piksel();
    Piksel(int, int);
    int getUp();
    int getDown();
    int getLeft();
    int getRight();
};
#endif
