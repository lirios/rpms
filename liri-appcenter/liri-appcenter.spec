%undefine __cmake_in_source_build

%global snapdate @DATE@
%global snaphash @HASH@

%define modulename appcenter

Name:           liri-%{modulename}
Summary:        Software center for Liri
Version:        @VERSION@
Release:        0.1%{?snaphash:.%{snapdate}git%(echo %{snaphash} | cut -c -13)}%{?dist}
License:        GPLv3+
URL:            https://liri.io
Source0:        https://github.com/lirios/%{modulename}/%{?snaphash:archive}%{!?snaphash:releases/download}/%{?snaphash}%{!?snaphash:v%{version}}/%{name}-%{?snaphash}%{!?snaphash:%{version}}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5QuickControls2)
BuildRequires:  qt5-qttools-devel
BuildRequires:  libliri-devel
BuildRequires:  pkgconfig(Qt5AccountsService)
BuildRequires:  pkgconfig(flatpak)
BuildRequires:  cmake(AppStreamQt)
BuildRequires:  liri-rpm-macros
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

Requires:       fluid
Requires:       libliri
Requires:       qt5-qtaccountsservice
Requires:       qt5-qtgsettings
Requires:       dconf

%description
Software center for Liri.


%package devel
Summary:    Development files for %{name}
Requires:   %{name}%{?isa} = %{version}-%{release}

%description devel
Files for development of Liri AppCenter plugins.


%prep
%setup -q -n %{?snaphash:%{modulename}-%{snaphash}}%{!?snaphash:%{name}-%{version}}


%build
%cmake_liri
%cmake_build


%install
%cmake_install


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/io.liri.AppCenter{,.Flatpak}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/io.liri.AppCenter.appdata.xml


%post -p /sbin/ldconfig


%postun -p /sbin/ldconfig


%files
%doc AUTHORS.md README.md
%{_bindir}/liri-appcenter
%{_liri_libexecdir}/liri-appcenter-notifier
%{_sysconfdir}/xdg/autostart/io.liri.AppCenter.Notifier.desktop
%{_datadir}/applications/io.liri.AppCenter.desktop
%{_datadir}/applications/io.liri.AppCenter.Notifier.desktop
%{_datadir}/applications/io.liri.AppCenter.Flatpak.desktop
%{_datadir}/metainfo/io.liri.AppCenter.appdata.xml
%{_datadir}/liri-appcenter/
%{_libdir}/libLiri1AppCenter.so.*
%{_qt5_qmldir}/Liri/AppCenter/
%{_qt5_plugindir}/liri/appcenter/


%files devel
%{_includedir}/LiriAppCenter/
%{_libdir}/libLiri1AppCenter.so
%{_libdir}/cmake/Liri1AppCenter/
