%global snapdate @DATE@
%global snaphash @HASH@

%define modulename files

Name:           liri-%{modulename}
Summary:        File manager for Liri
Version:        0.9.0
Release:        0.1%{?snaphash:.%{snapdate}git%(echo %{snaphash} | cut -c -13)}%{?dist}
License:        GPLv3+
URL:            http://liri.io
Source0:        https://github.com/lirios/%{modulename}/%{?snaphash:archive}%{!?snaphash:releases/download}/%{?snaphash}%{!?snaphash:v%{version}}/%{name}-%{?snaphash}%{!?snaphash:%{version}}.tar.gz

BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5QuickControls2)
BuildRequires:  cmake(Fluid)
BuildRequires:  qt5-qttools-devel
BuildRequires:  taglib-devel

BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  desktop-file-utils

Requires:       fluid

%description
Files is a file manager for Liri.


%prep
%setup -q -n %{?snaphash:%{modulename}-%{snaphash}}%{!?snaphash:%{name}-%{version}}


%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} -DDEVELOPMENT_BUILD:BOOL=ON ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files
%license LICENSE.GPLv3
%doc AUTHORS.md README.md
%{_bindir}/liri-files
%{_datadir}/applications/io.liri.Files.desktop
%{_kf5_qmldir}/Liri/Files/


%changelog
