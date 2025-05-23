#include "Wejscie.hpp"

using namespace std;

Wejscie::Wejscie(const string &filename) {
    try {
        file.open(filename);
    }
    catch (exception& e) {
        throw e;
    }
}
Wejscie::~Wejscie() {
    if (file.is_open()) {
        file.close();
    }
}

bool Wejscie::eof() {
    return file.eof();
}
