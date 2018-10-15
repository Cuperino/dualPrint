#ifndef HELP_H
#define HELP_H

#include <QDialog>
#include <QPixmap>

namespace Ui {
class Help;
}

class Help : public QDialog
{
    Q_OBJECT

public:
    explicit Help(QWidget *parent = nullptr);
    ~Help();

private slots:
    void on_closeButton_clicked();

    void on_previousButton_clicked();

    void on_nextButton_clicked();

    void setCurrentElement();

private:
    Ui::Help *ui;
    int i;
    static const int SIZE = 8;
    QString description[SIZE];
};

#endif // HELP_H
