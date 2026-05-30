/**     dualPrint
 *  By: Javier Oscar Cordero Pérez
 *  License: MIT-X
 *  Description: dualPrint is an application to facilitate manual duplex printing.
 *  Copyright 2014
 **/

#include "dpcli.h"
#include "mainwindow.h"
#include <QApplication>
#include <QtGlobal>

int main(int argc, char* argv[])
{
    // Objects
    QApplication a(argc, argv);

    // Program
    //> If ran with more than an argument, enter classic CLI mode.
    if (argc > 1) {
        // Load CLI
        dpCLI cli(argc, argv);
    }
    //> Otherwise, load the GUI
    else {
        // Load GUI
        MainWindow w;
        w.resize(338, 513);
        w.showNormal();
        return a.exec();
    }
    return 0;
}
