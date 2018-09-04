Name:           fluid
Summary:        Library for QtQuick apps with Material Design
Version:        1.0.0
Release:        3%{?dist}
License:        MPLv2
Url:            https://liri.io
Source0:        https://github.com/lirios/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz

Requires:       qt5-qtgraphicaleffects
Requires:       qt5-qtquickcontrols2
Requires:       qt5-qtsvg

BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5QuickControls2)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  qt5-rpm-macros
BuildRequires:  liri-qbs-shared
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

%description
Library for fluid and dynamic development of QtQuick apps
with the Material Design language.


%package devel
Summary:        Development files for %{name}
Group:          Development/System
Requires:       %{name} = %{version}-%{release}
Requires:       qt5-qtdeclarative-devel%{?_isa}
Requires:       qt5-qtquickcontrols2-devel%{?_isa}
Requires:       qt5-qtsvg-devel%{?_isa}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -n %{name}-%{version}
qbs setup-toolchains --type gcc /usr/bin/g++ gcc
qbs setup-qt %{_qt5_qmake} qt5
qbs config profiles.qt5.baseProfile gcc


%build
qbs build --no-install -d build %{?_smp_mflags} profile:qt5 \
    project.withDocumentation:false \
    project.useSystemQbsShared:true \
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
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.appdata.xml


%files
%license LICENSE.MPL2
%doc AUTHORS.md README.md
%{_bindir}/fluid-demo
%{_qt5_qmldir}/Fluid/
%{_datadir}/metainfo/io.liri.Fluid.Demo.appdata.xml
%{_datadir}/applications/io.liri.Fluid.Demo.desktop


%files devel
%{_datadir}/qbs/modules/Fluid/


%changelog
* Tue Sep 04 2018 Pier Luigi Fiorini <pierluigi.fiorini@gmail.com> - 1.0.0-3
- Add missing dependencies
