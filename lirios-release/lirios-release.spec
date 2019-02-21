%define dist_version 29
%define lirios_version 0.10.0

Name:           lirios-release
Summary:        Liri OS release files
Version:        %{dist_version}
Release:        3
License:        MIT
Source0:        LICENSE
Source1:        README.license
Source2:        plfiorini-lirios.repo
Source3:        85-display-manager.preset
Source4:        90-default.preset
Source5:        90-default-user.preset
Source6:        99-default-disable.preset

# for macros.systemd
BuildRequires:  systemd

Provides:       redhat-release
Provides:       system-release
Provides:       system-release(%{dist_version})
Provides:       system-release(releasever) = %{dist_version}

Requires:       filesystem
Requires:       fedora-repos(%{dist_version})

Conflicts:      redhat-release
Conflicts:      fedora-release
Conflicts:      generic-release

BuildArch:      noarch

%description
Liri OS release files such as yum configs and various /etc/ files that
define the release.


%prep
%setup -c -T
cp -a %{SOURCE0} %{SOURCE1} %{SOURCE3} %{SOURCE4} %{SOURCE5} %{SOURCE6} .


%build


%install
install -d %{buildroot}%{_sysconfdir}
echo "Liri OS release %{lirios_version}" > %{buildroot}%{_sysconfdir}/fedora-release
echo "cpe:/o:lirios:lirios:%{lirios_version}" > %{buildroot}%{_sysconfdir}/system-release-cpe
cp -p %{buildroot}%{_sysconfdir}/fedora-release %{buildroot}%{_sysconfdir}/issue
echo "Kernel \r on an \m (\l)" >> %{buildroot}%{_sysconfdir}/issue
cp -p %{buildroot}%{_sysconfdir}/issue %{buildroot}%{_sysconfdir}/issue.net
echo >> %{buildroot}%{_sysconfdir}/issue
ln -s fedora-release %{buildroot}%{_sysconfdir}/redhat-release
ln -s fedora-release %{buildroot}%{_sysconfdir}/system-release

install -d %{buildroot}/%{_prefix}/lib/os.release.d/
cat << EOF >>%{buildroot}%{_prefix}/lib/os.release.d/os-release-lirios
NAME="Liri OS"
VERSION=%{lirios_version}
ID=lirios
VERSION_ID=%{lirios_version}
PRETTY_NAME="Liri OS %{lirios_version}"
ANSI_COLOR="0;34"
CPE_NAME="cpe:/o:lirios:lirios:%{lirios_version}"
EOF
# Create the symlink for /usr/lib/os-release
ln -s ./os.release.d/os-release-lirios %{buildroot}%{_prefix}/lib/os-release
# Create the symlink for /etc/os-release
ln -s ..%{_prefix}/lib/os-release %{buildroot}%{_sysconfdir}/os-release

# Set up the dist tag macros
install -d -m 755 %{buildroot}%{_rpmconfigdir}/macros.d
cat >> %{buildroot}%{_rpmconfigdir}/macros.d/macros.dist << EOF
# dist macros.

%%fedora		%{dist_version}
%%dist		.fc%{dist_version}
%%fc%{dist_version}		1
EOF

# Install the .repo file
install -dm 755 %{buildroot}%{_sysconfdir}/yum.repos.d
install -pm 644 %{SOURCE2} \
    %{buildroot}%{_sysconfdir}/yum.repos.d

# Add presets
mkdir -p %{buildroot}%{_presetdir}
%global _userpresetdir %{dirname:%{_presetdir}}/user-preset
mkdir -p %{buildroot}%{_userpresetdir}
install -m 0644 %{SOURCE3} %{buildroot}%{_presetdir}/
install -m 0644 %{SOURCE4} %{buildroot}%{_presetdir}/
install -m 0644 %{SOURCE5} %{buildroot}/%{_userpresetdir}/
install -m 0644 %{SOURCE6} %{buildroot}%{_presetdir}/


%files
%license LICENSE README.license
%config %attr(0644,root,root) %{_prefix}/lib/os-release
%config %attr(0644,root,root) %{_prefix}/lib/os.release.d/os-release-lirios
%{_sysconfdir}/os-release
%config %attr(0644,root,root) %{_sysconfdir}/fedora-release
%{_sysconfdir}/redhat-release
%{_sysconfdir}/system-release
%config %attr(0644,root,root) %{_sysconfdir}/system-release-cpe
%config(noreplace) %attr(0644,root,root) %{_sysconfdir}/issue
%config(noreplace) %attr(0644,root,root) %{_sysconfdir}/issue.net
%dir %{_sysconfdir}/yum.repos.d/
%config(noreplace) %{_sysconfdir}/yum.repos.d/*
%attr(0644,root,root) %{_rpmconfigdir}/macros.d/macros.dist
%dir %{_presetdir}/
%{_presetdir}/85-display-manager.preset
%{_presetdir}/90-default.preset
%{_presetdir}/99-default-disable.preset
%dir %{_userpresetdir}/
%{_userpresetdir}/90-default-user.preset


%changelog
* Fri Feb 22 2019 Pier Luigi Fiorini <pierluigi.fiorini@gmail.com> - 29-3
- Provides system-release(releasever) = 29 so that libdnf will know
  the Fedora version we are using and expand $releasever accordingly.

* Thu Jan 24 2019 Pier Luigi Fiorini <pierluigi.fiorini@gmail.com> - 29-2
- Enable dbus-daemon explicitely.

* Sat Jan 05 2019 Pier Luigi Fiorini <pierluigi.fiorini@gmail.com> - 29-1
- Update to Fedora 29.

* Mon Oct 08 2018 Pier Luigi Fiorini <pierluigi.fiorini@gmail.com> - 28-1
- Use the same version as Fedora since $releasever is often used,
  for example in the official dnf repository files.

* Sat Sep 15 2018 Pier Luigi Fiorini <pierluigi.fiorini@gmail.com> - 0.10.0-2
- Fix dist tag macros.

* Mon Sep 03 2018 Pier Luigi Fiorini <pierluigi.fiorini@gmail.com> - 0.10.0-1
- Setup for Liri OS 0.10.0.
