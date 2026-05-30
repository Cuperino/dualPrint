// Copyright (C) 2012-2026 Javier O. Cordero Pérez
// SPDX-License-Identifier: MIT

#include "about.h"
#include "ui_about.h"

About::About(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::About)
{
    ui->setupUi(this);
    this->c = 0;
}

About::~About()
{
    delete ui;
}

void About::on_pushButton_Web_clicked()
{
    QString link="http://dualprint.org/";
    QDesktopServices::openUrl(QUrl(link));
}

void About::on_pushButton_Lic_clicked()
{
    QString link="http://dualprint.org/LICENSE";
    QDesktopServices::openUrl(QUrl(link));
}

void About::on_pushButton_clicked()
{
    this->c++;
    if (this->c == 16) {
        QString link="https://github.com/javiercordero/IlluminationSoftwareCreator";
        QDesktopServices::openUrl(QUrl(link));
        this->c = 0;
    }
}
