%global _grubthemedir /boot/grub2/themes

%define modulename themes

Summary:        Liri OS themes
Name:           lirios-%{modulename}
Version:        0.8.90
Release:        1%{?dist}
License:        GPLv3+
URL:            https://github.com/lirios
Source:         https://github.com/lirios/%{modulename}/archive/v%{version}.tar.gz
BuildRequires:  cmake
BuildArch:      noarch

%description
This package contains Liri OS themes for GRUB and Plymouth.


%package -n grub2-themes-lirios
Summary:        Liri OS theme for GRUB
%ifnarch aarch64
Requires:       grub2
%else
Requires:       grub2-efi
%endif

%description -n grub2-themes-lirios
This package contains the "Liri OS" theme for GRUB.


%package -n plymouth-theme-lirios
Summary:        Liri OS theme for Plymouth
Requires:       plymouth-plugin-two-step

%description -n plymouth-theme-lirios
This package contains the "Liri OS" theme for Plymouth.


%package -n sddm-theme-lirios
Summary:        Liri OS theme for SDDM
Requires:       sddm

%description -n sddm-theme-lirios
This package contains the "Liri OS" theme for SDDM.


%prep
%setup -n %{name}-%{version}


%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install DESTDIR=%{buildroot} -C %{_target_platform}


%post -n plymouth-theme-lirios
export LIB=%{_lib}
if [ $1 -eq 1 ]; then
    %{_sbindir}/plymouth-set-default-theme lirios
    %{_libexecdir}/plymouth/plymouth-generate-initrd
fi


%postun -n plymouth-theme-lirios
export LIB=%{_lib}
if [ $1 -eq 0 ]; then
    if [ "$(%{_sbindir}/plymouth-set-default-theme)" == "lirios" ]; then
        %{_sbindir}/plymouth-set-default-theme --reset
        %{_libexecdir}/plymouth/plymouth-generate-initrd
    fi
fi


%files -n grub2-themes-lirios
%defattr(-,root,root,-)
%doc AUTHORS.md README.md
%dir %{_grubthemedir}/lirios


%files -n plymouth-theme-lirios
%defattr(-,root,root,-)
%doc AUTHORS.md README.md
%dir %{_datadir}/plymouth/themes/lirios
%{_datadir}/plymouth/themes/lirios/*.png
%{_datadir}/plymouth/themes/lirios/lirios.plymouth


%files -n sddm-theme-lirios
%defattr(-,root,root,-)
%doc AUTHORS.md README.md
%dir %{_datadir}/sddm/themes/lirios


%changelog
* Sat Sep 17 2016 Pier Luigi Fiorini <pierluigi.fiorini@gmail.com> - 0.8.90-1
- Initial packaging.
