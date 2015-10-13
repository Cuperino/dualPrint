/**     dualPrint
 *  By: Javier Oscar Cordero Pérez
 *  License: MIT-X
 *  Description: dualPrint is an application to facilitate manual duplex printing.
 *  Copyright 2014
**/

#include "dpcli.h"
#include "javistd.h"

#include <QtGlobal>
//#include <QObject>
//#include <QCoreApplication>
#if QT_VERSION>4
    int i=5;
#else
    int i=4;
#endif

#include <QApplication>
#include "mainwindow.h"
#include <QDebug>

int main(int argc, char* argv[])
{
    qDebug() << "Current QT version" << i;


    // Constants
    const string SOFTWARE = "dualPrint",
                 VER = "QT 1.0",
                 MESSAGE = "Save paper!";

    // Objects
    QApplication a(argc, argv);
    static javistd jstd(SOFTWARE, VER, MESSAGE);

    // Program
    //> If ran with more than an argument, enter classic CLI mode.
    if (argc>1)
    {
        // Load CLI
        dpCLI cli(argc, argv, jstd);
    }
    //> Otherwise, load the GUI
    else
    {
        // Load GUI    
        MainWindow w;
        w.show();
        return a.exec();
    }
    return 0;
}
