%global snapdate @DATE@
%global snaphash @HASH@

%define modulename session

Name:           liri-%{modulename}
Summary:        Liri session
Version:        @VERSION@
Release:        0.1%{?snaphash:.%{snapdate}git%(echo %{snaphash} | cut -c -13)}%{?dist}
License:        GPLv3+
URL:            https://liri.io
Source0:        https://github.com/lirios/%{modulename}/%{?snaphash:archive}%{!?snaphash:releases/download}/%{?snaphash}%{!?snaphash:v%{version}}/%{name}-%{?snaphash}%{!?snaphash:%{version}}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  cmake(Qt5GSettings)
BuildRequires:  cmake(Liri1Xdg)
BuildRequires:  git
BuildRequires:  liri-rpm-macros

Requires:       dbus
Requires:       qt5-qttools
Requires:       qt5-qtgsettings
Requires:       libliri
Requires:       liri-shell
Requires:       dconf

%description
This is the Liri session manager.


%package devel
Summary:    Development files for %{name}
Requires:   %{name}%{?isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -n %{?snaphash:%{modulename}-%{snaphash}}%{!?snaphash:%{name}-%{version}}


%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_liri} \
    -DINSTALL_SYSTEMDUSERUNITDIR:PATH=%{_userunitdir} \
..
popd
make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}


%posttrans
glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :


%postun
if [ $1 -eq 0 ]; then
  glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
fi


%files
%license LICENSE.GPLv3
%license LICENSE.LGPLv3
%doc AUTHORS.md README.md
%{_bindir}/liri-session
%{_sysconfdir}/xdg/menus/*
%{_datadir}/wayland-sessions/*
%{_datadir}/desktop-directories/*
%{_datadir}/glib-2.0/schemas/*
%{_datadir}/dbus-1/services/io.liri.*.service
%{_libdir}/libLiri1Session.so.*
%{_liri_libexecdir}/liri-launcher


%files devel
%{_includedir}/LiriSession/
%{_libdir}/libLiri1Session.so
%{_libdir}/cmake/Liri1Session/
%{_libdir}/pkgconfig/Liri1Session.pc
