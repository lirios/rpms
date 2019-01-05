%global snapdate @DATE@
%global snaphash @HASH@

%define modulename files

Name:           liri-%{modulename}
Summary:        File manager for Liri
Version:        @VERSION@
Release:        0.1%{?snaphash:.%{snapdate}git%(echo %{snaphash} | cut -c -13)}%{?dist}
License:        GPLv3+
URL:            https://liri.io
Source0:        https://github.com/lirios/%{modulename}/%{?snaphash:archive}%{!?snaphash:releases/download}/%{?snaphash}%{!?snaphash:v%{version}}/%{name}-%{?snaphash}%{!?snaphash:%{version}}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5QuickControls2)
BuildRequires:  qt5-qttools-devel
BuildRequires:  taglib-devel
BuildRequires:  liri-rpm-macros
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

Requires:       fluid
Requires:       qt5-qtgsettings
Requires:       dconf

%description
Files is a file manager for Liri.


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


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/io.liri.Files.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/io.liri.Files.appdata.xml


%files -f %{name}.lang
%license LICENSE.GPLv3
%doc AUTHORS.md README.md
%{_bindir}/liri-files
%{_datadir}/liri-files/
%{_datadir}/applications/io.liri.Files.desktop
%{_datadir}/metainfo/io.liri.Files.appdata.xml
%{_qt5_qmldir}/Liri/Files/
