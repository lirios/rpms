%define modulename materialdecoration

Name:           liri-%{modulename}
Summary:        Material Design decoration for Qt applications on Wayland
Version:        1.0.0
Release:        1
License:        LGPLv3
Url:            https://liri.io
Source0:        https://github.com/lirios/%{modulename}/releases/download/v%{version}/%{name}-%{version}.tar.xz

BuildRequires:  pkgconfig(Qt5WaylandClient)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  qt5-rpm-macros
BuildRequires:  liri-qbs-shared

%description
Material Design decoration for Qt applications on Wayland.


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
%{_qt5_plugindir}/wayland-decoration-client/libmaterial.so
