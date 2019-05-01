Summary:        Liri OS customization
Name:           lirios-customization
Version:        0.10.0
Release:        1.20190501%{?dist}
URL:            http://liri.io
License:        MIT
BuildArch:      noarch
BuildRequires:  pkgconfig(systemd)


%description
Customization for Liri OS.


%prep


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


%files
%defattr(-,root,root,-)
%{_udevrulesdir}/10-disk-scheduler.rules


%changelog
* Wed May 01 2019 Pier Luigi Fiorini <pierluigi.fiorini@gmail.com> - 0.10.0-1.20190501
- Update version.

* Sun Oct 09 2016 Pier Luigi Fiorini <pierluigi.fiorini@gmail.com> - 0.9.0-1.20161009
- Initial packaging.
