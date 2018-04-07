%global snapdate @DATE@
%global snaphash @HASH@

Name:           liri-qbs-shared
Summary:        Extra imports and modules for Qbs
Version:        1.3.0
Release:        0.1%{?snaphash:.%{snapdate}git%(echo %{snaphash} | cut -c -13)}%{?dist}
License:        BSD-3
Url:            https://liri.io
Source0:        https://github.com/lirios/qbs-shared/%{?snaphash:archive}%{!?snaphash:releases/download}/%{?snaphash}%{!?snaphash:v%{version}}/qbs-shared-%{?snaphash}%{!?snaphash:%{version}}.tar.gz
BuildArch:      noarch

Requires:       qbs

BuildRequires:  qbs

%description
Shared imports and modules for projects using the qbs build system.


%prep
%setup -q -n %{?snaphash:qbs-shared-%{snaphash}}%{!?snaphash:qbs-shared-%{version}}
qbs setup-toolchains --type gcc /usr/bin/g++ gcc


%build
qbs build --no-install -d build %{?_smp_mflags} profile:gcc project.prefix:%{_prefix}


%install
qbs install --no-build -d build -v --install-root %{buildroot} profile:gcc


%files
%license LICENSE.BSD
%doc README.md
%{_datadir}/qbs/imports/
%{_datadir}/qbs/modules/
