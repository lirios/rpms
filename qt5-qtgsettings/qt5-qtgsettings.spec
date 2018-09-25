%global snapdate @DATE@
%global snaphash @HASH@

%global qt_module qtgsettings

Name:           qt5-%{qt_module}
Summary:        Qt5 - GSettings addon
Version:        @VERSION@
Release:        0.1%{?snaphash:.%{snapdate}git%(echo %{snaphash} | cut -c -13)}%{?dist}

License:        LGPLv3+
Url:            https://liri.io
Source0:        https://github.com/lirios/%{qt_module}/%{?snaphash:archive}%{!?snaphash:releases/download}/%{?snaphash}%{!?snaphash:v%{version}}/%{qt_module}-%{?snaphash}%{!?snaphash:%{version}}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-rpm-macros
BuildRequires:  liri-qbs-shared

Requires:       dconf

%description
Qt-style API wrapper for GSettings.


%package devel
Summary:    Development files for %{name}
Requires:   %{name}%{?isa} = %{version}-%{release}
Requires:   liri-qbs-shared

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -n %{?snaphash:%{qt_module}-%{snaphash}}%{!?snaphash:%{qt_module}-%{version}}
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
%license LICENSE.LGPLv3
%doc AUTHORS.md README.md
%{_libdir}/libQt5GSettings.so.*
%{_qt5_qmldir}/QtGSettings/


%files devel
%{_includedir}/Qt5GSettings/
%{_datadir}/qbs/modules/Qt5GSettings/
%{_libdir}/libQt5GSettings.so
%{_libdir}/cmake/Qt5GSettings/
%{_libdir}/pkgconfig/Qt5GSettings.pc
