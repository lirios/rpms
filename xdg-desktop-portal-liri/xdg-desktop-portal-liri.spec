# Version required for Session support.
%global xdg_desktop_portal_version 0.10

%global snapdate @DATE@
%global snaphash @HASH@

Name:           xdg-desktop-portal-liri
Summary:        Backend implementation for xdg-desktop-portal for Liri
Version:        @VERSION@
Release:        0.1%{?snaphash:.%{snapdate}git%(echo %{snaphash} | cut -c -13)}%{?dist}
License:        GPLv3+
URL:            https://liri.io
Source0:        https://github.com/lirios/%{name}/%{?snaphash:archive}%{!?snaphash:releases/download}/%{?snaphash}%{!?snaphash:v%{version}}/%{name}-%{?snaphash}%{!?snaphash:%{version}}.tar.gz

BuildRequires:  pkgconfig(xdg-desktop-portal) >= %{xdg_desktop_portal_version}
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  qt5-rpm-macros
BuildRequires:  liri-qbs-shared
BuildRequires:  fluid-devel
BuildRequires:  libliri-devel

Requires:       xdg-desktop-portal >= %{xdg_desktop_portal_version}
Requires:       fluid
Requires:       libliri

%description
A backend implementation for xdg-desktop-portal that is using Qt and various
pieces of Liri libraries and infrastructure.


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
%license LICENSE.GPLv3
%doc AUTHORS.md README.md
%{_libexecdir}/xdg-desktop-portal-liri
%{_datadir}/xdg-desktop-portal/portals/liri.portal
%{_datadir}/dbus-1/services/org.freedesktop.impl.portal.desktop.liri.service
