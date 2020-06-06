all: simulate.cpp
	gcc -shared -o simulate.so -Wall -fPIC simulate.cpp