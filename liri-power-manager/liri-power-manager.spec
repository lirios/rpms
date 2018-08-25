%global snapdate @DATE@
%global snaphash @HASH@

%define modulename power-manager

Name:           liri-%{modulename}
Summary:        Manages the power consumption settings of Liri Shell
Version:        @VERSION@
Release:        0.1%{?snaphash:.%{snapdate}git%(echo %{snaphash} | cut -c -13)}%{?dist}
License:        GPLv3+
URL:            http://liri.io
Source0:        https://github.com/lirios/%{modulename}/%{?snaphash:archive}%{!?snaphash:releases/download}/%{?snaphash}%{!?snaphash:v%{version}}/%{name}-%{?snaphash}%{!?snaphash:%{version}}.tar.gz

BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(gio-2.0) >= 2.31.0
BuildRequires:  pkgconfig(Qt5GSettings)
BuildRequires:  pkgconfig(LiriCore)
BuildRequires:  cmake(KF5Solid)
BuildRequires:  qt5-qttools
BuildRequires:  qt5-qttools-devel
BuildRequires:  qt5-rpm-macros
BuildRequires:  liri-qbs-shared
BuildRequires:  fluid-devel
BuildRequires:  desktop-file-utils

Requires:       fluid
Requires:       qt5-qtgsettings

%description
This package contains a daemon for power management and a
settings module to configure power consumption settings.


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
%find_lang %{name} --all-name --with-qt


%check
desktop-file-validate %{buildroot}%{_sysconfdir}/xdg/autostart/liri-power-manager.desktop


%posttrans
glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :


%postun
if [ $1 -eq 0 ]; then
  glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
fi


%files -f %{name}.lang
%license LICENSE.GPLv3
%doc AUTHORS.md README.md
%{_bindir}/liri-power-manager
%{_sysconfdir}/xdg/autostart/liri-power-manager.desktop
%{_datadir}/glib-2.0/schemas/*
%{_datadir}/liri-settings/modules/power/
%{_datadir}/liri-settings/translations/modules/power_*.qm
%{_datadir}/liri-shell/indicators/power/
%{_qt5_qmldir}/Liri/Power/
