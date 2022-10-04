%undefine __cmake_in_source_build

%define snapdate @DATE@
%define snaphash @HASH@

Name:           aurora-scanner
Summary:        Converts Wayland protocol definition to C++ code
Version:        @VERSION@
Release:        0.1%{?snaphash:.%{snapdate}git%(echo %{snaphash} | cut -c -13)}%{?dist}
License:        GPLv3
Url:            https://liri.io
Source0:        https://github.com/lirios/aurora-scanner/%{?snaphash:archive}%{!?snaphash:releases/download}/%{?snaphash}%{!?snaphash:v%{version}}/%{name}-%{?snaphash}%{!?snaphash:%{version}}.tar.gz

BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  liri-rpm-macros

%description
Converts Wayland protocol definition to C++ code.


%prep
%setup -q -n %{?snaphash:%{name}-%{snaphash}}%{!?snaphash:%{name}-%{version}}


%build
%cmake_liri
%cmake_build


%install
%cmake_install


%post -p /sbin/ldconfig


%postun -p /sbin/ldconfig


%files
%doc README.md
%{_bindir}/aurora-wayland-scanner
