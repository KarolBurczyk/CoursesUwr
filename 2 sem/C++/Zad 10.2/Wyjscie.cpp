#include "Wyjscie.hpp"

using namespace std;

Wyjscie::Wyjscie(const string &filename) {
    try {
        file.open(filename);
    }
    catch (exception& e) {
        throw e;
    }
}
Wyjscie::~Wyjscie() {
    if (file.is_open()) {
        file.close();
    }
}

