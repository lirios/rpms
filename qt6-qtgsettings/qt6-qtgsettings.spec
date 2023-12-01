%undefine __cmake_in_source_build

%global snapdate @DATE@
%global snaphash @HASH@

%global qt_module qtgsettings

Name:           qt6-%{qt_module}
Summary:        Qt6 - GSettings addon
Version:        @VERSION@
Release:        0.1%{?snaphash:.%{snapdate}git%(echo %{snaphash} | cut -c -13)}%{?dist}

License:        LGPLv3+
Url:            https://liri.io
Source0:        https://github.com/lirios/%{qt_module}/%{?snaphash:archive}%{!?snaphash:releases/download}/%{?snaphash}%{!?snaphash:v%{version}}/%{qt_module}-%{?snaphash}%{!?snaphash:%{version}}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6DBus)
BuildRequires:  pkgconfig(Qt6Qml)
BuildRequires:  pkgconfig(Qt6Quick)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  liri-cmake_shared

Requires:       dconf

%description
Qt-style API wrapper for GSettings.


%package devel
Summary:    Development files for %{name}
Requires:   %{name}%{?isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -n %{?snaphash:%{qt_module}-%{snaphash}}%{!?snaphash:%{qt_module}-%{version}}


%build
%cmake_kf6
%cmake_build


%install
%cmake_install


%post -p /sbin/ldconfig


%postun -p /sbin/ldconfig


%files
%license LICENSE.LGPLv3
%doc AUTHORS.md README.md
%{_libdir}/libQt6GSettings.so.*
%{_kf6_qmldir}/QtGSettings/


%files devel
%{_includedir}/Qt6GSettings/
%{_libdir}/libQt6GSettings.so
%{_libdir}/cmake/Qt6GSettings/
%{_libdir}/pkgconfig/Qt6GSettings.pc
