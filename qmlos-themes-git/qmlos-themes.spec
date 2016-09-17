%define snapdate 20160917
%define snaphash 4662c106e7e2b69dad26533b74e0ace90f8f1143

%define modulename themes

%global _grubthemedir /boot/grub2/themes

Summary:        qmlOS themes
Name:           qmlos-%{modulename}
Version:        0.9.0
Release:        1%{?snaphash:.%{snapdate}git%(echo %{snaphash} | cut -c -13)}%{?dist}
License:        GPLv3+
URL:            https://github.com/qmlos
Source:         https://github.com/qmlos/%{modulename}/%{?snaphash:archive}%{!?snaphash:releases/download}/%{?snaphash}%{!?snaphash:v%{version}}/%{name}-%{?snaphash}%{!?snaphash:%{version}}.tar.gz
BuildRequires:  cmake
BuildArch:      noarch

%description
This package contains qmlOS themes for GRUB and Plymouth.


%package -n grub2-themes-qmlos
Summary:        qmlOS theme for GRUB
%ifnarch aarch64
Requires:       grub2
%else
Requires:       grub2-efi
%endif

%description -n grub2-themes-qmlos
This package contains the "qmlOS" theme for GRUB.


%package -n plymouth-theme-qmlos
Summary:        qmlOS theme for Plymouth
Requires:       plymouth-plugin-two-step

%description -n plymouth-theme-qmlos
This package contains the "Hawaii" theme for Plymouth.


%package -n sddm-theme-qmlos
Summary:        qmlOS theme for SDDM
Requires:       sddm

%description -n sddm-theme-qmlos
This package contains the "qmlOS" theme for SDDM.


%prep
%setup -q -n %{?snaphash:%{name}-%{snaphash}}%{!?snaphash:%{name}-%{version}}


%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install DESTDIR=%{buildroot} -C %{_target_platform}


%post -n plymouth-theme-qmlos
export LIB=%{_lib}
if [ $1 -eq 1 ]; then
    %{_sbindir}/plymouth-set-default-theme hawaii
    %{_libexecdir}/plymouth/plymouth-generate-initrd
fi


%postun -n plymouth-theme-qmlos
export LIB=%{_lib}
if [ $1 -eq 0 ]; then
    if [ "$(%{_sbindir}/plymouth-set-default-theme)" == "hawaii" ]; then
        %{_sbindir}/plymouth-set-default-theme --reset
        %{_libexecdir}/plymouth/plymouth-generate-initrd
    fi
fi


%files -n grub2-themes-qmlos
%defattr(-,root,root,-)
%doc AUTHORS.md README.md
%dir %{_grubthemedir}/qmlos


%files -n plymouth-theme-qmlos
%defattr(-,root,root,-)
%doc AUTHORS.md README.md
%dir %{_datadir}/plymouth/themes/hawaii
%{_datadir}/plymouth/themes/hawaii/*.png
%{_datadir}/plymouth/themes/hawaii/hawaii.plymouth


%files -n sddm-theme-qmlos
%defattr(-,root,root,-)
%doc AUTHORS.md README.md
%dir %{_datadir}/sddm/themes/qmlos


%changelog
* Sat Sep 17 2016 Pier Luigi Fiorini <pierluigi.fiorini@gmail.com> - 0.9.0-1
- Initial packaging.
