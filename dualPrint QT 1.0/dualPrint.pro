#-------------------------------------------------
#
# Project created by QtCreator 2013-06-15T20:04:39
#
#-------------------------------------------------

QT       += core gui

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = dualPrint
TEMPLATE = app

SOURCES += main.cpp\
        mainwindow.cpp \
    dualprint.cpp \
    dpcli.cpp \
    about.cpp

HEADERS  += mainwindow.h \
    dualprint.h \
    dpcli.h \
    about.h

FORMS    += mainwindow.ui \
    about.ui

RESOURCES += \
    resources.qrc
