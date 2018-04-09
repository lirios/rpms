%define modulename terminal

Name:           liri-%{modulename}
Summary:        Terminal emulator for the Liri desktop environment
Version:        0.2.0
Release:        1%{?dist}
License:        GPLv3+
URL:            http://liri.io
Source0:        https://github.com/lirios/%{modulename}/releases/download/v%{version}/%{name}-%{version}.tar.xz

BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  liri-qbs-shared
BuildRequires:  fluid-devel
BuildRequires:  desktop-file-utils

Requires:       fluid


%description
This package contains a terminal emulator for the Liri desktop environment.


%prep
%setup -q -n %{name}-%{version}
qbs setup-toolchains --type gcc /usr/bin/g++ gcc
qbs setup-qt %{_qt5_qmake} qt5


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


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%posttrans
glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :


%postun
if [ $1 -eq 0 ]; then
  glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
fi


%files
%license LICENSE.GPLv3
%doc AUTHORS.md README.md
%{_bindir}/liri-terminal
%{_datadir}/appdata/*.appdata.xml
%{_datadir}/applications/*.desktop
%{_qt5_qmldir}/Liri/Terminal/
