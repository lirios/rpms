%global qt_module qtgsettings

Name:           qt5-%{qt_module}
Summary:        Qt5 - GSettings addon
Version:        1.3.0
Release:        1%{?dist}

License:        LGPLv3+
Url:            https://liri.io
Source0:        https://github.com/lirios/%{qt_module}/releases/download/v%{version}/%{qt_module}-%{version}.tar.xz

BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  liri-rpm-macros

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
%setup -q -n %{qt_module}-%{version}


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
%{_libdir}/libQt5GSettings.so.*
%{_qt5_qmldir}/QtGSettings/


%files devel
%{_includedir}/Qt5GSettings/
%{_libdir}/libQt5GSettings.so
%{_libdir}/cmake/Qt5GSettings/
%{_libdir}/pkgconfig/Qt5GSettings.pc
