%undefine __cmake_in_source_build

%global snapdate @DATE@
%global snaphash @HASH@

%define modulename text

Name:           liri-%{modulename}
Summary:        Advanced text editor
Version:        @VERSION@
Release:        0.1%{?snaphash:.%{snapdate}git%(echo %{snaphash} | cut -c -13)}%{?dist}
License:        GPLv3+
URL:            https://liri.io
Source0:        https://github.com/lirios/%{modulename}/%{?snaphash:archive}%{!?snaphash:releases/download}/%{?snaphash}%{!?snaphash:v%{version}}/%{name}-%{?snaphash}%{!?snaphash:%{version}}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5QuickControls2)
BuildRequires:  qt5-qttools-devel
BuildRequires:  liri-rpm-macros
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

Requires:       fluid

%description
Advanced text editor built in accordance with Material Design.


%prep
%setup -q -n %{?snaphash:%{modulename}-%{snaphash}}%{!?snaphash:%{name}-%{version}}


%build
%cmake_liri
%cmake_build


%install
%cmake_install


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/io.liri.Text.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/io.liri.Text.appdata.xml


%files
%license LICENSE.GPLv3
%doc AUTHORS.md README.md
%{_bindir}/liri-text
%{_datadir}/liri-text/
%{_datadir}/applications/io.liri.Text.desktop
%{_datadir}/metainfo/io.liri.Text.appdata.xml
%{_datadir}/icons/hicolor/*/*/io.liri.Text.png
