# Version required for Session support.
%global xdg_desktop_portal_version 0.10

%global snapdate @DATE@
%global snaphash @HASH@

Name:           xdg-desktop-portal-liri
Summary:        Backend implementation for xdg-desktop-portal for Liri
Version:        @VERSION@
Release:        0.1%{?snaphash:.%{snapdate}git%(echo %{snaphash} | cut -c -13)}%{?dist}
License:        GPLv3+
URL:            https://liri.io
Source0:        https://github.com/lirios/%{name}/%{?snaphash:archive}%{!?snaphash:releases/download}/%{?snaphash}%{!?snaphash:v%{version}}/%{name}-%{?snaphash}%{!?snaphash:%{version}}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(xdg-desktop-portal) >= %{xdg_desktop_portal_version}
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5QuickControls2)
BuildRequires:  liri-rpm-macros
BuildRequires:  libliri-devel

Requires:       xdg-desktop-portal >= %{xdg_desktop_portal_version}
Requires:       fluid
Requires:       libliri

%description
A backend implementation for xdg-desktop-portal that is using Qt and various
pieces of Liri libraries and infrastructure.


%prep
%setup -q -n %{?snaphash:%{name}-%{snaphash}}%{!?snaphash:%{name}-%{version}}


%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_liri} ..
popd
make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}


%files
%license LICENSE.GPLv3
%doc AUTHORS.md README.md
%{_liri_libexecdir}/xdg-desktop-portal-liri
%{_datadir}/xdg-desktop-portal/portals/liri.portal
%{_datadir}/dbus-1/services/org.freedesktop.impl.portal.desktop.liri.service
