Summary:        Plymouth "Hawaii" theme
Name:           plymouth-theme-hawaii
Version:        0.2.1
Release:        2%{?dist}
License:        GPLv2+
Source:         https://github.com/hawaii-desktop/hawaii-plymouth-theme/archive/v%{version}.tar.gz
Requires:       plymouth-plugin-two-step
BuildRequires:  cmake
BuildArch:      noarch

%description
This package contains the "Hawaii" theme for Plymouth.


%prep
%setup -n hawaii-plymouth-theme-%{version}

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install DESTDIR=%{buildroot} -C %{_target_platform}


%files
%defattr(-,root,root,-)
%doc AUTHORS README.md
%dir %{_datadir}/plymouth/themes/hawaii
%{_datadir}/plymouth/themes/hawaii/*.png
%{_datadir}/plymouth/themes/hawaii/hawaii.plymouth

%changelog
* Fri Jun 19 2015 Pier Luigi Fiorini <pierluigi.fiorini@gmail.com> - 0.2.1-2
- Requires plymouth-plugin-two-step.

* Sat Jun 13 2015 Pier Luigi Fiorini <pierluigi.fiorini@gmail.com> - 0.2.1-1
- Initial packaging.

* Sat Jun 13 2015 Pier Luigi Fiorini <pierluigi.fiorini@gmail.com> - 0.1.0-1
- Initial packaging.
