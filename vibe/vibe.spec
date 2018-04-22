%global snapdate @DATE@
%global snaphash @HASH@

Name:           vibe
Summary:        A collection of core classes used throughout Liri
Version:        @VERSION@
Release:        0.1%{?snaphash:.%{snapdate}git%(echo %{snaphash} | cut -c -13)}%{?dist}
License:        LGPLv3
URL:            http://liri.io
Source0:        https://github.com/lirios/%{name}/%{?snaphash:archive}%{!?snaphash:releases/download}/%{?snaphash}%{!?snaphash:v%{version}}/%{name}-%{?snaphash}%{!?snaphash:%{version}}.tar.gz

BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(gio-2.0) >= 2.31.0
BuildRequires:  pkgconfig(NetworkManager)
BuildRequires:  pkgconfig(ModemManager)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Fluid)
BuildRequires:  cmake(KF5Wallet)
BuildRequires:  cmake(KF5Solid)
BuildRequires:  cmake(KF5NetworkManagerQt)
BuildRequires:  cmake(KF5ModemManagerQt)
BuildRequires:  cmake(PolkitQt5-1)
BuildRequires:  libqtxdg-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules

%description
A collection of core classes used throughout Liri.


%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       extra-cmake-modules
Requires:       pkgconfig(gio-2.0) >= 2.31.0
Requires:       cmake(Qt5LinguistTools)

%description devel
%{summary}.


%prep
%setup -q -n %{?snaphash:%{name}-%{snaphash}}%{!?snaphash:%{name}-%{version}}


%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%files
%license LICENSE.LGPLv3
%doc AUTHORS.md README.md
%{_bindir}/notify
%{_kf5_qmldir}/*
%{_libdir}/libVibe*.so.*


%files devel
%{_includedir}/Vibe/
%{_libdir}/cmake/Vibe/
%{_libdir}/libVibe*.so
