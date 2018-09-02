%define snapdate @DATE@
%define snaphash @HASH@

%define modulename eglfs

Name:           liri-%{modulename}
Summary:        EGL fullscreen platform plugin
Version:        0.10.0
Release:        0.1%{?snaphash:.%{snapdate}git%(echo %{snaphash} | cut -c -13)}%{?dist}
License:        LGPLv3
Url:            https://liri.io
Source0:        https://github.com/lirios/%{modulename}/%{?snaphash:archive}%{!?snaphash:releases/download}/%{?snaphash}%{!?snaphash:v%{version}}/%{name}-%{?snaphash}%{!?snaphash:%{version}}.tar.gz

BuildRequires:  qt5-qtbase-static >= 5.9.0
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Udev)
BuildRequires:  pkgconfig(LiriLogind)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libinput) >= 0.12
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  qt5-rpm-macros
BuildRequires:  liri-qbs-shared

%description
This package includes a Qt platform plugin with support for kms and DRM.


%package devel
Summary:        Development files for %{name}
Group:          Development/System
Requires:       %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


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
rm -f %{buildroot}%{_libdir}/libLiriEdidSupport.a
rm -f %{buildroot}%{_libdir}/libLiriKmsSupport.a
rm -f %{buildroot}%{_libdir}/libLiriLibInput.a
rm -rf %{buildroot}%{_includedir}/LiriEdidSupport/
rm -rf %{buildroot}%{_includedir}/LiriKmsSupport/
rm -rf %{buildroot}%{_includedir}/LiriLibInput/


%post -p /sbin/ldconfig


%postun -p /sbin/ldconfig


%files
%license LICENSE.LGPLv3
%doc AUTHORS.md README.md
%{_qt5_plugindir}/platforms/liblirieglfs.so
%{_qt5_plugindir}/liri/egldeviceintegrations/
%{_libdir}/libLiriEglFSDeviceIntegration.so.*
%{_libdir}/libLiriEglFSKmsSupport.so.*
%{_libdir}/libLiriPlatformHeaders.so.*

%files devel
%{_includedir}/LiriEglFSDeviceIntegration/
%{_includedir}/LiriEglFSKmsSupport/
%{_includedir}/LiriPlatformHeaders/
%{_datadir}/qbs/modules/LiriEglFSDeviceIntegration/
%{_datadir}/qbs/modules/LiriEglFSKmsSupport/
%{_datadir}/qbs/modules/LiriPlatformHeaders/
%{_libdir}/libLiriEglFSDeviceIntegration.so
%{_libdir}/libLiriEglFSKmsSupport.so
%{_libdir}/libLiriPlatformHeaders.so
