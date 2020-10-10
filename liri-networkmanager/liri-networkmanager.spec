%undefine __cmake_in_source_build

%global snapdate @DATE@
%global snaphash @HASH@

%define modulename networkmanager

Name:           liri-%{modulename}
Summary:        NetworkManager integration for Liri
Version:        @VERSION@
Release:        0.1%{?snaphash:.%{snapdate}git%(echo %{snaphash} | cut -c -13)}%{?dist}
License:        GPLv3
URL:            https://liri.io
Source0:        https://github.com/lirios/%{modulename}/%{?snaphash:archive}%{!?snaphash:releases/download}/%{?snaphash}%{!?snaphash:v%{version}}/%{name}-%{?snaphash}%{!?snaphash:%{version}}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(gio-2.0) >= 2.31.0
BuildRequires:  pkgconfig(libnm)
BuildRequires:  pkgconfig(ModemManager)
BuildRequires:  pkgconfig(mm-glib)
BuildRequires:  cmake(KF5NetworkManagerQt)
BuildRequires:  cmake(KF5ModemManagerQt)
BuildRequires:  cmake(Liri1Notifications)
BuildRequires:  qt5-linguist
BuildRequires:  liri-rpm-macros

Requires:       fluid

%description
This package provides a QML plugin for NetworkManager,
a settings module to configure networking and an indicator
to access network options from the Liri shell.


%prep
%setup -q -n %{?snaphash:%{modulename}-%{snaphash}}%{!?snaphash:%{name}-%{version}}


%build
%cmake_liri
%cmake_build


%install
%cmake_install


%files
%license LICENSE.GPLv3
%doc AUTHORS.md README.md
%{_datadir}/liri-settings/modules/networkmanager/
%{_datadir}/liri-shell/indicators/networkmanager/
%{_qt5_qmldir}/Liri/NetworkManager/
%{_datadir}/liri-settings/translations/modules/networkmanager_*.qm
