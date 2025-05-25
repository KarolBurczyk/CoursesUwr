#include <iostream>
#include <iomanip>
#include <sstream>
#include <istream>
#include <vector>
#include <algorithm>

using namespace std;

inline istream& clearline(istream& input)
{
    char c;
    while (input.get(c) && c != '\n')
    {}
    return input;
}

struct Ignore
{
    int count;

    friend istream& operator>>(istream& input, const Ignore& manipulator) {
        char c;
        int ignored = 0;
        while (manipulator.count > ignored && input.get(c) && c != '\n') {
            if (c == '\n' or c == EOF) {
                break;
            }
            ignored++;
        }
        return input;
}

public:
    Ignore(int x) : count(x) {}
};

ostream& comma(ostream& os)
{
    return os << ", ";
}

ostream& colon(ostream& os)
{
    return os << ": ";
}

string index(int x, int w) {
    stringstream ss;
    ss << "[" << setw(w) << x << "]";
    return ss.str();
}

int main()
{
    vector<string> lines;
    string text;

    cout << "Oto przykladowe testy manipulatorow" << colon << endl;

    cout << "Podaj tekst" << colon;

    getline(cin >> Ignore(3), text);
    lines.push_back(text);

    cout << "Podaj tekst" << colon;

    getline(cin >> clearline, text);
    lines.push_back(text);

    cout << "Podaj tekst" << colon;

    getline(cin >> Ignore(5), text);
    lines.push_back(text);

    cout << "Podaj tekst" << colon;

    getline(cin >> clearline, text);
    lines.push_back(text);

    cout << "Przecinek:'" << comma << "'" << endl;

    cout << index(7, 7) << endl;

    sort(lines.begin(), lines.end());

    for(const auto & line : lines)
    {
        cout << line << endl;
    }

}