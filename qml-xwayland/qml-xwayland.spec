Name:           qml-xwayland
Summary:        XWayland support for QML Wayland compositors
Version:        0.10.0
Release:        1%{?dist}
License:        GPLv3
Url:            https://liri.io
Source0:        https://github.com/lirios/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz

BuildRequires:  gcc-c++
BuildRequires:  qt5-qtbase-static >= 5.5.0
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5WaylandCompositor)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(xcb-cursor)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  qt5-rpm-macros
BuildRequires:  liri-qbs-shared

Requires:       xorg-x11-server-Xwayland

%description
This package provides a QML plugin with an XWayland
implementation for Liri Shell.


%prep
%setup -q -n %{name}-%{version}
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
%{_qt5_qmldir}/Liri/XWayland/
