/**     dualPrint
 *  By: Javier Oscar Cordero Pérez
 *  License: MIT-X
 *  Description: dualPrint is an application to facilitate manual duplex printing.
 *  Copyright 2014
**/

#include <QtGlobal>
#include <QApplication>
#include "mainwindow.h"
#include "dpcli.h"

int main(int argc, char* argv[])
{
    // Objects
    QApplication a(argc, argv);

    // Program
    //> If ran with more than an argument, enter classic CLI mode.
    if (argc>1) {
        // Load CLI
        dpCLI cli(argc, argv);
    }
    //> Otherwise, load the GUI
    else {
        // Load GUI    
        MainWindow w;
        w.show();
        return a.exec();
    }
    return 0;
}
