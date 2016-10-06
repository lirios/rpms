%define snapdate 20160929
%define snaphash 94bd34c25c0c9f00b4d47a05f8726f6e777e02e5

%define modulename themes

%global _grubthemedir /boot/grub2/themes

Summary:        Liri OS themes
Name:           lirios-%{modulename}
Version:        0.9.0
Release:        0.1%{?snaphash:.%{snapdate}git%(echo %{snaphash} | cut -c -13)}%{?dist}
License:        GPLv3+
URL:            http://liri.io
Source:         https://github.com/lirios/%{modulename}/%{?snaphash:archive}%{!?snaphash:releases/download}/%{?snaphash}%{!?snaphash:v%{version}}/%{name}-%{?snaphash}%{!?snaphash:%{version}}.tar.gz
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
%setup -q -n %{?snaphash:%{modulename}-%{snaphash}}%{!?snaphash:%{name}-%{version}}


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
* Sat Sep 17 2016 Pier Luigi Fiorini <pierluigi.fiorini@gmail.com> - 0.9.0-1
- Initial packaging.
