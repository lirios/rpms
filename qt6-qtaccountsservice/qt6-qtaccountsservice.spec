%undefine __cmake_in_source_build

%global snapdate @DATE@
%global snaphash @HASH@

%global qt_module qtaccountsservice

Name:           qt6-%{qt_module}
Summary:        Qt6 - AccountService addon
Version:        @VERSION@
Release:        0.1%{?snaphash:.%{snapdate}git%(echo %{snaphash} | cut -c -13)}%{?dist}

License:        LGPLv3+
Url:            https://liri.io
Source0:        https://github.com/lirios/%{qt_module}/%{?snaphash:archive}%{!?snaphash:releases/download}/%{?snaphash}%{!?snaphash:v%{version}}/%{qt_module}-%{?snaphash}%{!?snaphash:%{version}}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6DBus)
BuildRequires:  pkgconfig(Qt6Network)
BuildRequires:  pkgconfig(Qt6Qml)
BuildRequires:  pkgconfig(Qt6Quick)
BuildRequires:  liri-cmake-shared

%description
Qt-style API for freedesktop.org's AccountsService DBus service (see 
http://www.freedesktop.org/wiki/Software/AccountsService).


%package devel
Summary:    Development files for Qt Account Service Addon
Requires:   %{name}%{?isa} = %{version}-%{release}

%description devel
Files for development using Qt Account Service Addon.


%prep
%setup -q -n %{?snaphash:%{qt_module}-%{snaphash}}%{!?snaphash:%{qt_module}-%{version}}


%build
%cmake_kf6
%cmake_build


%install
%cmake_install


%post -p /sbin/ldconfig


%postun -p /sbin/ldconfig


%files
%license LICENSE.LGPLv3
%doc AUTHORS.md README.md
%{_libdir}/libQt6AccountsService.so.*
%{_kf6_qmldir}/QtAccountsService/


%files devel
%{_includedir}/Qt6AccountsService/
%{_libdir}/libQt6AccountsService.so
%{_libdir}/cmake/Qt6AccountsService/
%{_libdir}/pkgconfig/Qt6AccountsService.pc
