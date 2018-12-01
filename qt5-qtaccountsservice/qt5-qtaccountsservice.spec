%global snapdate @DATE@
%global snaphash @HASH@

%global qt_module qtaccountsservice

Name:           qt5-%{qt_module}
Summary:        Qt5 - AccountService addon
Version:        @VERSION@
Release:        0.1%{?snaphash:.%{snapdate}git%(echo %{snaphash} | cut -c -13)}%{?dist}

License:        LGPLv3+
Url:            https://liri.io
Source0:        https://github.com/lirios/%{qt_module}/%{?snaphash:archive}%{!?snaphash:releases/download}/%{?snaphash}%{!?snaphash:v%{version}}/%{qt_module}-%{?snaphash}%{!?snaphash:%{version}}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  liri-rpm-macros

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
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_liri} ..
popd
make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}


%post -p /sbin/ldconfig


%postun -p /sbin/ldconfig


%files
%license LICENSE.LGPLv3
%doc AUTHORS.md README.md
%{_libdir}/libQt5AccountsService.so.*
%{_qt5_qmldir}/QtAccountsService/


%files devel
%{_includedir}/Qt5AccountsService/
%{_libdir}/libQt5AccountsService.so
%{_libdir}/cmake/Qt5AccountsService/
%{_libdir}/pkgconfig/Qt5AccountsService.pc
