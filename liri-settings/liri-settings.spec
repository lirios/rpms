%undefine __cmake_in_source_build

%global snapdate @DATE@
%global snaphash @HASH@

%define modulename settings

Name:           liri-%{modulename}
Summary:        Utilities to configure the Liri desktop environment
Version:        @VERSION@
Release:        0.1%{?snaphash:.%{snapdate}git%(echo %{snaphash} | cut -c -13)}%{?dist}
License:        GPLv3+
URL:            https://liri.io
Source0:        https://github.com/lirios/%{modulename}/%{?snaphash:archive}%{!?snaphash:releases/download}/%{?snaphash}%{!?snaphash:v%{version}}/%{name}-%{?snaphash}%{!?snaphash:%{version}}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5QuickControls2)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(polkit-qt5-1)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  cmake(Liri1Xdg)
BuildRequires:  qt5-qttools
BuildRequires:  qt5-qttools-devel
BuildRequires:  liri-rpm-macros
BuildRequires:  desktop-file-utils

Requires:       qt5-qtaccountsservice
Requires:       qt5-qtgsettings
Requires:       polkit-qt5-1
Requires:       fluid
Requires:       xkeyboard-config
Requires:       dconf


%description
This package contains configuration utilities for the Liri desktop, which
allow to configure various settings including desktop fonts, keyboard and
mouse properties, sound setup, desktop theme and background, user interface
properties, screen resolution, and other settings.


%prep
%setup -q -n %{?snaphash:%{modulename}-%{snaphash}}%{!?snaphash:%{name}-%{version}}


%build
%cmake_liri
%cmake_build


%install
%cmake_install

%find_lang %{name} --all-name --with-qt


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/io.liri.Settings.desktop


%files -f %{name}.lang
%license LICENSE.GPLv3
%doc AUTHORS.md README.md
%{_bindir}/liri-settings
%{_datadir}/liri-settings/
%{_datadir}/applications/io.liri.Settings.desktop
%{_datadir}/dbus-1/services/io.liri.Settings.service
%{_qt5_qmldir}/Liri/Settings/
