%define snapdate @DATE@
%define snaphash @HASH@

%define modulename wayland

Name:           liri-%{modulename}
Summary:        Wayland client and server libraries for Qt applications
Version:        0.10.0
Release:        0.1%{?snaphash:.%{snapdate}git%(echo %{snaphash} | cut -c -13)}%{?dist}
# Most files are LGPLv2.1+, alternatively GPLv2+ but some are derived from Qt
# which is now LGPLv3, alternatively GPLv2 or GPLv3 or later approved by the KDE Free Qt Foundation.
# Code derived from QtWaylandCompositor is LGPLv3, alternatively GPLv2+.
# Since the KDE Free Qt Foundation might reject future GPL upgrades and we don't have
# a crystal ball, we explicitly state the licenses here.
License:        LGPLv3 or GPLv2 or GPLv3
Url:            https://liri.io
Source0:        https://github.com/lirios/%{modulename}/%{?snaphash:archive}%{!?snaphash:releases/download}/%{?snaphash}%{!?snaphash:v%{version}}/%{name}-%{?snaphash}%{!?snaphash:%{version}}.tar.gz

Requires:       qt5-qtdeclarative
Suggests:       weston >= 1.5
Requires:       xorg-x11-server-Xwayland
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  qt5-qtbase-static >= 5.5.0
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5WaylandClient)
BuildRequires:  pkgconfig(Qt5WaylandCompositor)
BuildRequires:  pkgconfig(Qt5Udev)
BuildRequires:  pkgconfig(LiriLogind)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libinput) >= 0.12
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(xcb-cursor)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  qt5-rpm-macros
BuildRequires:  liri-qbs-shared

%description
Wayland client and server libraries for Qt applications.

This package includes also a platform plugin for QtWayland compositors,
a shell integration to nest the compositor inside another one and
a Material Design client-side decoration for Qt applications,
and an XWayland implementation.


%package devel
Summary:        Development files for %{name}
Group:          Development/System
Requires:       %{name} = %{version}-%{release}
Requires:       liri-qbs-shared

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package -n libliriwayland-client
Summary:        Green Island client library

%description -n libliriwayland-client
Green Island client library.


%package -n libliriwayland-server
Summary:        Green Island server library

%description -n libliriwayland-server
Green Island server library.


%package -n libliriwayland-client-devel
Summary:        Development files for Wayland client applications
Requires:       %{name}-devel = %{version}-%{release}
Requires:       pkgconfig(wayland-client)
Requires:       pkgconfig(wayland-cursor)
Requires:       liri-qbs-shared

%description -n libliriwayland-client-devel
The libliriwayland-client-devel package contains libraries and header files
for developing Wayland client applications with Qt.


%package -n libliriwayland-server-devel
Summary:        Development files for Wayland compositors
Requires:       %{name}-devel = %{version}-%{release}
Requires:       systemd-devel
Requires:       pkgconfig(wayland-client)
Requires:       pkgconfig(wayland-cursor)
Requires:       pkgconfig(wayland-server)
Requires:       pkgconfig(wayland-egl)
Requires:       liri-qbs-shared

%description -n libliriwayland-server-devel
The libliriwayland-server-devel package contains libraries and header files
for developing Wayland compositors with Qt.


%prep
%setup -q -n %{?snaphash:%{modulename}-%{snaphash}}%{!?snaphash:%{name}-%{version}}
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


%post -p /sbin/ldconfig


%postun -p /sbin/ldconfig


%files
%license LICENSE.LGPLv3 LICENSE.GPLv3
%doc AUTHORS.md README.md
%{_qt5_qmldir}/Liri/XWayland/
%{_qt5_plugindir}/platforms/*
%{_qt5_plugindir}/liri/egldeviceintegrations/*

%files devel
%{_includedir}/Liri/LibInput/
%{_includedir}/Liri/UDev/
%{_libdir}/pkgconfig/LiriLibInput.pc
%{_libdir}/pkgconfig/LiriUDev.pc

%files -n libliriwayland-client
%{_libdir}/libLiriWaylandClient.so.*

%files -n libliriwayland-client-devel
%{_includedir}/Liri/WaylandClient/
%{_libdir}/libLiriWaylandClient.so
%{_libdir}/pkgconfig/LiriWaylandClient.pc

%files -n libliriwayland-server
%{_libdir}/libLiriWaylandServer.so.*
%{_qt5_qmldir}/Liri/WaylandServer/

%files -n libliriwayland-server-devel
%{_includedir}/Liri/WaylandServer/
%{_libdir}/libLiriWaylandServer.so
%{_libdir}/pkgconfig/LiriWaylandServer.pc
