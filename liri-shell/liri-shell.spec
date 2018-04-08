%global snapdate @DATE@
%global snaphash @HASH@

%define modulename shell

Name:           liri-%{modulename}
Summary:        Liri shell for desktop, netbook and tablet
Version:        0.9.0
Release:        0.1%{?snaphash:.%{snapdate}git%(echo %{snaphash} | cut -c -13)}%{?dist}
License:        GPLv3+
URL:            http://liri.io
Source0:        https://github.com/lirios/%{modulename}/%{?snaphash:archive}%{!?snaphash:releases/download}/%{?snaphash}%{!?snaphash:v%{version}}/%{name}-%{?snaphash}%{!?snaphash:%{version}}.tar.gz

BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5WaylandClient)
BuildRequires:  pkgconfig(Qt5Xdg)
#BuildRequires:  pkgconfig(QtAccountsService)
BuildRequires:  qt5-qtaccountsservice-devel
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  cmake(GreenIslandClient)
BuildRequires:  cmake(GreenIslandServer)
BuildRequires:  cmake(Fluid)
BuildRequires:  cmake(Vibe)
BuildRequires:  pam-devel

BuildRequires:  git
BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules

Requires:       qt5-qtsvg
Requires:       qt5-qttools
Requires:       greenisland >= 0.8.0
Requires:       dbus
Requires:       dbus-x11
Requires:       pam
Requires:       udisks2
Requires:       upower
Requires:       dconf
Requires:       fluid
Requires:       vibe
Requires:       %{name}-components = %{version}
Requires:       liri-workspace >= %{version}

%description
This is the Liri desktop environment shell.


%package components
Summary:        Liri Shell QtQuick components

%description components
This package contains QtQuick components used by Liri Shell that are shared
with the SDDM theme.


%prep
%setup -q -n %{?snaphash:%{modulename}-%{snaphash}}%{!?snaphash:%{name}-%{version}}


%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} -DDEVELOPMENT_BUILD:BOOL=ON ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}


%files
%license LICENSE.GPLv3
%doc AUTHORS.md README.md
%{_bindir}/*
%{_datadir}/wayland-sessions/*
%{_datadir}/greenisland/shells/*
%{_userunitdir}/*
#%{_kf5_qtplugindir}/wayland-decoration-client/*
%{_libexecdir}/liri-shell-helper

%files components
%{_kf5_qmldir}/Liri/Launcher/
%{_kf5_qmldir}/Liri/LoginManager/
%{_kf5_qmldir}/Liri/Shell/
