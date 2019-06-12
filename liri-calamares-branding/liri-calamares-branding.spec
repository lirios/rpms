%global snapdate @DATE@
%global snaphash @HASH@

%define modulename calamares-branding

Name:           liri-%{modulename}
Summary:        Liri OS branding and customizations for Calamares
Version:        @VERSION@
Release:        0.1%{?snaphash:.%{snapdate}git%(echo %{snaphash} | cut -c -13)}%{?dist}
License:        GPLv3+
URL:            https://liri.io
Source0:        https://github.com/lirios/%{modulename}/%{?snaphash:archive}%{!?snaphash:releases/download}/%{?snaphash}%{!?snaphash:v%{version}}/%{name}-%{?snaphash}%{!?snaphash:%{version}}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5QuickControls2)
BuildRequires:  liri-rpm-macros
BuildRequires:  desktop-file-utils

Requires:       calamares
Requires:       rpm-ostree
Requires:       fluid

%description
Liri OS branding and customizations for Calamares.


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


%check
desktop-file-validate %{buildroot}%{_sysconfdir}/xdg/autostart/io.liri.LiveWelcome.desktop


%files
%license LICENSE.GPLv3
%doc AUTHORS.md README.md
%{_bindir}/liri-live-welcome
%{_bindir}/calamares.sh
%{_bindir}/calamares-ostree-install
%{_sysconfdir}/xdg/autostart/io.liri.LiveWelcome.desktop
%{_sysconfdir}/calamares/*.conf
%{_sysconfdir}/calamares/modules/*.conf
%{_datadir}/calamares/branding/liri/
%{_datadir}/calamares/modules/*.conf
%{_datadir}/liri-calamares-branding/
%{_datadir}/liri-live-welcome/
%{_libdir}/calamares/modules/*/
