# This package needs to be rebuilt every time Qt is updated.

%undefine __cmake_in_source_build

%global snapdate @DATE@
%global snaphash @HASH@

%define modulename qtintegration

Name:           liri-%{modulename}
Summary:        Qt applications integration with the Liri desktop environment
Version:        @VERSION@
Release:        0.1%{?snaphash:.%{snapdate}git%(echo %{snaphash} | cut -c -13)}%{?dist}
License:        GPLv3
Url:            https://liri.io
Source0:        https://github.com/lirios/%{modulename}/%{?snaphash:archive}%{!?snaphash:releases/download}/%{?snaphash}%{!?snaphash:v%{version}}/%{name}-%{?snaphash}%{!?snaphash:%{version}}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6QuickControls2)
BuildRequires:  pkgconfig(Qt6GSettings)
BuildRequires:  kf6-rpm-macros
BuildRequires:  qt6-qtbase-private-devel

%description
Qt applications integration with the Liri desktop environment.


%prep
%setup -q -n %{?snaphash:%{modulename}-%{snaphash}}%{!?snaphash:%{name}-%{version}}


%build
%cmake_kf6 -DFEATURE_qtintegration_material_decoration:BOOL=off
%cmake_build


%install
%cmake_install


%files
%doc AUTHORS.md README.md
%{_kf6_qtplugindir}/platformthemes/liritheme.so
#%{_kf6_qtplugindir}/wayland-decoration-client/materialdecoration.so
