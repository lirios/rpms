Summary:        Liri OS customization
Name:           lirios-customization
Version:        0.9.0
Release:        1.20161009%{?dist}
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
