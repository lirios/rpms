# This package needs to be rebuilt every time Qt is updated.

%undefine __cmake_in_source_build

%global snapdate @DATE@
%global snaphash @HASH@

%define modulename materialdecoration

Name:           liri-%{modulename}
Summary:        Material Design decoration for Qt applications on Wayland
Version:        @VERSION@
Release:        0.1%{?snaphash:.%{snapdate}git%(echo %{snaphash} | cut -c -13)}%{?dist}
License:        LGPLv3
Url:            https://liri.io
Source0:        https://github.com/lirios/%{modulename}/%{?snaphash:archive}%{!?snaphash:releases/download}/%{?snaphash}%{!?snaphash:v%{version}}/%{name}-%{?snaphash}%{!?snaphash:%{version}}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(Qt5WaylandClient)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  liri-rpm-macros
BuildRequires:  qt5-qtbase-private-devel

%description
Material Design decoration for Qt applications on Wayland.


%prep
%setup -q -n %{?snaphash:%{modulename}-%{snaphash}}%{!?snaphash:%{name}-%{version}}


%build
%cmake_liri
%cmake_build


%install
%cmake_install


%files
%license LICENSE.LGPLv3
%doc AUTHORS.md README.md
%{_qt5_plugindir}/wayland-decoration-client/libmaterialdecoration.so
