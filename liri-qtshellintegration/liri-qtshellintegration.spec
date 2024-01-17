# This package needs to be rebuilt every time Qt is updated.

%undefine __cmake_in_source_build

%global snapdate @DATE@
%global snaphash @HASH@

%define modulename qtshellintegration

Name:           liri-%{modulename}
Summary:        Integration between Wayland shell protocols and Qt applications
Version:        @VERSION@
Release:        0.1%{?snaphash:.%{snapdate}git%(echo %{snaphash} | cut -c -13)}%{?dist}
License:        GPLv3
Url:            https://liri.io
Source0:        https://github.com/lirios/%{modulename}/%{?snaphash:archive}%{!?snaphash:releases/download}/%{?snaphash}%{!?snaphash:v%{version}}/%{name}-%{?snaphash}%{!?snaphash:%{version}}.tar.gz

BuildRequires:  pkgconfig(Qt6WaylandClient)
BuildRequires:  pkgconfig(Qt6Qml)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  kf6-rpm-macros
BuildRequires:  liri-cmake-shared
BuildRequires:  qt6-qtbase-private-devel

%description
Qt applications integration with the Liri desktop environment.


%package devel
Summary:  Developer files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: cmake(Qt6Gui)

%description devel
%{summary}.


%prep
%setup -q -n %{?snaphash:%{modulename}-%{snaphash}}%{!?snaphash:%{name}-%{version}}


%build
%cmake_kf6
%cmake_build


%install
%cmake_install


%files
%license LICENSES/*
%doc AUTHORS.md README.md
%{_libdir}/libLiri1QtShellIntegration.so.*
%{_kf6_qmldir}/Liri/QtShellIntegration/
%{_qt6_plugindir}/wayland-shell-integration/

%files devel
%{_includedir}/LiriQtShellIntegration/
%{_libdir}/libLiri1QtShellIntegration.so
%{_libdir}/cmake/Liri1QtShellIntegration/
