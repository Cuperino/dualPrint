/**     dualPrint
 *  By: Javier Oscar Cordero Pérez
 *  License: MIT-X
 *  Description: dualPrint is an application to facilitate manual duplex printing.
 *  Copyright 2014
**/

#include "dualprint.h"
#include <iostream>
#include <cstdlib> //Using atoi char to int conversion
#include <sstream> //Used for integer to string conversion
#include <cmath> //Used for absolute values

using namespace std;

//PUBLIC

dualprint::dualprint( int Cap ) {
    cap = Cap*2;
    return;
}

// Cap input validation for simple algorithm
bool dualprint::capValidation( int first, int last, int perSide) {
    if ((last - first + 1.0) / perSide > cap)
        return false; // Exceeded cap value.
    return true; // Validation pass.
}

// CONSTANT RANGE PRINT
string dualprint::simpleOdd( int first, int last, int perSide ) {
    //RESSET VALUES FOR OPERATION
    setSimpleValues(first, last, perSide); //Set class variables
    resetOdd();
    if ( currentFirstPage == currentLastPage )
        wOdd = currentFirstPage;
        //ONE PAGE PER SIDE
    else if ( pagesPerSide == 1 )
        onePagePerSideOdd();
    else // MULTI PagesPerSide
         // FIRST TO LAST
        if ( currentFirstPage < currentLastPage ) // if pages in normal order
            //EVEN HAS ONE SET ONLY
            if ( currentLastPage < currentFirstPage+pagesPerSide ) //fEspecial 1 in ISC dualPrint
                write += '-' + num2string( currentLastPage );
            else { //MULTIPLE PAGES PER SIDE
                write += '-';
                multipage();
            }
        else
            //EVEN HAS ONE SET ONLY
            if ( currentLastPage > currentFirstPage-pagesPerSide ) //fEspecial 1 in ISC dualPrint
                write += '-' + num2string( currentLastPage );
            else { //MULTIPLE PAGES PER SIDE
                write += '-';
                multipageReverse();
            }
    wOdd = write;

    return wOdd;
}

string dualprint::simpleEven( int first, int last, int perSide ) {
    //RESET VALUES FOR OPERATION
    setSimpleValues(first, last, perSide);
    resetEven();
    //Is there's a need to print anything at all? Check need and direction of print.
    if ( ( currentFirstPage < currentLastPage-pagesPerSide+1 && currentFirstPage < currentLastPage ) || ( currentFirstPage > currentLastPage+pagesPerSide-1 && currentFirstPage > currentLastPage ) ) {
        //ONE PAGE PER SIDE
        if ( pagesPerSide == 1 )
            onePagePerSideEven();
        else // MULTI PagesPerSide
             // FIRST TO LAST
            if ( currentFirstPage < currentLastPage ) // if pages in normal order
                //EVEN HAS ONE PAGE ONLY
                if ( currentLastPage == currentFirstPage+pagesPerSide ) //fEspecial 0 in ISC dualPrint
                    wEven = write; //* This can be improved.
                //EVEN HAS ONE SET ONLY
                else if ( currentLastPage < currentFirstPage+pagesPerSide*2 ) //fEspecial 1 in ISC dualPrint
                    //onlyOneSetOnBackEven();
                    write += '-' + num2string( currentLastPage );
                else { //MULTIPLE PAGES PER SIDE
                    write += '-';
                    multipage();
                }
            else
             // REVERSE
                //EVEN HAS ONE PAGE ONLY
                if ( currentLastPage == currentFirstPage-pagesPerSide ) //fEspecial 0 in ISC dualPrint
                    //onlyOnePageOnBackEven();
                    wEven = write; //* This can be improved.
                    //EVEN HAS ONE SET ONLY
                else if ( currentLastPage > currentFirstPage-pagesPerSide) //fEspecial 1 in ISC dualPrint
                    //onlyOneSetOnBackEven();
                    write += '-' + num2string( currentLastPage );
                else { //MULTIPLE PAGES PER SIDE
                    write += '-';
                    multipageReverse();
                }
        wEven = write;
    } // end if
    else
        wEven = "";
    return wEven;
} // end function even

int dualprint::simpleTotal( int first, int last, int perSide ) {
    int total=0;
    if (perSide>0)
    {
        if ( first<last )
            total = abs( (last-first)/perSide/2+1 );
        else
            total = abs( (first-last)/perSide/2+1 );
    }
    return total;
} // end function total

//PRIVATE
//Set class' global variables according to arguments.
void dualprint::setSimpleValues( int First, int Last, int PerSide ) {

    currentFirstPage = abs( First );
    currentLastPage = abs( Last );
    pagesPerSide = abs( PerSide );

    if ( currentFirstPage < 1 )
        currentFirstPage = 1;
    if ( currentLastPage < 1 )
        currentLastPage = 1;
    if ( pagesPerSide < 1 )
        pagesPerSide = 1;

    return;
} // end function setValues

//Convert integers to strings for concatenation. /*Reference: http://www.wlug.org.nz/ConvertingAnIntegerToaStringInCpp*/
string dualprint::num2string( int num) {
    ostringstream buffer;
    buffer << num;
    return buffer.str();
}

//Set or reset basic variables for dualprint operations.
void dualprint::resetOdd() {
    //mod = 0; //part of 3.0
    acumulator = currentFirstPage;
    write = num2string(currentFirstPage);
    return;
}
void dualprint::resetEven() {
    //mod = 0;
    if ( currentFirstPage < currentLastPage )
        acumulator = currentFirstPage + pagesPerSide;
    else
        acumulator = currentFirstPage - pagesPerSide;
    write = num2string(acumulator);
    return;
}

//Comma only for one page per side documents
void dualprint::onePagePerSideOdd() {
    if ( currentFirstPage < currentLastPage)
    {
        acumulator += 2;
        while (acumulator <= currentLastPage)
        {
            write += ',';
            write += num2string(acumulator);
            acumulator += 2;
        }
    }
    else
    {
        acumulator -= 2;
        while (acumulator >= currentLastPage)
        {
            write += ',';
            write += num2string(acumulator);
            acumulator -= 2;
        }
    }
    wOdd = write;
    return;
}
void dualprint::onePagePerSideEven() {
    if ( currentFirstPage < currentLastPage)
    {
        acumulator += 2;
        while (acumulator <= currentLastPage)
        {
            write += ',';
            write += num2string(acumulator);
            acumulator += 2;
        }
    }
    else
    {
        acumulator -= 2;
        while (acumulator >= currentLastPage)
        {
            write += ',';
            write += num2string(acumulator);
            acumulator -= 2;
        }
    }
    wEven = write;
    return;
}

//Process multiple pages per side
void dualprint::multipage() {
    int testVal=0;
    do {
        //Dash
        acumulator += pagesPerSide-1;
        write += num2string(acumulator);
        //testComa
        testVal = acumulator+pagesPerSide+1;
        if ( testVal < currentLastPage ) {
            write += ',';
            //Coma
            acumulator += pagesPerSide+1;
            write += num2string(acumulator);
            //test for next Dash
            testVal = acumulator + pagesPerSide-1;
            write += '-';
            if (testVal == currentLastPage) {
                acumulator = testVal;
                write += num2string(acumulator);
                return;
            }
            else if (testVal > currentLastPage) {
                acumulator = currentLastPage;
                write += num2string(acumulator);
                return;
            }
            // repeat do while
        }
        else if ( testVal == currentLastPage ) {
            write += ',';
            acumulator += pagesPerSide+1;
            write += num2string(acumulator);
            return;
        }
        else
            return;
    } while (acumulator > acumulator-1); //"Infinite loop". Since the last page could be reached at any of multiple steps, return points are placed at key positions.
}

//Process multiple pages per side
void dualprint::multipageReverse() {
    int testVal=0;
    do {
        //Dash
        acumulator -= pagesPerSide-1;
        write += num2string(acumulator);
        //testComa
        testVal = acumulator - (pagesPerSide+1);
        if ( testVal > currentLastPage ) {
            write += ',';
            //Coma
            acumulator -= pagesPerSide+1;
            write += num2string(acumulator);
            //test for next Dash
            testVal = acumulator - (pagesPerSide-1);
            write += '-';
            if (testVal == currentLastPage) {
                acumulator = testVal;
                write += num2string(acumulator); //+ 'b';
                return;
            }
            else if (testVal < currentLastPage) {
                acumulator = currentLastPage;
                write += num2string(acumulator);
                return;
            }
        }
        else if ( testVal == currentLastPage ) {
            write += ',';
            acumulator -= pagesPerSide+1;
            write += num2string(acumulator);// + 'd';
            return;
        }
        else
            return;
    } while (acumulator > acumulator-1); //"Infinite loop". Since the last page could be reached at any of multiple steps, return points are placed at key positions.
}
