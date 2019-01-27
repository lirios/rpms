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
BuildArch:      noarch

BuildRequires:  gcc-c++
BuildRequires:  liri-rpm-macros

Requires:       calamares

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


%files
%license LICENSE.GPLv3
%doc AUTHORS.md README.md
%{_bindir}/calamares.sh
%{_sysconfdir}/calamares/*.conf
%{_sysconfdir}/calamares/modules/*.conf
%{_datadir}/calamares/branding/liri/
%{_datadir}/liri-calamares-branding/
%{_libdir}/calamares/modules/*/
