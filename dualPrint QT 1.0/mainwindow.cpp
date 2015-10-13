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

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_dualPrintButton_clicked()
{
    // Get input values from UI
    int firstPage = ui->firstPageTextBox->text().toInt(),
        lastPage = ui->lastPageTextBox->text().toInt(),
        pagesPerSide = ui->pagesPerSideSpinBox->text().toInt();

    // dualPrint into corresponding textboxes
    ui->oddOutput->setText( QString::fromStdString(dualPrint.simpleOdd(firstPage, lastPage, pagesPerSide)) );
    ui->evenOutput->setText( QString::fromStdString(dualPrint.simpleEven(firstPage, lastPage, pagesPerSide)) );
    ui->dualPrintButton->setText( "Total: "+QString::number(dualPrint.simpleTotal(firstPage, lastPage, pagesPerSide)) );

    // Copy Odd: textbox into clipboard using the QT library.
    on_oddCopy_clicked();

    return;
}

void MainWindow::on_oddCopy_clicked()
{
    // Copy Odd: textbox into clipboard using the QT library.
    QClipboard *clipboard = QApplication::clipboard();
    clipboard->setText(ui->oddOutput->text(), QClipboard::Clipboard);
    ui->statusBar->showMessage("First print range copied to clipboard.");
}

void MainWindow::on_evenCopy_clicked()
{
    // Copy Even: textbox into clipboard using the QT library.
    QClipboard *clipboard = QApplication::clipboard();
    clipboard->setText(ui->evenOutput->text(), QClipboard::Clipboard);
    ui->statusBar->showMessage("Second print range copied to clipboard.");
}

void MainWindow::on_aboutButton_clicked()
{
    // Load an About window similar to the Illumination version of dualPrint. See www.dualprint.org for more details.
    About *about = new About;
    about->show();
}

void MainWindow::on_howToButton_clicked()
{
    //* Load a specific local HTML5 onto a window. The HTML page shall display instructions on how to print on both sides with any printer.
    // Alternative operation... for the moment.
    QString link="http://imaginary.tech/dualprint/en/print-on-back.html";
    QDesktopServices::openUrl(QUrl(link));
}
