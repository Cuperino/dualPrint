/**     dualPrint
 *  By: Javier Oscar Cordero Pérez
 *  License: MIT-X
 *  Description: dualPrint is an application to facilitate manual duplex printing.
 *  Copyright 2014
**/

#ifndef DPCLI_H
#define DPCLI_H
#include <cstdlib> //Using atoi char to int conversion
#include <sstream> //Used for integer to string conversion
#include "dualprint.h"

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
