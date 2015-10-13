/********************************************************************************
** Form generated from reading UI file 'about.ui'
**
** Created by: Qt User Interface Compiler version 5.2.1
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_ABOUT_H
#define UI_ABOUT_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QDialog>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QVBoxLayout>

QT_BEGIN_NAMESPACE

class Ui_About
{
public:
    QVBoxLayout *verticalLayout;
    QPushButton *pushButton;
    QLabel *dualPrint;
    QLabel *ver;
    QLabel *description;
    QLabel *Copyright;
    QLabel *License;
    QHBoxLayout *horizontalLayout;
    QPushButton *pushButton_Web;
    QPushButton *pushButton_Lic;

    void setupUi(QDialog *About)
    {
        if (About->objectName().isEmpty())
            About->setObjectName(QStringLiteral("About"));
        About->resize(240, 320);
        QIcon icon;
        icon.addFile(QStringLiteral(":/img/images/dualprint.gif"), QSize(), QIcon::Normal, QIcon::Off);
        About->setWindowIcon(icon);
        About->setModal(false);
        verticalLayout = new QVBoxLayout(About);
        verticalLayout->setObjectName(QStringLiteral("verticalLayout"));
        pushButton = new QPushButton(About);
        pushButton->setObjectName(QStringLiteral("pushButton"));
        QSizePolicy sizePolicy(QSizePolicy::MinimumExpanding, QSizePolicy::Fixed);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(pushButton->sizePolicy().hasHeightForWidth());
        pushButton->setSizePolicy(sizePolicy);
        pushButton->setIcon(icon);
        pushButton->setIconSize(QSize(90, 90));
        pushButton->setFlat(true);

        verticalLayout->addWidget(pushButton);

        dualPrint = new QLabel(About);
        dualPrint->setObjectName(QStringLiteral("dualPrint"));
        QSizePolicy sizePolicy1(QSizePolicy::Preferred, QSizePolicy::MinimumExpanding);
        sizePolicy1.setHorizontalStretch(0);
        sizePolicy1.setVerticalStretch(0);
        sizePolicy1.setHeightForWidth(dualPrint->sizePolicy().hasHeightForWidth());
        dualPrint->setSizePolicy(sizePolicy1);
        dualPrint->setText(QStringLiteral("dualPrint"));
        dualPrint->setAlignment(Qt::AlignBottom|Qt::AlignHCenter);

        verticalLayout->addWidget(dualPrint);

        ver = new QLabel(About);
        ver->setObjectName(QStringLiteral("ver"));
        sizePolicy1.setHeightForWidth(ver->sizePolicy().hasHeightForWidth());
        ver->setSizePolicy(sizePolicy1);
        ver->setAlignment(Qt::AlignHCenter|Qt::AlignTop);

        verticalLayout->addWidget(ver);

        description = new QLabel(About);
        description->setObjectName(QStringLiteral("description"));
        sizePolicy1.setHeightForWidth(description->sizePolicy().hasHeightForWidth());
        description->setSizePolicy(sizePolicy1);
        description->setAlignment(Qt::AlignCenter);
        description->setWordWrap(true);

        verticalLayout->addWidget(description);

        Copyright = new QLabel(About);
        Copyright->setObjectName(QStringLiteral("Copyright"));
        sizePolicy1.setHeightForWidth(Copyright->sizePolicy().hasHeightForWidth());
        Copyright->setSizePolicy(sizePolicy1);
        Copyright->setAlignment(Qt::AlignBottom|Qt::AlignHCenter);

        verticalLayout->addWidget(Copyright);

        License = new QLabel(About);
        License->setObjectName(QStringLiteral("License"));
        sizePolicy1.setHeightForWidth(License->sizePolicy().hasHeightForWidth());
        License->setSizePolicy(sizePolicy1);
        License->setAlignment(Qt::AlignHCenter|Qt::AlignTop);

        verticalLayout->addWidget(License);

        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setObjectName(QStringLiteral("horizontalLayout"));
        pushButton_Web = new QPushButton(About);
        pushButton_Web->setObjectName(QStringLiteral("pushButton_Web"));
        QSizePolicy sizePolicy2(QSizePolicy::Minimum, QSizePolicy::MinimumExpanding);
        sizePolicy2.setHorizontalStretch(0);
        sizePolicy2.setVerticalStretch(0);
        sizePolicy2.setHeightForWidth(pushButton_Web->sizePolicy().hasHeightForWidth());
        pushButton_Web->setSizePolicy(sizePolicy2);

        horizontalLayout->addWidget(pushButton_Web);

        pushButton_Lic = new QPushButton(About);
        pushButton_Lic->setObjectName(QStringLiteral("pushButton_Lic"));
        sizePolicy2.setHeightForWidth(pushButton_Lic->sizePolicy().hasHeightForWidth());
        pushButton_Lic->setSizePolicy(sizePolicy2);

        horizontalLayout->addWidget(pushButton_Lic);


        verticalLayout->addLayout(horizontalLayout);


        retranslateUi(About);

        QMetaObject::connectSlotsByName(About);
    } // setupUi

    void retranslateUi(QDialog *About)
    {
        About->setWindowTitle(QApplication::translate("About", "Dialog", 0));
        pushButton->setText(QString());
        ver->setText(QApplication::translate("About", "QT 1.0", 0));
        description->setText(QApplication::translate("About", "dualPrint is an app that assists manual multiple pages per sheet duplex printing.", 0));
        Copyright->setText(QApplication::translate("About", "Copyright 2014 Javier O. Cordero P\303\251rez", 0));
        License->setText(QApplication::translate("About", "dualPrint is available under the MIT License", 0));
        pushButton_Web->setText(QApplication::translate("About", "Website", 0));
        pushButton_Lic->setText(QApplication::translate("About", "License", 0));
    } // retranslateUi

};

namespace Ui {
    class About: public Ui_About {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_ABOUT_H
