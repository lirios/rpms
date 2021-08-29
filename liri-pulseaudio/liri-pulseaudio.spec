%undefine __cmake_in_source_build

%global snapdate @DATE@
%global snaphash @HASH@

%define modulename pulseaudio

Name:           liri-%{modulename}
Summary:        PulseAudio integration for Liri
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
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libpulse-mainloop-glib)
BuildRequires:  qt5-linguist
BuildRequires:  liri-rpm-macros

Requires:       pulseaudio-daemon
Requires:       fluid

%description
This package provides a QML plugin for PulseAudio,
a settings module to configure sound and an indicator
to access volume and media players from the Liri shell.


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
%{_datadir}/liri-settings/modules/pulseaudio/
%{_datadir}/liri-shell/statusarea/pulseaudio/
%{_qt5_qmldir}/Liri/PulseAudio/
%{_datadir}/liri-settings/translations/modules/pulseaudio_*.qm
