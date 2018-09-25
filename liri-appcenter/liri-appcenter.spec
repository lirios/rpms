%global snapdate @DATE@
%global snaphash @HASH@

%define modulename appcenter

Name:           liri-%{modulename}
Summary:        Software center for Liri
Version:        @VERSION@
Release:        0.1%{?snaphash:.%{snapdate}git%(echo %{snaphash} | cut -c -13)}%{?dist}
License:        GPLv3+
URL:            https://liri.io
Source0:        https://github.com/lirios/%{modulename}/%{?snaphash:archive}%{!?snaphash:releases/download}/%{?snaphash}%{!?snaphash:v%{version}}/%{name}-%{?snaphash}%{!?snaphash:%{version}}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  qt5-qttools-devel
BuildRequires:  fluid-devel
BuildRequires:  libliri-devel
BuildRequires:  pkgconfig(flatpak)
BuildRequires:  cmake(AppStreamQt)
BuildRequires:  liri-qbs-shared
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

Requires:       fluid
Requires:       libliri
Requires:       qt5-qtgsettings
Requires:       dconf

%description
Software center for Liri.


%package devel
Summary:    Development files for %{name}
Requires:   %{name}%{?isa} = %{version}-%{release}

%description devel
Files for development of Liri AppCenter plugins.


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
desktop-file-validate %{buildroot}%{_datadir}/applications/io.liri.AppCenter{,.Flatpak}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/io.liri.AppCenter.appdata.xml


%post -p /sbin/ldconfig


%postun -p /sbin/ldconfig


%files
%license LICENSE.GPLv3 LICENSE.LGPLv3
%doc AUTHORS.md README.md
%{_bindir}/liri-appcenter
%{_bindir}/liri-update-notifier
%{_datadir}/applications/io.liri.AppCenter.desktop
%{_datadir}/applications/io.liri.AppCenter.Flatpak.desktop
%{_datadir}/metainfo/io.liri.AppCenter.appdata.xml
%{_libdir}/libLiriAppCenter.so.*
%{_qt5_qmldir}/Liri/AppCenter/
%{_qt5_plugindir}/liri/appcenter/


%files devel
%{_includedir}/LiriAppCenter/
%{_datadir}/qbs/modules/LiriAppCenter/
%{_libdir}/libLiriAppCenter.so
%{_libdir}/cmake/LiriAppCenter/
%{_libdir}/pkgconfig/LiriAppCenter.pc
