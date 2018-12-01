%global snapdate @DATE@
%global snaphash @HASH@

%global qt_module qtudev

Name:           qt5-%{qt_module}
Summary:        Qt-style API for udev
Version:        @VERSION@
Release:        0.1%{?snaphash:.%{snapdate}git%(echo %{snaphash} | cut -c -13)}%{?dist}

License:        LGPLv3+
Url:            https://liri.io
Source0:        https://github.com/lirios/%{qt_module}/%{?snaphash:archive}%{!?snaphash:releases/download}/%{?snaphash}%{!?snaphash:v%{version}}/%{qt_module}-%{?snaphash}%{!?snaphash:%{version}}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  liri-rpm-macros

%description
Qt-style API for udev.


%package devel
Summary:    Development files for %{name}
Requires:   %{name}%{?isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -n %{?snaphash:%{qt_module}-%{snaphash}}%{!?snaphash:%{qt_module}-%{version}}


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
%{_libdir}/libQt5Udev.so.*


%files devel
%{_includedir}/Qt5Udev/
%{_libdir}/libQt5Udev.so
%{_libdir}/cmake/Qt5Udev/
%{_libdir}/pkgconfig/Qt5Udev.pc
