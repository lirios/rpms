%define modulename text

Name:           liri-%{modulename}
Summary:        Advanced text editor
Version:        0.5.0
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
Advanced text editor built in accordance with Material Design.


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
desktop-file-validate %{buildroot}%{_datadir}/applications/io.liri.Text.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/io.liri.Text.appdata.xml


%files
%license LICENSE.GPLv3
%doc AUTHORS.md README.md
%{_bindir}/liri-text
%{_datadir}/liri-text/
%{_datadir}/applications/io.liri.Text.desktop
%{_datadir}/metainfo/io.liri.Text.appdata.xml
%{_datadir}/icons/hicolor/*/*/io.liri.Text.png
