#ifndef ABOUT_H
#define ABOUT_H

#include <QDialog>
#include <QDesktopServices>
#include <QUrl>

namespace Ui {
class About;
}

class About : public QDialog
{
    Q_OBJECT

public:
    explicit About(QWidget *parent = 0);
    ~About();

private slots:
    void on_pushButton_Web_clicked();

    void on_pushButton_Lic_clicked();

    void on_pushButton_clicked();

private:
    Ui::About *ui;
    int c;
};

#endif // ABOUT_H
