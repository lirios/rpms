%define modulename cmake-shared

Name:           liri-%{modulename}
Summary:        Additional modules for the CMake build system
Version:        1.0.0
Release:        1%{dist}
License:        BSD-3
Url:            https://liri.io
Source0:        https://github.com/lirios/%{modulename}/releases/download/v%{version}/%{name}-%{version}.tar.xz
Source1:        macros.liri

BuildRequires:  gcc-c++
BuildRequires:  cmake

Requires:       extra-cmake-modules

BuildArch:      noarch

%description
Additional modules for the CMake build system.


%package -n liri-rpm-macros
Summary: RPM macros for Liri
Requires: liri-cmake-shared
Requires: qt5-rpm-macros
BuildArch: noarch

%description -n liri-rpm-macros
RPM macros for building Liri packages.


%prep
%setup -q -n %{name}-%{version}


%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake} ..
popd
make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

install -Dpm644 %{_sourcedir}/macros.liri %{buildroot}%{_rpmconfigdir}/macros.d/macros.liri


%files
%license LICENSE.BSD
%doc README.md
%{_datadir}/LiriCMakeShared/

%files -n liri-rpm-macros
%{_rpmconfigdir}/macros.d/macros.liri
