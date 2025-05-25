#include "kolornt.h++"
KolorNt::KolorNt()
:KolorTransparentny(0, 0, 0, 0)
,KolorNazwany("")
{}

KolorNt::KolorNt(int a, int b, int c, int t, string s)
:KolorTransparentny(a, b, c, t)
,KolorNazwany(s)
{}