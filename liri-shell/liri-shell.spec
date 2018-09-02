%global snapdate @DATE@
%global snaphash @HASH@

%define modulename shell

Name:           liri-%{modulename}
Summary:        Liri shell for desktop and mobile
Version:        @VERSION@
Release:        0.1%{?snaphash:.%{snapdate}git%(echo %{snaphash} | cut -c -13)}%{?dist}
License:        GPLv3+
URL:            http://liri.io
Source0:        https://github.com/lirios/%{modulename}/%{?snaphash:archive}%{!?snaphash:releases/download}/%{?snaphash}%{!?snaphash:v%{version}}/%{name}-%{?snaphash}%{!?snaphash:%{version}}.tar.gz

BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5WaylandClient)
BuildRequires:  pkgconfig(Qt5WaylandCompositor)
BuildRequires:  pkgconfig(Qt5Xdg)
BuildRequires:  pkgconfig(Qt5AccountsService)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(polkit-qt5-1)
BuildRequires:  cmake(KF5Solid)
BuildRequires:  pam-devel
BuildRequires:  git
BuildRequires:  qt5-rpm-macros
BuildRequires:  fluid-devel
BuildRequires:  liri-qbs-shared
BuildRequires:  libliri-devel
BuildRequires:  qt5-qtgsettings-devel
BuildRequires:  liri-eglfs-devel

Requires:       qt5-qtsvg
Requires:       qt5-qttools
Requires:       qt5-qtgsettings
Requires:       liri-eglfs
Requires:       libliri
Requires:       fluid
Requires:       dbus
Requires:       pam
Requires:       udisks2
Requires:       upower
Requires:       dconf
Requires:       %{name}-components = %{version}

Suggests:       qml-xwayland

%description
This is the Liri desktop environment shell.


%package components
Summary:        Liri Shell QtQuick components

%description components
This package contains QtQuick components used by Liri Shell that are shared
with the SDDM theme.


%prep
%setup -q -n %{?snaphash:%{modulename}-%{snaphash}}%{!?snaphash:%{name}-%{version}}
qbs setup-toolchains --type gcc /usr/bin/g++ gcc
qbs setup-qt %{_qt5_qmake} qt5
qbs config profiles.qt5.baseProfile gcc


%build
qbs build --no-install -d build %{?_smp_mflags} profile:qt5 \
    projects.Shell.systemdUserUnitDir:%{_userunitdir} \
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


%posttrans
glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :


%postun
if [ $1 -eq 0 ]; then
  glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
fi


%files
%license LICENSE.GPLv3
%doc AUTHORS.md README.md
%{_bindir}/liri-session
%{_bindir}/liri-shell
%{_sysconfdir}/pam.d/liri-shell.pam
%{_sysconfdir}/xdg/menus/*
%{_datadir}/wayland-sessions/*
%{_datadir}/desktop-directories/*
%{_datadir}/glib-2.0/schemas/*
%{_userunitdir}/*
%{_libexecdir}/liri-shell-helper
%{_qt5_qmldir}/Liri/Launcher/
%{_qt5_qmldir}/Liri/Mpris/
%{_qt5_qmldir}/Liri/PolicyKit/
%{_qt5_qmldir}/Liri/Storage/

%files components
%{_qt5_qmldir}/Liri/LoginManager/
%{_qt5_qmldir}/Liri/Shell/
