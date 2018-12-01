%global snapdate @DATE@
%global snaphash @HASH@

%define modulename browser

Name:           liri-%{modulename}
Summary:        Material Design web browser
Version:        @VERSION@
Release:        0.1%{?snaphash:.%{snapdate}git%(echo %{snaphash} | cut -c -13)}%{?dist}
License:        GPLv3+
URL:            https://liri.io
Source0:        https://github.com/lirios/%{modulename}/%{?snaphash:archive}%{!?snaphash:releases/download}/%{?snaphash}%{!?snaphash:v%{version}}/%{name}-%{?snaphash}%{!?snaphash:%{version}}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5QuickControls2)
BuildRequires:  pkgconfig(Qt5WebEngine)
BuildRequires:  qt5-qttools-devel
BuildRequires:  liri-rpm-macros
BuildRequires:  desktop-file-utils

Requires:       fluid
Requires:       qt5-qtwebengine

%description
Modern web browser based on QtWebEngine (which is itself based on
the Chromium core, i.e., Blink) and the Qt framework.

Born to use the Material Design, fits very well with
the Liri desktop.


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
desktop-file-validate %{buildroot}%{_datadir}/applications/io.liri.Browser.desktop


%files
%license LICENSE.GPLv3
%doc AUTHORS.md README.md
%{_bindir}/liri-browser
%{_datadir}/applications/io.liri.Browser.desktop
%{_datadir}/icons/hicolor/*/*/io.liri.Browser.png
%{_datadir}/icons/hicolor/*/*/io.liri.Browser.svg
