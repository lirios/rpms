Summary:        Liri OS customization
Name:           lirios-customization
Version:        0.10.0
Release:        1.20190501%{?dist}
URL:            https://liri.io
License:        MIT

Source0:        10-disk-scheduler.rules
Source0:        org.projectatomic.rpmostree1.rules

BuildRequires:  pkgconfig(systemd)

BuildArch:      noarch


%description
Customization for Liri OS.


%prep
%setup -c -T


%build


%install
# Configure disk schedulers
install -Dm0644 %{_sourcedir}/10-disk-scheduler.rules %{buildroot}%{_udevrulesdir}/

# Polkit rules for rpm-ostree
install -Dm0644 %{_sourcedir}/org.projectatomic.rpmostree1.rules -t %{buildroot}%{_datadir}/polkit-1/rules.d/


%files
%defattr(-,root,root,-)
%{_udevrulesdir}/10-disk-scheduler.rules
%attr(0644,root,root) %{_datadir}/polkit-1/rules.d/org.projectatomic.rpmostree1.rules
