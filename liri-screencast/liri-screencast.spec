%global snapdate @DATE@
%global snaphash @HASH@

%define modulename screencast

Name:           liri-%{modulename}
Summary:        Take videos of your screen
Version:        @VERSION@
Release:        0.1%{?snaphash:.%{snapdate}git%(echo %{snaphash} | cut -c -13)}%{?dist}
License:        GPLv3+
URL:            https://liri.io
Source0:        https://github.com/lirios/%{modulename}/%{?snaphash:archive}%{!?snaphash:releases/download}/%{?snaphash}%{!?snaphash:v%{version}}/%{name}-%{?snaphash}%{!?snaphash:%{version}}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  qt5-qttools
BuildRequires:  qt5-qttools-devel
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  liri-rpm-macros

%description
Take videos of your screen under a Liri Shell session.


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
%find_lang %{name} --all-name --with-qt


%files -f %{name}.lang
%license LICENSE.GPLv3
%doc AUTHORS.md README.md
%{_bindir}/liri-screencast
#%{_datadir}/liri-screencast/translations/liri-screencast_*.qm
