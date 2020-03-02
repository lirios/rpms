%define snapdate @DATE@
%define snaphash @HASH@

%define modulename wayland

Name:           liri-%{modulename}
Summary:        Wayland client and server libraries for Qt applications
Version:        0.10.0
Release:        0.1%{?snaphash:.%{snapdate}git%(echo %{snaphash} | cut -c -13)}%{?dist}
License:        LGPLv3 or GPLv2 or GPLv3
Url:            https://liri.io
Source0:        https://github.com/lirios/%{modulename}/%{?snaphash:archive}%{!?snaphash:releases/download}/%{?snaphash}%{!?snaphash:v%{version}}/%{name}-%{?snaphash}%{!?snaphash:%{version}}.tar.gz

BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5WaylandClient)
BuildRequires:  pkgconfig(Qt5WaylandCompositor)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  liri-rpm-macros

%description
Wayland client and server libraries for Qt applications.


%package devel
Summary:        Development files for %{name}
Group:          Development/System
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig(wayland-client)
Requires:       pkgconfig(wayland-server)
BuildRequires:  pkgconfig(Qt5WaylandClient)
BuildRequires:  pkgconfig(Qt5WaylandCompositor)

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


%post -p /sbin/ldconfig


%postun -p /sbin/ldconfig


%files
%license LICENSE.LGPLv3
%doc AUTHORS.md README.md
%{_libdir}/libLiri1WaylandClient.so.*
%{_libdir}/libLiri1WaylandServer.so.*
%{_qt5_qmldir}/Liri/WaylandClient/
%{_qt5_qmldir}/Liri/WaylandServer/

%files devel
%{_includedir}/LiriWaylandClient/
%{_includedir}/LiriWaylandServer/
%{_libdir}/libLiri1WaylandClient.so
%{_libdir}/libLiri1WaylandServer.so
%{_libdir}/pkgconfig/Liri1WaylandClient.pc
%{_libdir}/pkgconfig/Liri1WaylandServer.pc
%{_libdir}/cmake/Liri1WaylandClient/
%{_libdir}/cmake/Liri1WaylandServer/
