%define dist_version %{fedora}
%define lirios_version 0.10.0

Name:           lirios-release
Summary:        Liri OS release files
Version:        %{dist_version}
Release:        2.20191204
License:        MIT
URL:            https://liri.io/
Source0:        LICENSE
Source1:        README.license
Source3:        85-display-manager.preset
Source4:        90-default.preset
Source5:        90-default-user.preset
Source6:        99-default-disable.preset

# for macros.systemd
BuildRequires:  systemd

BuildArch:      noarch

%description
Liri OS release files such as yum configs and various /etc/ files that
define the release.


%package common
Summary: Liri OS release files
Requires: lirios-release-variant = %{version}-%{release}

Obsoletes: redhat-release
Provides:  redhat-release
Obsoletes: lirios-release < 30-3

%description common
Release files common to all Liri OS variants.


%package desktop
Summary: Base package for the desktop specific variant of Liri OS

RemovePathPostfixes: .desktop
Requires:   filesystem
Provides:   lirios-release = %{version}-%{release}
Provides:   lirios-release-variant = %{version}-%{release}
Conflicts:  generic-release
Conflicts:  system-release
Provides:   system-release
Provides:   system-release(%{dist_version})
Provides:   system-release(releasever) = %{dist_version}
Provides:   base-module(platform:f%{dist_version})
Requires:   lirios-release-common = %{version}-%{release}

%description desktop
Provides a base package for Liri OS Desktop.


%package mobile
Summary: Base package for the mobile specific variant of Liri OS

RemovePathPostfixes: .mobile
Requires:   filesystem
Provides:   lirios-release = %{version}-%{release}
Provides:   lirios-release-variant = %{version}-%{release}
Conflicts:  generic-release
Conflicts:  system-release
Provides:   system-release
Provides:   system-release(%{dist_version})
Provides:   system-release(releasever) = %{dist_version}
Provides:   base-module(platform:f%{dist_version})
Requires:   lirios-release-common = %{version}-%{release}

%description mobile
Provides a base package for Liri OS Mobile.


%package embedded
Summary: Base package for the embedded specific variant of Liri OS

RemovePathPostfixes: .embedded
Requires:   filesystem
Provides:   lirios-release = %{version}-%{release}
Provides:   lirios-release-variant = %{version}-%{release}
Conflicts:  generic-release
Conflicts:  system-release
Provides:   system-release
Provides:   system-release(%{dist_version})
Provides:   system-release(releasever) = %{dist_version}
Provides:   base-module(platform:f%{dist_version})
Requires:   lirios-release-common = %{version}-%{release}

%description embedded
Provides a base package for Liri OS Embedded.


%prep
%setup -c -T
cp -a %{SOURCE0} %{SOURCE1} %{SOURCE3} %{SOURCE4} %{SOURCE5} %{SOURCE6} .


%build


%install
install -d %{buildroot}%{_prefix}/lib
echo "Liri OS release %{lirios_version}" > %{buildroot}%{_prefix}/lib/fedora-release

# Symlink the -release files
install -d %{buildroot}%{_sysconfdir}
ln -s ../usr/lib/fedora-release %{buildroot}%{_sysconfdir}/fedora-release
ln -s fedora-release %{buildroot}%{_sysconfdir}/redhat-release
ln -s fedora-release %{buildroot}%{_sysconfdir}/system-release

# Create base os-release file
cat << EOF >>%{buildroot}%{_prefix}/lib/os-release
NAME="Liri OS"
VERSION="%{lirios_version} (Base)"
ID=lirios
VERSION_ID=%{lirios_version}
PRETTY_NAME="Liri OS %{lirios_version}"
ANSI_COLOR="0;34"
EOF

# Create os-release file for desktop
cp -p %{buildroot}%{_prefix}/lib/os-release \
      %{buildroot}%{_prefix}/lib/os-release.desktop
echo "VARIANT=\"Desktop\"" >> %{buildroot}%{_prefix}/lib/os-release.desktop
echo "VARIANT_ID=desktop" >> %{buildroot}%{_prefix}/lib/os-release.desktop
sed -i -e "s|(Base)|(Desktop)|g" %{buildroot}%{_prefix}/lib/os-release.desktop

# Create os-release file for mobile
cp -p %{buildroot}%{_prefix}/lib/os-release \
      %{buildroot}%{_prefix}/lib/os-release.mobile
echo "VARIANT=\"Mobile\"" >> %{buildroot}%{_prefix}/lib/os-release.mobile
echo "VARIANT_ID=mobile" >> %{buildroot}%{_prefix}/lib/os-release.mobile
sed -i -e "s|(Base)|(Mobile)|g" %{buildroot}%{_prefix}/lib/os-release.mobile

# Create os-release file for embedded
cp -p %{buildroot}%{_prefix}/lib/os-release \
      %{buildroot}%{_prefix}/lib/os-release.embedded
echo "VARIANT=\"Embedded\"" >> %{buildroot}%{_prefix}/lib/os-release.embedded
echo "VARIANT_ID=embedded" >> %{buildroot}%{_prefix}/lib/os-release.embedded
sed -i -e "s|(Base)|(Embedded)|g" %{buildroot}%{_prefix}/lib/os-release.embedded

# Create the common /etc/issue
echo "\S" > %{buildroot}%{_prefix}/lib/issue
echo "Kernel \r on an \m (\l)" >> %{buildroot}%{_prefix}/lib/issue
echo >> %{buildroot}%{_prefix}/lib/issue
ln -s ../usr/lib/issue %{buildroot}%{_sysconfdir}/issue

# Create /etc/issue.net
echo "\S" > %{buildroot}%{_prefix}/lib/issue.net
echo "Kernel \r on an \m (\l)" >> %{buildroot}%{_prefix}/lib/issue.net
ln -s ../usr/lib/issue.net %{buildroot}%{_sysconfdir}/issue.net

# Remove the now useless base os-release
rm -f %{buildroot}%{_prefix}/lib/os-release

# Create /etc/issue.d
mkdir -p %{buildroot}%{_sysconfdir}/issue.d

# Create the symlink for /etc/os-release
ln -s ../usr/lib/os-release %{buildroot}%{_sysconfdir}/os-release

# Set up the dist tag macros
install -d -m 755 %{buildroot}%{_rpmconfigdir}/macros.d
cat >> %{buildroot}%{_rpmconfigdir}/macros.d/macros.dist << EOF
# dist macros.

%%fedora		%{dist_version}
%%dist		.fc%{dist_version}
%%fc%{dist_version}		1
EOF

# Add presets
mkdir -p %{buildroot}%{_presetdir}
%global _userpresetdir %{dirname:%{_presetdir}}/user-preset
mkdir -p %{buildroot}%{_userpresetdir}
install -m 0644 %{SOURCE3} %{buildroot}%{_presetdir}/
install -m 0644 %{SOURCE4} %{buildroot}%{_presetdir}/
install -m 0644 %{SOURCE5} %{buildroot}/%{_userpresetdir}/
install -m 0644 %{SOURCE6} %{buildroot}%{_presetdir}/


%files desktop
%{_prefix}/lib/os-release.desktop

%files mobile
%{_prefix}/lib/os-release.mobile

%files embedded
%{_prefix}/lib/os-release.embedded

%files common
%license LICENSE README.license
%{_prefix}/lib/fedora-release
%{_sysconfdir}/os-release
%{_sysconfdir}/fedora-release
%{_sysconfdir}/redhat-release
%{_sysconfdir}/system-release
%attr(0644,root,root) %{_prefix}/lib/issue
%config(noreplace) %{_sysconfdir}/issue
%attr(0644,root,root) %{_prefix}/lib/issue.net
%config(noreplace) %{_sysconfdir}/issue.net
%dir %{_sysconfdir}/issue.d
%attr(0644,root,root) %{_rpmconfigdir}/macros.d/macros.dist
%dir %{_presetdir}/
%{_presetdir}/85-display-manager.preset
%{_presetdir}/90-default.preset
%{_presetdir}/99-default-disable.preset
%dir %{_userpresetdir}/
%{_userpresetdir}/90-default-user.preset
