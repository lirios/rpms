%undefine __cmake_in_source_build

%global snapdate @DATE@
%global snaphash @HASH@

%define modulename shell

Name:           liri-%{modulename}
Summary:        Liri shell for desktop and mobile
Version:        @VERSION@
Release:        0.1%{?snaphash:.%{snapdate}git%(echo %{snaphash} | cut -c -13)}%{?dist}
License:        GPLv3+
URL:            https://liri.io
Source0:        https://github.com/lirios/%{modulename}/%{?snaphash:archive}%{!?snaphash:releases/download}/%{?snaphash}%{!?snaphash:v%{version}}/%{name}-%{?snaphash}%{!?snaphash:%{version}}.tar.gz

BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5QuickControls2)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5WaylandClient)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(polkit-qt5-1)
BuildRequires:  cmake(Qt5AccountsService)
BuildRequires:  cmake(Qt5GSettings)
BuildRequires:  cmake(Liri1Xdg)
BuildRequires:  cmake(Liri1AuroraCompositor)
BuildRequires:  cmake(Liri1AuroraClient)
BuildRequires:  cmake(KF5Solid)
BuildRequires:  pam-devel
BuildRequires:  git
BuildRequires:  liri-rpm-macros
BuildRequires:  qt5-qtbase-private-devel
BuildRequires:  aurora-scanner

Requires:       qt5-qtsvg
Requires:       qt5-qttools
Requires:       qt5-qtgsettings
Requires:       liri-qtintegration
Requires:       libliri
Requires:       fluid
Requires:       pam
Requires:       udisks2
Requires:       upower
Requires:       dconf
Requires:       accountsservice
Requires:       %{name}-components = %{version}

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
%cmake_liri \
    -DINSTALL_SYSTEMDUSERUNITDIR:PATH=%{_userunitdir} \
    -DLIRI_SHELL_DEVELOPMENT_BUILD:BOOL=ON
%cmake_build

# Set SDDM theme
mkdir -p %{buildroot}/usr/lib/sddm/sddm.conf.d
cat > %{buildroot}/usr/lib/sddm/sddm.conf.d/00-liri.conf <<EOF
[Theme]
Current=liri
EOF


%install
%cmake_install
rm -f %{buildroot}%{_libdir}/*.a


%posttrans
glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :


%postun
if [ $1 -eq 0 ]; then
  glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
fi


%files
%license LICENSE.GPLv3
%doc AUTHORS.md README.md
%{_datadir}/liri-shell/
%{_datadir}/glib-2.0/schemas/*
%{_userunitdir}/liri-*
%{_liri_libexecdir}/liri-shell
%{_liri_libexecdir}/liri-shell-helper
%{_qt5_qmldir}/Liri/Launcher/
%{_qt5_qmldir}/Liri/LoginManager/
%{_qt5_qmldir}/Liri/Mpris/
%{_qt5_qmldir}/Liri/PolicyKit/
%{_qt5_qmldir}/Liri/Shell/
%{_qt5_qmldir}/Liri/Storage/
%{_qt5_qmldir}/Liri/private/shell/
%{_prefix}/lib/sddm/sddm.conf.d/00-liri.conf
%{_datadir}/sddm/themes/liri/
