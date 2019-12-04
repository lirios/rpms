Summary:        Liri OS customization
Name:           lirios-customization
Version:        0.10.0
Release:        1.20190501%{?dist}
URL:            http://liri.io
License:        MIT

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
install -d %{buildroot}%{_udevrulesdir}
cat > %{buildroot}%{_udevrulesdir}/10-disk-scheduler.rules <<EOF
# Set deadline scheduler for non-rotating disks
ACTION=="add|change", KERNEL=="sd[a-z]", ATTR{queue/rotational}=="0", ATTR{queue/scheduler}="deadline"

# Set cfq scheduler for rotating disks
ACTION=="add|change", KERNEL=="sd[a-z]", ATTR{queue/rotational}=="1", ATTR{queue/scheduler}="cfq"
EOF

# Polkit rules for rpm-ostree
install -Dm0644 %{_sourcedir}/org.projectatomic.rpmostree1.rules -t %{buildroot}%{_datadir}/polkit-1/rules.d/


%files
%defattr(-,root,root,-)
%{_udevrulesdir}/10-disk-scheduler.rules
%attr(0644,root,root) %{_datadir}/polkit-1/rules.d/org.projectatomic.rpmostree1.rules


%changelog
* Wed May 01 2019 Pier Luigi Fiorini <pierluigi.fiorini@gmail.com> - 0.10.0-1.20190501
- Update version.

* Sun Oct 09 2016 Pier Luigi Fiorini <pierluigi.fiorini@gmail.com> - 0.9.0-1.20161009
- Initial packaging.
