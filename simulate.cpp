/*********************************************
 * 
 * simulate.cpp
 * 
 * Robert A McDougal
 * 5 June 2020
 * 
 ********************************************/

/*
    compile on linux or mac via:

    gcc -shared -o simulate.so -Wall -fPIC simulate.cpp
*/

#include <cstdint>

extern "C" {
    void simulate(int64_t n, double* xs, double* ys, double* zs, double x, double y, double z);
}

const double sigma = 10;
const double beta = 8. / 3.;
const double rho = 28;
const double dt = 0.01;

void simulate(int64_t n, double* xs, double* ys, double* zs, double x, double y, double z) {
    for (int64_t i = 0; i < n; i++) {
        double dxdt = sigma * (y - x);
        double dydt = x * (rho - z) - y;
        double dzdt = x * y - beta * z;
        xs[i] = x = x + dxdt * dt;
        ys[i] = y = y + dydt * dt;
        zs[i] = z = z + dzdt * dt;
    }
}