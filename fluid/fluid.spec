%undefine __cmake_in_source_build

%global snapdate @DATE@
%global snaphash @HASH@

Name:           fluid
Summary:        Library for QtQuick apps with Material Design
Version:        @VERSION@
Release:        0.1%{?snaphash:.%{snapdate}git%(echo %{snaphash} | cut -c -13)}%{?dist}
License:        MPLv2
Url:            https://liri.io
Source0:        https://github.com/lirios/%{name}/%{?snaphash:archive}%{!?snaphash:releases/download}/%{?snaphash}%{!?snaphash:v%{version}}/%{name}-%{?snaphash}%{!?snaphash:%{version}}.tar.gz

Requires:       qt6-qt5compat
Requires:       qt6-qtsvg

BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Svg)
BuildRequires:  pkgconfig(Qt6Qml)
BuildRequires:  pkgconfig(Qt6Quick)
BuildRequires:  pkgconfig(Qt6QuickControls2)
BuildRequires:  pkgconfig(Qt6Network)
BuildRequires:  pkgconfig(Qt6WaylandClient)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  liri-rpm-macros
BuildRequires:  kf6-rpm-macros
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  qt6-doctools
BuildRequires:  qt6-qtbase-private-devel

%description
Library for fluid and dynamic development of QtQuick apps
with the Material Design language.


%prep
%setup -q -n %{?snaphash:%{name}-%{snaphash}}%{!?snaphash:%{name}-%{version}}


%build
%cmake_kf6
%cmake_build


%install
%cmake_install


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/*.appdata.xml


%files
%license LICENSE.MPL2
%doc AUTHORS.md README.md
%{_kf6_bindir}/fluid-demo
%{_kf6_qmldir}/Fluid/
%{_kf6_metainfodir}/io.liri.Fluid.Demo.appdata.xml
%{_datadir}/applications/io.liri.Fluid.Demo.desktop
%{_datadir}/icons/hicolor/*/apps/io.liri.Fluid.Demo.png
%{_datadir}/icons/hicolor/scalable/apps/io.liri.Fluid.Demo.svg
%{_datadir}/doc/fluid/html/
