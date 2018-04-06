%global snapdate @DATE@
%global snaphash @HASH@

Name:           fluid
Summary:        Library for fluid and dynamic applications development with QtQuick
Version:        0.9.0
Release:        0.1%{?snaphash:.%{snapdate}git%(echo %{snaphash} | cut -c -13)}%{?dist}
License:        MPLv2
URL:            http://liri.io
Source0:        https://github.com/lirios/%{name}/%{?snaphash:archive}%{!?snaphash:releases/download}/%{?snaphash}%{!?snaphash:v%{version}}/%{name}-%{?snaphash}%{!?snaphash:%{version}}.tar.gz

Requires:       qt5-qtgraphicaleffects
Requires:       qt5-qtquickcontrols2

BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5QuickControls2)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  git

%description
Library for fluid and dynamic applications development with QtQuick.


%prep
%setup -q -n %{?snaphash:%{name}-%{snaphash}}%{!?snaphash:%{name}-%{version}}


%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       extra-cmake-modules
Requires:       pkgconfig(Qt5QuickControls2)

%description devel
%{summary}.


%build
./scripts/fetch_icons.sh

mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}


%files
%license LICENSE.MPL2
%doc AUTHORS.md README.md
%{_bindir}/fluid-demo
%{_kf5_qmldir}/Fluid/
%{_libdir}/libFluid*.so.*


%files devel
%license LICENSE.MPL2
%doc AUTHORS.md README.md
%{_includedir}/Fluid/
%{_libdir}/cmake/Fluid/
%{_libdir}/libFluid*.so


%changelog
* Sat Sep 17 2016 Pier Luigi Fiorini <pierluigi.fiorini@gmail.com> - 0.9.0-1
- Initial packaging.
