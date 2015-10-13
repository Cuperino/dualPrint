/**     dualPrint
 *  By: Javier Oscar Cordero Pérez
 *  License: MIT-X
 *  Description: dualPrint is an application to facilitate manual duplex printing.
 *  Copyright 2014
**/

//#ifndef MAINWINDOW_H
#define MAINWINDOW_H
#include <QMainWindow>
#include <QClipboard>
#include "dualprint.h"
#include "about.h"

namespace Ui {
    class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT
    
public:
    explicit MainWindow(QWidget *parent = 0);
    ~MainWindow();
    
private slots:
    void on_dualPrintButton_clicked();

    void on_oddCopy_clicked();

    void on_evenCopy_clicked();

    void on_aboutButton_clicked();

    void on_howToButton_clicked();

private:
    Ui::MainWindow *ui;
    dualprint dualPrint;
};

//#endif // MAINWINDOW_H
