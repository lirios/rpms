%undefine __cmake_in_source_build

%global snapdate @DATE@
%global snaphash @HASH@

%define modulename wallpapers

Summary:        Backgrounds for the Liri desktop
Name:           liri-%{modulename}
Version:        @VERSION@
Release:        0.1%{?snaphash:.%{snapdate}git%(echo %{snaphash} | cut -c -13)}%{?dist}
License:        CC-BY-SA
URL:            https://liri.io
Source:         https://github.com/lirios/%{modulename}/%{?snaphash:archive}%{!?snaphash:releases/download}/%{?snaphash}%{!?snaphash:v%{version}}/%{name}-%{?snaphash}%{!?snaphash:%{version}}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  liri-rpm-macros

BuildArch:      noarch

%description
This package contains backgrounds for the Liri desktop.


%prep
%setup -q -n %{?snaphash:%{modulename}-%{snaphash}}%{!?snaphash:%{name}-%{version}}


%build
%cmake_liri
%cmake_build


%install
%cmake_install


%files
%defattr(-,root,root,-)
%{_datadir}/backgrounds/liri/
