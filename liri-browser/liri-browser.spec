%global snapdate @DATE@
%global snaphash @HASH@

%define modulename browser

Name:           liri-%{modulename}
Summary:        Material Design web browser
Version:        @VERSION@
Release:        0.1%{?snaphash:.%{snapdate}git%(echo %{snaphash} | cut -c -13)}%{?dist}
License:        GPLv3+
URL:            https://liri.io
Source0:        https://github.com/lirios/%{modulename}/%{?snaphash:archive}%{!?snaphash:releases/download}/%{?snaphash}%{!?snaphash:v%{version}}/%{name}-%{?snaphash}%{!?snaphash:%{version}}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(Qt5WebEngine)
BuildRequires:  qt5-qttools-devel
BuildRequires:  fluid-devel
BuildRequires:  liri-qbs-shared
BuildRequires:  desktop-file-utils

Requires:       fluid
Requires:       qt5-qtwebengine

%description
Modern web browser based on QtWebEngine (which is itself based on
the Chromium core, i.e., Blink) and the Qt framework.

Born to use the Material Design, fits very well with
the Liri desktop.


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


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/io.liri.Browser.desktop


%files
%license LICENSE.GPLv3
%doc AUTHORS.md README.md
%{_bindir}/liri-browser
%{_datadir}/applications/io.liri.Browser.desktop
%{_datadir}/icons/hicolor/*/*/io.liri.Browser.png
%{_datadir}/icons/hicolor/*/*/io.liri.Browser.svg
