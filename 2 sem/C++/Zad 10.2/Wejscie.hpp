#include <fstream>

using namespace std;

class Wejscie {
public:
    Wejscie(const string& filename);
    ~Wejscie();

    template<typename T>
    void read(T& value)
    {
        file.read(reinterpret_cast<char*>(&value), sizeof(T));
    }

    bool eof();

private:
    ifstream file;
};

