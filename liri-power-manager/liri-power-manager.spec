%global snapdate @DATE@
%global snaphash @HASH@

%define modulename power-manager

Name:           liri-%{modulename}
Summary:        Manages the power consumption settings of Liri Shell
Version:        @VERSION@
Release:        0.1%{?snaphash:.%{snapdate}git%(echo %{snaphash} | cut -c -13)}%{?dist}
License:        GPLv3+
URL:            https://liri.io
Source0:        https://github.com/lirios/%{modulename}/%{?snaphash:archive}%{!?snaphash:releases/download}/%{?snaphash}%{!?snaphash:v%{version}}/%{name}-%{?snaphash}%{!?snaphash:%{version}}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(gio-2.0) >= 2.31.0
BuildRequires:  pkgconfig(Qt5GSettings)
BuildRequires:  pkgconfig(Liri1Core)
BuildRequires:  pkgconfig(Liri1LocalDevice)
BuildRequires:  pkgconfig(Liri1Logind)
BuildRequires:  pkgconfig(Liri1Notifications)
BuildRequires:  pkgconfig(Liri1Session)
BuildRequires:  cmake(KF5Solid)
BuildRequires:  qt5-qttools
BuildRequires:  qt5-qttools-devel
BuildRequires:  liri-rpm-macros

Requires:       fluid
Requires:       qt5-qtgsettings

%description
This package contains a daemon for power management and a
settings module to configure power consumption settings.


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


%posttrans
glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :


%postun
if [ $1 -eq 0 ]; then
  glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
fi


%files
%license LICENSE.GPLv3
%doc AUTHORS.md README.md
%{_datadir}/glib-2.0/schemas/*
%{_datadir}/liri-power-manager/translations/*.qm
%{_datadir}/liri-settings/modules/power/
%{_datadir}/liri-settings/translations/modules/power_*.qm
%{_datadir}/liri-shell/indicators/power/
%{_qt5_qmldir}/Liri/Power/
%{_qt5_plugindir}/liri/sessionmodules/libpower.so
