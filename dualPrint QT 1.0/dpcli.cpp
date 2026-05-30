// Copyright (C) 2012-2026 Javier O. Cordero Pérez
// SPDX-License-Identifier: MIT

#include <iostream>

#include "dpcli.h"
#include "dualprint.h"

dpCLI::dpCLI( int argc, char* argv[] )
{
    // Initialize private values
    verbose = true;
    displayOdd = false;
    displayEven = false;
    displayTotal = false;

    // Process extra arguments.
    if ( argc > 2 ) {
        std::string arg;
        for ( int i = 2; i < argc; ++i ) {
            arg = argv[i];
            if ( arg == "-h" || arg == "--help" ) {
                showUsage();
                break;
            }
            else if ( arg == "-p" || arg == "/p" || arg == "--pipe")
                verbose = false;
            else if ( arg == "-o" || arg == "/o" || arg == "--odd")
                displayOdd = true;
            else if ( arg == "-e" || arg == "/e" || arg == "--even")
                displayEven = true;
            else if ( arg == "-t" || arg == "/t" || arg == "--total")
                displayTotal = true;
        } // end for

        // if no good extra arguments are entered, switch to default.
        if (displayOdd == false && displayEven == false && displayTotal == false) {
            displayOdd=true;
            displayEven=true;
            displayTotal=true;
        } // end if

        // Arguments passed. Do a dualPrint.
        constantPrint( atoi(argv[1]), atoi(argv[2]), atoi(argv[3]) );

    } // end if
    else
        showUsage();
} // end dpCLI

// PRIVATE

void dpCLI::constantPrint( int firstPage, int lastPage, int pagesPerSide ) {
    dualprint dualPrint/*(Cap )*/; // Set maximum pages Cap. Good for system with limited resources.

    if (verbose == false) {
        if (displayOdd == true)
            std::cout << dualPrint.simpleOdd( firstPage, lastPage, pagesPerSide ) << std::endl;
        if (displayEven == true)
            std::cout << dualPrint.simpleEven( firstPage, lastPage, pagesPerSide ) << std::endl;
        if (displayTotal == true)
            std::cout << dualPrint.simpleTotal( firstPage, lastPage, pagesPerSide ) << std::endl;
    }
    else {
        this->showHeader();
        if (displayOdd == true)
            std::cout << std::endl << " Odd:\t" << dualPrint.simpleOdd( firstPage, lastPage, pagesPerSide ) << std::endl;
        if (displayEven == true)
            std::cout << std::endl << " Even:\t" << dualPrint.simpleEven( firstPage, lastPage, pagesPerSide ) << std::endl;
        if (displayTotal == true)
            std::cout << std::endl << " Total:\t" << dualPrint.simpleTotal( firstPage, lastPage, pagesPerSide ) << std::endl;
    }
    return;
}

void dpCLI::showUsage() {
    this->showHeader();
    std::cout << "\nUsage:"
         << "\n <initial_page> <last_page> <pages_per_side> <options>"
         /*<< "\n Segmented print: <print_range> <pages_per_side> <options>\n"*/
         << "\nOptions:\n"
         << "\t-h,--help\t\tShow this help message\n"
         << "\t-p,--pipe\t\tShow numbers only\n"
         << "\t-o,--odd\t\tShow odd print set\n"
         << "\t-e,--even\t\tShow even print set\n"
         << "\t-t,--total\t\tShow total of pages to print\n"
         << "\nNote:\n\tOdd, even and total appear by default\n";
    return;
}

void dpCLI::showHeader() {
    std::cout << "DualPrint - Manual duplex printing made easier"
         << "\nLicenced under the MIT, by Javier Cordero <javier@imaginary.tech>\n";
}
