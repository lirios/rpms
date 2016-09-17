Name:           fluid
Summary:        Library for fluid and dynamic applications development with QtQuick
Version:        0.8.90
Release:        1%{?dist}
License:        MPLv2
URL:            https://github.com/qmlos
Source0:        https://github.com/qmlos/%{name}/archive/v%{version}}.tar.gz

Requires:       qt5-graphicaleffects
Requires:       qt5-qtquickcontrols2

BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules

%description
Library for fluid and dynamic applications development with QtQuick.


%prep
%setup -q -n %{name}-%{version}


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
%{_kf5_qmldir}/Fluid/


%changelog
* Sat Sep 17 2016 Pier Luigi Fiorini <pierluigi.fiorini@gmail.com> - 0.8.90-1
- Initial packaging.
