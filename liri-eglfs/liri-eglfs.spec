%define snapdate @DATE@
%define snaphash @HASH@

%define modulename eglfs

Name:           liri-%{modulename}
Summary:        EGL fullscreen platform plugin
Version:        @VERSION@
Release:        0.1%{?snaphash:.%{snapdate}git%(echo %{snaphash} | cut -c -13)}%{?dist}
License:        LGPLv3
Url:            https://liri.io
Source0:        https://github.com/lirios/%{modulename}/%{?snaphash:archive}%{!?snaphash:releases/download}/%{?snaphash}%{!?snaphash:v%{version}}/%{name}-%{?snaphash}%{!?snaphash:%{version}}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  qt5-qtbase-static >= 5.9.0
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Udev)
BuildRequires:  pkgconfig(Liri1Logind)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libinput) >= 0.12
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  liri-rpm-macros
%if 0%{?fedora} >= 30
BuildRequires:  qt5-qtbase-private-devel
%endif

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


%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_liri} ..
popd
make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}
rm -f %{buildroot}%{_libdir}/libLiri1{EdidSupport,KmsSupport,LibInput}.a
rm -rf %{buildroot}%{_includedir}/Liri{EglFSDeviceIntegration,EglFSKmsSupport,EdidSupport,KmsSupport,LibInput}
rm -f %{buildroot}%{_libdir}/libLiri1EglFS{DeviceIntegration,KmsSupport}.so


%post -p /sbin/ldconfig


%postun -p /sbin/ldconfig


%files
%license LICENSE.LGPLv3
%doc AUTHORS.md README.md
%{_qt5_plugindir}/platforms/liblirieglfs.so
%{_qt5_plugindir}/liri/egldeviceintegrations/
%{_libdir}/libLiri1EglFSDeviceIntegration.so.*
%{_libdir}/libLiri1EglFSKmsSupport.so.*
%{_libdir}/libLiri1PlatformHeaders.so.*

%files devel
%{_includedir}/LiriPlatformHeaders/
%{_libdir}/cmake/Liri1PlatformHeaders/
%{_libdir}/libLiri1PlatformHeaders.so
%{_libdir}/pkgconfig/Liri1PlatformHeaders.pc
