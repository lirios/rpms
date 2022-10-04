%undefine __cmake_in_source_build

%define snapdate @DATE@
%define snaphash @HASH@

Name:           aurora-compositor
Summary:        Wayland compositor library for Qt applications
Version:        @VERSION@
Release:        0.1%{?snaphash:.%{snapdate}git%(echo %{snaphash} | cut -c -13)}%{?dist}
License:        LGPLv3
Url:            https://liri.io
Source0:        https://github.com/lirios/%{name}/%{?snaphash:archive}%{!?snaphash:releases/download}/%{?snaphash}%{!?snaphash:v%{version}}/%{name}-%{?snaphash}%{!?snaphash:%{version}}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  qt5-qtbase-static >= 5.9.0
BuildRequires:  qt5-qtbase-private-devel
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libinput) >= 0.12
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(xcb-cursor)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  liri-rpm-macros
BuildRequires:  aurora-scanner

%description
Wayland compositor library for Qt applications.


%package devel
Summary:        Development files for %{name}
Group:          Development/System
Requires:       %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -n %{?snaphash:%{name}-%{snaphash}}%{!?snaphash:%{name}-%{version}}


%build
%cmake_liri
%cmake_build


%install
%cmake_install


%post -p /sbin/ldconfig


%postun -p /sbin/ldconfig


%files
%doc README
%{_libdir}/libLiri1AuroraXkbCommonSupport.so.*
%{_libdir}/libLiri1AuroraCompositor.so.*
%{_libdir}/libLiri1AuroraPlatformHeaders.so.*
%{_libdir}/libLiri1AuroraLogind.so.*
%{_libdir}/libLiri1AuroraUdev.so.*
%{_libdir}/libLiri1AuroraLibInput.so.*
%{_libdir}/libLiri1EglFSDeviceIntegration.so.*
%{_libdir}/libLiri1EglFSKmsSupport.so.*
%{_qt5_plugindir}/aurora/wayland-graphics-integration-server/
%{_qt5_qmldir}/Aurora/Compositor/
%{_qt5_plugindir}/platforms/liblirieglfs.so
%{_qt5_plugindir}/liri/egldeviceintegrations/

%files devel
%{_includedir}/LiriAuroraXkbCommonSupport/
%{_libdir}/libLiri1AuroraXkbCommonSupport.so
%{_libdir}/cmake/Liri1AuroraXkbCommonSupport/
%{_libdir}/pkgconfig/Liri1AuroraXkbCommonSupport.pc
%{_includedir}/LiriAuroraCompositor/
%{_libdir}/libLiri1AuroraCompositor.so
%{_libdir}/cmake/Liri1AuroraCompositor/
%{_libdir}/pkgconfig/Liri1AuroraCompositor.pc
%{_includedir}/LiriAuroraPlatformHeaders/
%{_libdir}/libLiri1AuroraPlatformHeaders.so
%{_libdir}/cmake/Liri1AuroraPlatformHeaders/
%{_libdir}/pkgconfig/Liri1AuroraPlatformHeaders.pc
%{_includedir}/LiriAuroraLogind/
%{_libdir}/libLiri1AuroraLogind.so
%{_includedir}/LiriAuroraUdev/
%{_libdir}/libLiri1AuroraUdev.so
%{_includedir}/LiriAuroraLibInput/
%{_libdir}/libLiri1AuroraLibInput.so
%{_includedir}/LiriAuroraEdidSupport/
%{_libdir}/libLiri1AuroraEdidSupport.a
%{_includedir}/LiriAuroraKmsSupport/
%{_libdir}/libLiri1AuroraKmsSupport.a
%{_includedir}/LiriEglFSDeviceIntegration/
%{_libdir}/libLiri1EglFSDeviceIntegration.so
%{_includedir}/LiriEglFSKmsSupport/
%{_libdir}/libLiri1EglFSKmsSupport.so
