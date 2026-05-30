// Copyright (C) 2012-2026 Javier O. Cordero Pérez
// SPDX-License-Identifier: MIT

#ifndef DPCLI_H
#define DPCLI_H
#include <cstdlib> //Using atoi char to int conversion

class dpCLI
{
public:
    dpCLI(int argc, char* argv[]);

private:
    // Variables
    bool verbose, displayOdd, displayEven, displayTotal;
    // Functions
    void showUsage();
    void showHeader();
    void constantPrint( int, int, int );
};

#endif // DPCLI_H
