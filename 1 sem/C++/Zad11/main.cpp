#include <iostream>

using namespace std;

int main()
{
  int tab[6] = {0, 7, 5, 9, 2, 5};
  int tmp = 0;
  int siz = sizeof(tab);
  for (int i = 0; i < siz - 1; i++)
    {
      for (int j = i + 1; j < siz; j++)
        {
          if(tab[i] > tab[j])
          {
            tmp = tab[i];
            tab[i] = tab[j];
            tab[j] = tmp;
          }
        }
    }
  for(int i = 0; i < siz; i++)
    {
      cout<<tab[i]<<" ";
    }
}