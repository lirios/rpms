%global snapdate @DATE@
%global snaphash @HASH@

Name:           libliri
Summary:        Library for Liri applications
Version:        0.9.0
Release:        0.1%{?snaphash:.%{snapdate}git%(echo %{snaphash} | cut -c -13)}%{?dist}
License:        LGPLv3
Url:            https://liri.io
Source0:        https://github.com/lirios/%{name}/%{?snaphash:archive}%{!?snaphash:releases/download}/%{?snaphash}%{!?snaphash:v%{version}}/%{name}-%{?snaphash}%{!?snaphash:%{version}}.tar.gz

Requires:       qt5-qtdeclarative

BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5Xdg)
BuildRequires:  qt5-rpm-macros
BuildRequires:  liri-qbs-shared

%description
Library for all Liri components.


%package devel
Summary:        Development files for %{name}
Group:          Development/System
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qbs

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -n %{?snaphash:%{name}-%{snaphash}}%{!?snaphash:%{name}-%{version}}
qbs setup-toolchains --type gcc /usr/bin/g++ gcc
qbs setup-qt %{_qt5_qmake} qt5
qbs config profiles.qt5.baseProfile gcc


%build
qbs build --no-install -d build %{?_smp_mflags} profile:qt5 \
    modules.lirideployment.prefix:%{_prefix} \
    modules.lirideployment.etcDir:%{_sysconfdir} \
    modules.lirideployment.binDir:%{_bindir} \
    modules.lirideployment.sbinDir:%{_sbindir} \
    modules.lirideployment.libDir:%{_libdir} \
    modules.lirideployment.libexecDir:%{_libexecdir} \
    modules.lirideployment.includeDir:%{_includedir} \
    modules.lirideployment.dataDir:%{_datadir} \
    modules.lirideployment.docDir:%{_docdir} \
    modules.lirideployment.manDir:%{_mandir} \
    modules.lirideployment.infoDir:%{_infodir} \
    modules.lirideployment.qmlDir:%{_qt5_qmldir} \
    modules.lirideployment.pluginsDir:%{_qt5_plugindir}


%install
qbs install --no-build -d build -v --install-root %{buildroot} profile:qt5


%files
%license LICENSE.LGPLv3
%doc AUTHORS.md README.md
%{_bindir}/liri-notify
%{_qt5_qmldir}/Liri/Core/
%{_qt5_qmldir}/Liri/Device/
%{_qt5_qmldir}/Liri/Notifications/
%{_libdir}/libLiriCore.so.*
%{_libdir}/libLiriDBusService.so.*
%{_libdir}/libLiriLocalDevice.so.*
%{_libdir}/libLiriLogind.so.*
%{_libdir}/libLiriModels.so.*
%{_libdir}/libLiriNotifications.so.*


%files devel
%{_includedir}/LiriCore/
%{_includedir}/LiriDBusService/
%{_includedir}/LiriLocalDevice/
%{_includedir}/LiriLogind/
%{_includedir}/LiriModels/
%{_includedir}/LiriNotifications/
%{_libdir}/libLiriCore.so
%{_libdir}/libLiriDBusService.so
%{_libdir}/libLiriLocalDevice.so
%{_libdir}/libLiriLogind.so
%{_libdir}/libLiriModels.so
%{_libdir}/libLiriNotifications.so
%{_datadir}/qbs/modules/LiriCore/
%{_datadir}/qbs/modules/LiriDBusService/
%{_datadir}/qbs/modules/LiriLocalDevice/
%{_datadir}/qbs/modules/LiriLogind/
%{_datadir}/qbs/modules/LiriModels/
%{_datadir}/qbs/modules/LiriNotifications/
%{_libdir}/cmake/LiriCore/
%{_libdir}/cmake/LiriDBusService/
%{_libdir}/cmake/LiriLocalDevice/
%{_libdir}/cmake/LiriLogind/
%{_libdir}/cmake/LiriModels/
%{_libdir}/cmake/LiriNotifications/
%{_libdir}/pkgconfig/LiriCore.pc
%{_libdir}/pkgconfig/LiriDBusService.pc
%{_libdir}/pkgconfig/LiriLocalDevice.pc
%{_libdir}/pkgconfig/LiriLogind.pc
%{_libdir}/pkgconfig/LiriModels.pc
%{_libdir}/pkgconfig/LiriNotifications.pc
