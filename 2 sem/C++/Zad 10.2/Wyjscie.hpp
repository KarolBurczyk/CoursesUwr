#include <fstream>

using namespace std;

class Wyjscie {
public:
    Wyjscie(const string& filename);
    ~Wyjscie();

    template<typename T>
    void write(const T& value)
    {
        file.write(reinterpret_cast<const char*>(&value), sizeof(T));
    }

private:
    ofstream file;
};

