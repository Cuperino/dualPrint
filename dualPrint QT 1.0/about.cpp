#include "about.h"
#include "ui_about.h"

About::About(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::About)
{
    ui->setupUi(this);
}

About::~About()
{
    delete ui;
}

void About::on_pushButton_Web_clicked()
{
    QString link="http://imaginary.tech/dualprint";
    QDesktopServices::openUrl(QUrl(link));
}

void About::on_pushButton_Lic_clicked()
{
    QString link="http://imaginary.tech/dualprint/LICENSE";
    QDesktopServices::openUrl(QUrl(link));
}
