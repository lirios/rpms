%define modulename calculator

Name:           liri-%{modulename}
Summary:        Material Design calculator
Version:        1.3.0
Release:        1%{?dist}
License:        GPLv3+
URL:            https://liri.io
Source0:        https://github.com/lirios/%{modulename}/releases/download/v%{version}/%{name}-%{version}.tar.xz

BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5QuickControls2)
BuildRequires:  qt5-qttools-devel
BuildRequires:  liri-rpm-macros
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

Requires:       fluid

%description
Material Design calculator.


%prep
%setup -q -n %{name}-%{version}


%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_liri} ..
popd
make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/io.liri.Calculator.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/io.liri.Calculator.appdata.xml


%files
%license LICENSE.GPLv3
%doc README.md
%{_bindir}/liri-calculator
%{_datadir}/liri-calculator/
%{_datadir}/applications/io.liri.Calculator.desktop
%{_datadir}/metainfo/io.liri.Calculator.appdata.xml
%{_datadir}/icons/hicolor/*/*/io.liri.Calculator.png
