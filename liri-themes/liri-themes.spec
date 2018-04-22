%global snapdate @DATE@
%global snaphash @HASH@

%define modulename themes

%global _grubthemedir /boot/grub/themes

Summary:        Liri OS themes
Name:           liri-%{modulename}
Version:        @VERSION@
Release:        0.1%{?snaphash:.%{snapdate}git%(echo %{snaphash} | cut -c -13)}%{?dist}
License:        GPLv3+
URL:            http://liri.io
Source:         https://github.com/lirios/%{modulename}/%{?snaphash:archive}%{!?snaphash:releases/download}/%{?snaphash}%{!?snaphash:v%{version}}/%{name}-%{?snaphash}%{!?snaphash:%{version}}.tar.gz
BuildRequires:  liri-qbs-shared
BuildArch:      noarch

%description
This package contains Liri OS themes for GRUB and Plymouth.


%package -n liri-color-schemes
Summary:        Color schemes for Qt applications

%description -n liri-color-schemes
This package contains color schemes for Qt applications.


%package -n grub2-lirios-theme
Summary:        Liri OS theme for GRUB
%ifnarch aarch64
Requires:       grub2
%else
Requires:       grub2-efi
%endif

%description -n grub2-lirios-theme
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
qbs setup-toolchains --type gcc /usr/bin/g++ gcc


%build
qbs build --no-install -d build %{?_smp_mflags} profile:gcc \
    modules.lirideployment.prefix:%{_prefix} \
    modules.lirideployment.etcDir:%{_sysconfdir} \
    modules.lirideployment.binDir:%{_bindir} \
    modules.lirideployment.sbinDir:%{_sbindir} \
    modules.lirideployment.libDir:%{_libdir} \
    modules.lirideployment.libexecDir:%{_libexecdir} \
    modules.lirideployment.includeDir:%{_includedir} \
    modules.lirideployment.dataDir:%{_datadir} \
    modules.lirideployment.docDir:%{_docdir} \
    modules.lirideployment.manDir:%{_mandir} \
    modules.lirideployment.infoDir:%{_infodir} \
    modules.lirideployment.qmlDir:%{_qt5_qmldir} \
    modules.lirideployment.pluginsDir:%{_qt5_plugindir}


%install
qbs install --no-build -d build -v --install-root %{buildroot} profile:qt5


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


%files -n liri-color-schemes
%defattr(-,root,root,-)
%{_datadir}/color-schemes/*.colors


%files -n grub2-lirios-theme
%defattr(-,root,root,-)
%doc AUTHORS.md README.md
%{_grubthemedir}/lirios/


%files -n plymouth-theme-lirios
%defattr(-,root,root,-)
%doc AUTHORS.md README.md
%{_datadir}/plymouth/themes/lirios/


%files -n sddm-theme-lirios
%defattr(-,root,root,-)
%doc AUTHORS.md README.md
%{_datadir}/sddm/themes/lirios/
