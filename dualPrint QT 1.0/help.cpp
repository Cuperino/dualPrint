#include "help.h"
#include "ui_help.h"

Help::Help(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::Help)
{
    ui->setupUi(this);
}

Help::~Help() {
    delete ui;
}

void Help::on_closeButton_clicked() {
    this->close();
}

void Help::on_previousButton_clicked() {

}

void Help::on_nextButton_clicked() {

}
