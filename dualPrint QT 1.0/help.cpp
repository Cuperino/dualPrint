#include "help.h"
#include "ui_help.h"

Help::Help(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::Help)
{
    ui->setupUi(this);
    this->i = 0;
    this->description[0] = "Message 1";
    this->description[1] = "Message 2";
    this->description[2] = "Message 3";
    this->description[3] = "Message 4";
    this->description[4] = "Message 5";
    this->description[5] = "Message 6";
    this->description[6] = "Message 7";
    this->description[7] = "Message 8";
    this->setCurrentElement();
}

Help::~Help() {
    delete ui;
}

void Help::on_closeButton_clicked() {
    this->close();
}

void Help::on_previousButton_clicked() {
    if (this->i == 0)
        i = this->SIZE-1;
    else
        this->i--;
    this->setCurrentElement();
}

void Help::on_nextButton_clicked() {
    if (this->i == this->SIZE-1)
        i = 0;
    else
        this->i++;
    this->setCurrentElement();
}

void Help::setCurrentElement() {
    QString url = ":/img/images/help" + QString::number(this->i) + ".jpg";
    QPixmap currentPic(url);
    ui->picture->setPixmap(currentPic);
    ui->picture->resize(ui->picture->pixmap()->size());
    ui->description->setText(this->description[this->i]);
}
