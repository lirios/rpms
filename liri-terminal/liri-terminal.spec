%global snapdate @DATE@
%global snaphash @HASH@

%define modulename terminal

Name:           liri-%{modulename}
Summary:        Terminal emulator for the Liri desktop environment
Version:        @VERSION@
Release:        0.1%{?snaphash:.%{snapdate}git%(echo %{snaphash} | cut -c -13)}%{?dist}
License:        GPLv3+
URL:            https://liri.io
Source0:        https://github.com/lirios/%{modulename}/%{?snaphash:archive}%{!?snaphash:releases/download}/%{?snaphash}%{!?snaphash:v%{version}}/%{name}-%{?snaphash}%{!?snaphash:%{version}}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5QuickControls2)
BuildRequires:  liri-rpm-macros
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

Requires:       fluid
Requires:       qt5-qtgsettings
Requires:       dconf


%description
This package contains a terminal emulator for the Liri desktop environment.


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
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.appdata.xml


%posttrans
glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :


%postun
if [ $1 -eq 0 ]; then
  glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
fi


%files
%license LICENSE.GPLv3
%doc AUTHORS.md README.md
%{_bindir}/liri-terminal
%{_datadir}/metainfo/*.appdata.xml
%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/io.liri.Terminal.gschema.xml
%{_datadir}/liri-terminal/
%{_qt5_qmldir}/Liri/Terminal/
