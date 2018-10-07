/**     dualPrint
 *  By: Javier Oscar Cordero Pérez
 *  License: MIT-X
 *  Description: dualPrint is an application to facilitate manual duplex printing.
 *  Copyright 2014
**/

#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
}

MainWindow::~MainWindow() {
    delete ui;
}

void MainWindow::on_dualPrintButton_clicked() {
    // Get input values from UI
    int firstPage = ui->firstPageSpinBox->text().toInt(),
        lastPage = ui->lastPageSpinBox->text().toInt(),
        pagesPerSide = ui->pagesPerSideSpinBox->text().toInt();

    // dualPrint into corresponding textboxes
    ui->oddOutput->setText( QString::fromStdString(dualPrint.simpleOdd(firstPage, lastPage, pagesPerSide)) );
    ui->evenOutput->setText( QString::fromStdString(dualPrint.simpleEven(firstPage, lastPage, pagesPerSide)) );
    ui->dualPrintButton->setText( "Total: "+QString::number(dualPrint.simpleTotal(firstPage, lastPage, pagesPerSide)) );

    // Copy Odd: textbox into clipboard using the QT library.
    on_oddCopy_clicked();

    return;
}

void MainWindow::on_oddCopy_clicked() {
    // Copy Odd: textbox into clipboard using the QT library.
    QClipboard *clipboard = QApplication::clipboard();
    clipboard->setText(ui->oddOutput->text(), QClipboard::Clipboard);
    ui->statusBar->showMessage("First print range copied to clipboard.");
}

void MainWindow::on_evenCopy_clicked() {
    // Copy Even: textbox into clipboard using the QT library.
    QClipboard *clipboard = QApplication::clipboard();
    clipboard->setText(ui->evenOutput->text(), QClipboard::Clipboard);
    ui->statusBar->showMessage("Second print range copied to clipboard.");
}

void MainWindow::on_aboutButton_clicked() {
    About *about = new About;
    about->show();
}

void MainWindow::on_howToButton_clicked() {
    //Help *help = new Help;
    //help->show();
}
