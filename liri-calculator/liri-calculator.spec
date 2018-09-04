%define modulename calculator

Name:           liri-%{modulename}
Summary:        Material Design calculator
Version:        1.1.0
Release:        1%{?dist}
License:        GPLv3+
URL:            http://liri.io
Source0:        https://github.com/lirios/%{modulename}/releases/download/v%{version}/%{name}-%{version}.tar.xz

BuildRequires:  qt5-qttools-devel
BuildRequires:  fluid-devel
BuildRequires:  liri-qbs-shared
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

Requires:       fluid

%description
Material Design calculator.


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


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/io.liri.Calculator.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/io.liri.Calculator.appdata.xml


%files
%license LICENSE.GPLv3
%doc README.md
%{_bindir}/liri-calculator
%{_datadir}/applications/io.liri.Calculator.desktop
%{_datadir}/metainfo/io.liri.Calculator.appdata.xml
%{_datadir}/icons/hicolor/*/*/io.liri.Calculator.png


%changelog
* Tue Sep 04 2018 Pier Luigi Fiorini <pierluigi.fiorini@gmail.com> - 1.1.0-1
- Initial packaging
