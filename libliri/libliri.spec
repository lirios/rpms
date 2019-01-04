%global snapdate @DATE@
%global snaphash @HASH@

Name:           libliri
Summary:        Library for Liri applications
Version:        @VERSION@
Release:        0.1%{?snaphash:.%{snapdate}git%(echo %{snaphash} | cut -c -13)}%{?dist}
License:        LGPLv3
Url:            https://liri.io
Source0:        https://github.com/lirios/%{name}/%{?snaphash:archive}%{!?snaphash:releases/download}/%{?snaphash}%{!?snaphash:v%{version}}/%{name}-%{?snaphash}%{!?snaphash:%{version}}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  liri-rpm-macros

%description
Library for all Liri components.


%package devel
Summary:        Development files for %{name}
Group:          Development/System
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -n %{?snaphash:%{name}-%{snaphash}}%{!?snaphash:%{name}-%{version}}


%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_liri} ..
popd
make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}


%files
%license LICENSE.LGPLv3
%doc AUTHORS.md README.md
%{_bindir}/liri-notify
%{_qt5_qmldir}/Liri/Core/
%{_qt5_qmldir}/Liri/Device/
%{_qt5_qmldir}/Liri/Notifications/
%{_qt5_qmldir}/Liri/Xdg/
%{_libdir}/libLiri1Core.so.*
%{_libdir}/libLiri1DBusService.so.*
%{_libdir}/libLiri1LocalDevice.so.*
%{_libdir}/libLiri1Logind.so.*
%{_libdir}/libLiri1Models.so.*
%{_libdir}/libLiri1Notifications.so.*
%{_libdir}/libLiri1Xdg.so.*


%files devel
%{_includedir}/LiriCore/
%{_includedir}/LiriDBusService/
%{_includedir}/LiriLocalDevice/
%{_includedir}/LiriLogind/
%{_includedir}/LiriModels/
%{_includedir}/LiriNotifications/
%{_includedir}/LiriXdg/
%{_libdir}/libLiri1Core.so
%{_libdir}/libLiri1DBusService.so
%{_libdir}/libLiri1LocalDevice.so
%{_libdir}/libLiri1Logind.so
%{_libdir}/libLiri1Models.so
%{_libdir}/libLiri1Notifications.so
%{_libdir}/libLiri1Xdg.so
%{_libdir}/cmake/Liri1Core/
%{_libdir}/cmake/Liri1DBusService/
%{_libdir}/cmake/Liri1LocalDevice/
%{_libdir}/cmake/Liri1Logind/
%{_libdir}/cmake/Liri1Models/
%{_libdir}/cmake/Liri1Notifications/
%{_libdir}/cmake/Liri1Xdg/
%{_libdir}/pkgconfig/Liri1Core.pc
%{_libdir}/pkgconfig/Liri1DBusService.pc
%{_libdir}/pkgconfig/Liri1LocalDevice.pc
%{_libdir}/pkgconfig/Liri1Logind.pc
%{_libdir}/pkgconfig/Liri1Models.pc
%{_libdir}/pkgconfig/Liri1Notifications.pc
%{_libdir}/pkgconfig/Liri1Xdg.pc
