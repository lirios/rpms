%undefine __cmake_in_source_build

%global snapdate @DATE@
%global snaphash @HASH@

%define modulename cmake-shared

Name:           liri-%{modulename}
Summary:        Additional modules for the CMake build system
Version:        @VERSION@
Release:        0.1%{?snaphash:.%{snapdate}git%(echo %{snaphash} | cut -c -13)}%{?dist}
License:        BSD-3
Url:            https://liri.io
Source0:        https://github.com/lirios/%{modulename}/%{?snaphash:archive}%{!?snaphash:releases/download}/%{?snaphash}%{!?snaphash:v%{version}}/%{name}-%{?snaphash}%{!?snaphash:%{version}}.tar.gz
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
%setup -q -n %{?snaphash:%{modulename}-%{snaphash}}%{!?snaphash:%{name}-%{version}}


%build
%cmake
%cmake_build


%install
%cmake_install
install -Dpm644 %{_sourcedir}/macros.liri %{buildroot}%{_rpmconfigdir}/macros.d/macros.liri


%files
%doc README.md
%{_datadir}/LiriCMakeShared/

%files -n liri-rpm-macros
%{_rpmconfigdir}/macros.d/macros.liri
