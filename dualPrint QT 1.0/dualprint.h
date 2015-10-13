/**     dualPrint
 *  By: Javier Oscar Cordero Pérez
 *  License: MIT-X
 *  Description: dualPrint is an application to facilitate manual duplex printing.
 *  Copyright 2014
**/

#ifndef DUALPRINT_H
#define DUALPRINT_H
#include <iostream>
#include <sstream> //Used for integer to string conversion

using namespace std;

class dualprint {
public:
    // Public functions

    //> Constant range dualPrint
    string simpleOdd( int, int, int );
    string simpleEven( int, int, int );
    int simpleTotal( int, int, int );

    //> Constructors
    dualprint( int Cap = 5000 );

private:
    // Private Variables
    string write, wOdd, wEven;
    int cap, currentFirstPage, currentLastPage, pagesPerSide, acumulator;

    // Private Functions
    bool capValidation( int, int, int );
    string num2string( int );

    //> Constant range dualPrint
    void setSimpleValues( int, int, int );
    void resetOdd(); // Set and reset variables for operations.
    void resetEven();
    void onePagePerSideOdd();
    void onePagePerSideEven();
    void multipage();
    void multipageReverse();
};

#endif // DUALPRINT_H
