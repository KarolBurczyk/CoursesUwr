# Makefile
CXX = g++
CXXFLAGS = -Wall -Wextra -std=c++17 -O2

all: transport

transport: transport.o
	$(CXX) $(CXXFLAGS) -o transport transport.o

transport.o: transport.cpp
	$(CXX) $(CXXFLAGS) -c transport.cpp

clean:
	rm -f *.o

distclean: clean
	rm -f transport
