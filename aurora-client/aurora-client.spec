%undefine __cmake_in_source_build

%define snapdate @DATE@
%define snaphash @HASH@

Name:           aurora-client
Summary:        Wayland client library for Qt applications
Version:        0.10.0
Release:        0.1%{?snaphash:.%{snapdate}git%(echo %{snaphash} | cut -c -13)}%{?dist}
License:        LGPLv3
Url:            https://liri.io
Source0:        https://github.com/lirios/%{name}/%{?snaphash:archive}%{!?snaphash:releases/download}/%{?snaphash}%{!?snaphash:v%{version}}/%{name}-%{?snaphash}%{!?snaphash:%{version}}.tar.gz

BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5WaylandClient)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  liri-rpm-macros

%description
Qt-style API to interact with Wayland protocols inside Qt-based graphical applications.


%package devel
Summary:        Development files for %{name}
Group:          Development/System
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig(wayland-client)
BuildRequires:  pkgconfig(Qt5WaylandClient)

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
%doc README.md
%{_libdir}/libLiri1AuroraClient.so.*
%{_qt5_qmldir}/Liri/WaylandClient/

%files devel
%{_includedir}/LiriWaylandClient/
%{_libdir}/libLiri1AuroraClient.so
%{_libdir}/pkgconfig/Liri1AuroraClient.pc
%{_libdir}/cmake/Liri1AuroraClient/
