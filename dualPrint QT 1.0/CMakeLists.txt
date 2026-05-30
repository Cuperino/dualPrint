# Copyright (C) 2026 Javier O. Cordero Pérez
# SPDX-License-Identifier: GPL-3.0-or-later

cmake_minimum_required(VERSION 3.22)

project(dualPrint
    VERSION 1.1.0
    DESCRIPTION "Assistant for manual duplex printing"
    HOMEPAGE_URL "https://dualprint.org/"
    LANGUAGES CXX)

set(CMAKE_INCLUDE_CURRENT_DIR ON)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_AUTOUIC ON)
set(CMAKE_AUTOMOC ON)

find_package(QT NAMES Qt6 REQUIRED COMPONENTS Core)

find_package(Qt${QT_VERSION_MAJOR} REQUIRED COMPONENTS
    Widgets
)

qt_standard_project_setup()

qt_add_executable(${PROJECT_NAME}
    about.cpp
    about.h
    about.ui
    dpcli.cpp
    dpcli.h
    dualprint.cpp
    dualprint.h
    help.cpp
    help.h
    help.ui
    main.cpp
    mainwindow.ui
    mainwindow.h
    mainwindow.cpp
)

# resources.qrc
qt_add_resources(${PROJECT_NAME} "resources"
    PREFIX "/img"
    FILES
    images/copy.gif
    images/dualprint.gif
    images/header.jpg
    images/help4.jpg
    images/help6.jpg
    images/help0.jpg
    images/help1.jpg
    images/help2.jpg
    images/help3.jpg
    images/help5.jpg
    images/help7.jpg
)

set_target_properties(${PROJECT_NAME} PROPERTIES
    MACOSX_BUNDLE_GUI_IDENTIFIER com.cuperino.dualprint
    MACOSX_BUNDLE_BUNDLE_VERSION ${PROJECT_VERSION}
    MACOSX_BUNDLE_SHORT_VERSION_STRING ${PROJECT_VERSION_MAJOR}.${PROJECT_VERSION_MINOR}
    MACOSX_BUNDLE TRUE
    WIN32_EXECUTABLE TRUE
)

target_link_libraries(${PROJECT_NAME}
    PRIVATE
    Qt${QT_VERSION_MAJOR}::Widgets
)

include(GNUInstallDirs)
install(TARGETS ${PROJECT_NAME}
    BUNDLE DESTINATION .
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
    RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
)

