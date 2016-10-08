%define snapdate @DATE@
%define snaphash @HASH@

Name:           greenisland
Summary:        QtQuick-based Wayland compositor in library form
Version:        0.9.0
Release:        0.1%{?snaphash:.%{snapdate}git%(echo %{snaphash} | cut -c -13)}%{?dist}
# Most files are LGPLv2.1+, alternatively GPLv2+ but some are derived from Qt
# which is now LGPLv3, alternatively GPLv2 or GPLv3 or later approved by the KDE Free Qt Foundation.
# Code derived from QtWaylandCompositor is LGPLv3, alternatively GPLv2+.
# Since the KDE Free Qt Foundation might reject future GPL upgrades and we don't have
# a crystal ball, we explicitly state the licenses here.
License:        LGPLv3 or GPLv2 or GPLv3
URL:            http://hawaiios.org
Source0:        https://github.com/greenisland/%{name}/%{?snaphash:archive}%{!?snaphash:releases/download}/%{?snaphash}%{!?snaphash:v%{version}}/%{name}-%{?snaphash}%{!?snaphash:%{version}}.tar.gz

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
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(wayland-egl)
%if 0%{?fedora} >= 24
BuildRequires:  pkgconfig(wayland-protocols)
%endif
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libinput) >= 0.12
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(xcb-cursor)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules

%description
QtQuick-based Wayland compositor in library form.

The API extends QtCompositor with additional features needed by any real world
Wayland compositor.

Green Island offers multiple screen support and it also implements specific
protocols such as xdg-shell, gtk-shell and those for Plasma 5.

Also include a screencaster protocol and command line application, plus a
minimal Wayland compositor written with QML.

Green Island can be used by any desktop environment that wish to implement
its compositor by using QML or for shells deeply integrated with the compositor
in the same process.


%package devel
Summary:        Development files for %{name}
Group:          Development/System
Requires:       %{name} = %{version}-%{release}
Requires:       extra-cmake-modules

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package -n libgreenisland-client
Summary:        Green Island client library

%description -n libgreenisland-client
Green Island client library.


%package -n libgreenisland-server
Summary:        Green Island server library

%description -n libgreenisland-server
Green Island server library.


%package -n libgreenisland-platform
Summary:        Green Island platform library

%description -n libgreenisland-platform
Green Island platform library.


%package -n libgreenisland-client-devel
Summary:        Development files for Wayland client applications
Requires:       %{name}-devel = %{version}-%{release}
Requires:       pkgconfig(wayland-client)
Requires:       pkgconfig(wayland-cursor)

%description -n libgreenisland-client-devel
The libgreenisland-client-devel package contains libraries and header files
for developing Wayland client applications with Qt.


%package -n libgreenisland-server-devel
Summary:        Development files for Wayland compositors
Requires:       %{name}-devel = %{version}-%{release}
Requires:       systemd-devel
Requires:       pkgconfig(wayland-client)
Requires:       pkgconfig(wayland-cursor)
Requires:       pkgconfig(wayland-server)
Requires:       pkgconfig(wayland-egl)
Requires:       libgreenisland-platform-devel = %{version}-%{release}

%description -n libgreenisland-server-devel
The libgreenisland-server-devel package contains libraries and header files
for developing Wayland compositors with Qt.


%package -n libgreenisland-platform-devel
Summary:        Development files for Green Island platform applications
Requires:       %{name}-devel = %{version}-%{release}
Requires:       pkgconfig(gio-2.0)
Requires:       pkgconfig(xkbcommon)

%description -n libgreenisland-platform-devel
The libgreenisland-server-devel package contains libraries and header files
for developing Wayland compositors with Qt.


%prep
%setup -q -n %{?snaphash:%{name}-%{snaphash}}%{!?snaphash:%{name}-%{version}}


%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%if 0%{?fedora} < 24
%{cmake_kf5} -DUSE_LOCAL_WAYLAND_PROTOCOLS:BOOL=ON ..
%else
%{cmake_kf5} ..
%endif
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}


%post -p /sbin/ldconfig


%postun -p /sbin/ldconfig


%files
%license LICENSE.LGPLv3 LICENSE.GPLv3
%doc AUTHORS.md CONTRIBUTORS.md README.md
%{_bindir}/greenisland
%{_bindir}/greenisland-launcher
%{_bindir}/greenisland-screencaster
%{_kf5_qmldir}/GreenIsland/
%{_qt5_plugindir}/greenisland/
%{_qt5_plugindir}/platforms/*
%{_datadir}/greenisland/

%files devel
%{_bindir}/greenisland-wayland-scanner
%{_includedir}/Hawaii/GreenIsland/
%{_includedir}/Hawaii/greenisland_version.h
%{_libdir}/cmake/GreenIsland/

%files -n libgreenisland-client
%{_libdir}/libGreenIslandClient.so.*

%files -n libgreenisland-client-devel
%{_includedir}/Hawaii/GreenIsland/client/
%{_includedir}/Hawaii/GreenIsland/Client/
%{_libdir}/libGreenIslandClient.so
%{_libdir}/cmake/GreenIslandClient/
#{_libdir}/pkgconfig/GreenIslandClient.pc
%{_kf5_archdatadir}/mkspecs/modules/qt_GreenIslandClient.pri

%files -n libgreenisland-server
%{_libdir}/libGreenIslandCompositor.so.*
%{_libdir}/libGreenIslandServer.so.*

%files -n libgreenisland-server-devel
%{_includedir}/Hawaii/GreenIsland/QtWaylandCompositor/
%{_includedir}/Hawaii/GreenIsland/server/
%{_includedir}/Hawaii/GreenIsland/Server/
%{_libdir}/libGreenIslandCompositor.so
%{_libdir}/libGreenIslandServer.so
%{_libdir}/cmake/GreenIslandCompositor/
%{_libdir}/cmake/GreenIslandServer/
#{_libdir}/pkgconfig/GreenIslandCompositor.pc
#{_libdir}/pkgconfig/GreenIslandServer.pc
%{_kf5_archdatadir}/mkspecs/modules/qt_GreenIslandCompositor.pri
%{_kf5_archdatadir}/mkspecs/modules/qt_GreenIslandServer.pri

%files -n libgreenisland-platform
%{_libdir}/libGreenIslandPlatform.so.*

%files -n libgreenisland-platform-devel
%{_includedir}/Hawaii/GreenIsland/platform/
%{_includedir}/Hawaii/GreenIsland/Platform/
%{_libdir}/cmake/GreenIslandPlatform/
%{_libdir}/libGreenIslandPlatform.so
%{_kf5_archdatadir}/mkspecs/modules/qt_GreenIslandPlatform.pri
#{_libdir}/pkgconfig/GreenIslandPlatform.pc


%changelog
* Sat Sep 17 2016 Pier Luigi Fiorini <pierluigi.fiorini@gmail.com> - 0.9.0-1
- Initial packaging.
