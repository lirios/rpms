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

BuildRequires:  gcc-c++
BuildRequires:  cmake >= 3.29.0-1
BuildRequires:  extra-cmake-modules >= 5.245.0-1

Requires:       extra-cmake-modules >= 5.245.0-1

BuildArch:      noarch

%description
Additional modules for the CMake build system.


%prep
%setup -q -n %{?snaphash:%{modulename}-%{snaphash}}%{!?snaphash:%{name}-%{version}}


%build
%cmake
%cmake_build


%install
%cmake_install


%files
%doc README.md
%{_datadir}/LiriCMakeShared/
