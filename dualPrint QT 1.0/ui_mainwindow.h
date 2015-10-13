/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created by: Qt User Interface Compiler version 5.2.1
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QLocale>
#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QSpacerItem>
#include <QtWidgets/QSpinBox>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QToolButton>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *centralWidget;
    QPushButton *pushButton;
    QWidget *widget;
    QVBoxLayout *verticalLayout;
    QLabel *firstPageLabel;
    QHBoxLayout *horizontalLayout_5;
    QSpacerItem *horizontalSpacer_3;
    QLineEdit *firstPageTextBox;
    QSpacerItem *horizontalSpacer;
    QLabel *lastPageLabel;
    QHBoxLayout *horizontalLayout_6;
    QSpacerItem *horizontalSpacer_4;
    QLineEdit *lastPageTextBox;
    QSpacerItem *horizontalSpacer_2;
    QLabel *pagesPerSideLabel;
    QHBoxLayout *horizontalLayout;
    QSpinBox *pagesPerSideSpinBox;
    QPushButton *dualPrintButton;
    QLabel *oddLabel;
    QHBoxLayout *horizontalLayout_2;
    QToolButton *oddCopy;
    QLineEdit *oddOutput;
    QLabel *evenLabel;
    QHBoxLayout *horizontalLayout_3;
    QToolButton *evenCopy;
    QLineEdit *evenOutput;
    QHBoxLayout *horizontalLayout_4;
    QPushButton *howToButton;
    QPushButton *aboutButton;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QStringLiteral("MainWindow"));
        MainWindow->setWindowModality(Qt::NonModal);
        MainWindow->setEnabled(true);
        MainWindow->resize(320, 450);
        QSizePolicy sizePolicy(QSizePolicy::Fixed, QSizePolicy::Fixed);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(MainWindow->sizePolicy().hasHeightForWidth());
        MainWindow->setSizePolicy(sizePolicy);
        MainWindow->setMinimumSize(QSize(320, 450));
        MainWindow->setMaximumSize(QSize(320, 450));
        QIcon icon;
        icon.addFile(QStringLiteral(":/img/images/dualprint.gif"), QSize(), QIcon::Normal, QIcon::Off);
        MainWindow->setWindowIcon(icon);
        MainWindow->setLocale(QLocale(QLocale::English, QLocale::PuertoRico));
        MainWindow->setAnimated(false);
        MainWindow->setDocumentMode(false);
        MainWindow->setTabShape(QTabWidget::Rounded);
        MainWindow->setUnifiedTitleAndToolBarOnMac(false);
        centralWidget = new QWidget(MainWindow);
        centralWidget->setObjectName(QStringLiteral("centralWidget"));
        pushButton = new QPushButton(centralWidget);
        pushButton->setObjectName(QStringLiteral("pushButton"));
        pushButton->setGeometry(QRect(0, 0, 320, 68));
        sizePolicy.setHeightForWidth(pushButton->sizePolicy().hasHeightForWidth());
        pushButton->setSizePolicy(sizePolicy);
        pushButton->setMinimumSize(QSize(0, 0));
        QIcon icon1;
        icon1.addFile(QStringLiteral(":/img/images/header.jpg"), QSize(), QIcon::Normal, QIcon::Off);
        pushButton->setIcon(icon1);
        pushButton->setIconSize(QSize(320, 68));
        pushButton->setAutoRepeat(false);
        pushButton->setFlat(true);
        widget = new QWidget(centralWidget);
        widget->setObjectName(QStringLiteral("widget"));
        widget->setGeometry(QRect(14, 76, 291, 351));
        verticalLayout = new QVBoxLayout(widget);
        verticalLayout->setSpacing(6);
        verticalLayout->setContentsMargins(11, 11, 11, 11);
        verticalLayout->setObjectName(QStringLiteral("verticalLayout"));
        verticalLayout->setContentsMargins(0, 0, 0, 0);
        firstPageLabel = new QLabel(widget);
        firstPageLabel->setObjectName(QStringLiteral("firstPageLabel"));
        QFont font;
        font.setPointSize(10);
        firstPageLabel->setFont(font);
        firstPageLabel->setTextFormat(Qt::AutoText);
        firstPageLabel->setAlignment(Qt::AlignCenter);
        firstPageLabel->setWordWrap(false);

        verticalLayout->addWidget(firstPageLabel);

        horizontalLayout_5 = new QHBoxLayout();
        horizontalLayout_5->setSpacing(6);
        horizontalLayout_5->setObjectName(QStringLiteral("horizontalLayout_5"));
        horizontalSpacer_3 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_5->addItem(horizontalSpacer_3);

        firstPageTextBox = new QLineEdit(widget);
        firstPageTextBox->setObjectName(QStringLiteral("firstPageTextBox"));
        QSizePolicy sizePolicy1(QSizePolicy::MinimumExpanding, QSizePolicy::Fixed);
        sizePolicy1.setHorizontalStretch(0);
        sizePolicy1.setVerticalStretch(0);
        sizePolicy1.setHeightForWidth(firstPageTextBox->sizePolicy().hasHeightForWidth());
        firstPageTextBox->setSizePolicy(sizePolicy1);
        QFont font1;
        font1.setPointSize(12);
        firstPageTextBox->setFont(font1);

        horizontalLayout_5->addWidget(firstPageTextBox);

        horizontalSpacer = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_5->addItem(horizontalSpacer);


        verticalLayout->addLayout(horizontalLayout_5);

        lastPageLabel = new QLabel(widget);
        lastPageLabel->setObjectName(QStringLiteral("lastPageLabel"));
        lastPageLabel->setFont(font);
        lastPageLabel->setAlignment(Qt::AlignCenter);

        verticalLayout->addWidget(lastPageLabel);

        horizontalLayout_6 = new QHBoxLayout();
        horizontalLayout_6->setSpacing(6);
        horizontalLayout_6->setObjectName(QStringLiteral("horizontalLayout_6"));
        horizontalSpacer_4 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_6->addItem(horizontalSpacer_4);

        lastPageTextBox = new QLineEdit(widget);
        lastPageTextBox->setObjectName(QStringLiteral("lastPageTextBox"));
        QSizePolicy sizePolicy2(QSizePolicy::Preferred, QSizePolicy::Fixed);
        sizePolicy2.setHorizontalStretch(0);
        sizePolicy2.setVerticalStretch(0);
        sizePolicy2.setHeightForWidth(lastPageTextBox->sizePolicy().hasHeightForWidth());
        lastPageTextBox->setSizePolicy(sizePolicy2);
        lastPageTextBox->setFont(font1);

        horizontalLayout_6->addWidget(lastPageTextBox);

        horizontalSpacer_2 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_6->addItem(horizontalSpacer_2);


        verticalLayout->addLayout(horizontalLayout_6);

        pagesPerSideLabel = new QLabel(widget);
        pagesPerSideLabel->setObjectName(QStringLiteral("pagesPerSideLabel"));
        pagesPerSideLabel->setFont(font);
        pagesPerSideLabel->setAlignment(Qt::AlignLeading|Qt::AlignLeft|Qt::AlignVCenter);

        verticalLayout->addWidget(pagesPerSideLabel);

        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setSpacing(6);
        horizontalLayout->setObjectName(QStringLiteral("horizontalLayout"));
        pagesPerSideSpinBox = new QSpinBox(widget);
        pagesPerSideSpinBox->setObjectName(QStringLiteral("pagesPerSideSpinBox"));
        QSizePolicy sizePolicy3(QSizePolicy::Minimum, QSizePolicy::Fixed);
        sizePolicy3.setHorizontalStretch(1);
        sizePolicy3.setVerticalStretch(0);
        sizePolicy3.setHeightForWidth(pagesPerSideSpinBox->sizePolicy().hasHeightForWidth());
        pagesPerSideSpinBox->setSizePolicy(sizePolicy3);
        pagesPerSideSpinBox->setFont(font1);
        pagesPerSideSpinBox->setMinimum(1);
        pagesPerSideSpinBox->setMaximum(8);
        pagesPerSideSpinBox->setValue(4);

        horizontalLayout->addWidget(pagesPerSideSpinBox);

        dualPrintButton = new QPushButton(widget);
        dualPrintButton->setObjectName(QStringLiteral("dualPrintButton"));
        QSizePolicy sizePolicy4(QSizePolicy::Minimum, QSizePolicy::Fixed);
        sizePolicy4.setHorizontalStretch(3);
        sizePolicy4.setVerticalStretch(0);
        sizePolicy4.setHeightForWidth(dualPrintButton->sizePolicy().hasHeightForWidth());
        dualPrintButton->setSizePolicy(sizePolicy4);
        QFont font2;
        font2.setPointSize(11);
        dualPrintButton->setFont(font2);
        dualPrintButton->setCheckable(false);
        dualPrintButton->setDefault(false);

        horizontalLayout->addWidget(dualPrintButton);


        verticalLayout->addLayout(horizontalLayout);

        oddLabel = new QLabel(widget);
        oddLabel->setObjectName(QStringLiteral("oddLabel"));
        oddLabel->setFont(font);

        verticalLayout->addWidget(oddLabel);

        horizontalLayout_2 = new QHBoxLayout();
        horizontalLayout_2->setSpacing(6);
        horizontalLayout_2->setObjectName(QStringLiteral("horizontalLayout_2"));
        oddCopy = new QToolButton(widget);
        oddCopy->setObjectName(QStringLiteral("oddCopy"));
        oddCopy->setFocusPolicy(Qt::ClickFocus);
        QIcon icon2;
        icon2.addFile(QStringLiteral(":/img/images/copy.gif"), QSize(), QIcon::Normal, QIcon::Off);
        oddCopy->setIcon(icon2);
        oddCopy->setIconSize(QSize(32, 32));
        oddCopy->setCheckable(false);

        horizontalLayout_2->addWidget(oddCopy);

        oddOutput = new QLineEdit(widget);
        oddOutput->setObjectName(QStringLiteral("oddOutput"));
        oddOutput->setFont(font1);
        oddOutput->setReadOnly(true);

        horizontalLayout_2->addWidget(oddOutput);


        verticalLayout->addLayout(horizontalLayout_2);

        evenLabel = new QLabel(widget);
        evenLabel->setObjectName(QStringLiteral("evenLabel"));
        evenLabel->setFont(font);

        verticalLayout->addWidget(evenLabel);

        horizontalLayout_3 = new QHBoxLayout();
        horizontalLayout_3->setSpacing(6);
        horizontalLayout_3->setObjectName(QStringLiteral("horizontalLayout_3"));
        evenCopy = new QToolButton(widget);
        evenCopy->setObjectName(QStringLiteral("evenCopy"));
        evenCopy->setIcon(icon2);
        evenCopy->setIconSize(QSize(32, 32));
        evenCopy->setCheckable(false);

        horizontalLayout_3->addWidget(evenCopy);

        evenOutput = new QLineEdit(widget);
        evenOutput->setObjectName(QStringLiteral("evenOutput"));
        evenOutput->setFont(font1);
        evenOutput->setReadOnly(true);

        horizontalLayout_3->addWidget(evenOutput);


        verticalLayout->addLayout(horizontalLayout_3);

        horizontalLayout_4 = new QHBoxLayout();
        horizontalLayout_4->setSpacing(6);
        horizontalLayout_4->setObjectName(QStringLiteral("horizontalLayout_4"));
        howToButton = new QPushButton(widget);
        howToButton->setObjectName(QStringLiteral("howToButton"));
        howToButton->setFont(font);

        horizontalLayout_4->addWidget(howToButton);

        aboutButton = new QPushButton(widget);
        aboutButton->setObjectName(QStringLiteral("aboutButton"));
        aboutButton->setFont(font);

        horizontalLayout_4->addWidget(aboutButton);


        verticalLayout->addLayout(horizontalLayout_4);

        MainWindow->setCentralWidget(centralWidget);
        pushButton->raise();
        statusBar = new QStatusBar(MainWindow);
        statusBar->setObjectName(QStringLiteral("statusBar"));
        MainWindow->setStatusBar(statusBar);
#ifndef QT_NO_SHORTCUT
        firstPageLabel->setBuddy(firstPageTextBox);
        lastPageLabel->setBuddy(lastPageTextBox);
        pagesPerSideLabel->setBuddy(pagesPerSideSpinBox);
        oddLabel->setBuddy(oddCopy);
        evenLabel->setBuddy(evenCopy);
#endif // QT_NO_SHORTCUT
        QWidget::setTabOrder(firstPageTextBox, lastPageTextBox);
        QWidget::setTabOrder(lastPageTextBox, pagesPerSideSpinBox);
        QWidget::setTabOrder(pagesPerSideSpinBox, dualPrintButton);
        QWidget::setTabOrder(dualPrintButton, oddOutput);
        QWidget::setTabOrder(oddOutput, evenOutput);
        QWidget::setTabOrder(evenOutput, evenCopy);
        QWidget::setTabOrder(evenCopy, howToButton);
        QWidget::setTabOrder(howToButton, aboutButton);
        QWidget::setTabOrder(aboutButton, pushButton);

        retranslateUi(MainWindow);

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QApplication::translate("MainWindow", "dualPrint, save paper", 0));
        pushButton->setText(QString());
        firstPageLabel->setText(QApplication::translate("MainWindow", "Which would be the first page to print?", 0));
        firstPageTextBox->setText(QApplication::translate("MainWindow", "1", 0));
        lastPageLabel->setText(QApplication::translate("MainWindow", "Which would be the last page to print?", 0));
        lastPageTextBox->setText(QApplication::translate("MainWindow", "12", 0));
        pagesPerSideLabel->setText(QApplication::translate("MainWindow", "How many slides or pages per side?", 0));
        dualPrintButton->setText(QApplication::translate("MainWindow", "Generate Print Sets", 0));
        oddLabel->setText(QApplication::translate("MainWindow", "Odd, set of pages to print first.", 0));
        oddCopy->setText(QString());
        evenLabel->setText(QApplication::translate("MainWindow", "Even, set of pages to print on the back.", 0));
        evenCopy->setText(QString());
        howToButton->setText(QApplication::translate("MainWindow", "Help me print!", 0));
        aboutButton->setText(QApplication::translate("MainWindow", "About dualPrint", 0));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
