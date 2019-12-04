Summary:        Liri OS repositories
Name:           lirios-repos
Version:        %{fedora}
Release:        20191018.1%{?dist}
License:        MIT
URL:            https://liri.io/

Source0:        plfiorini-lirios.repo
Source1:        plfiorini-liri-stable.repo
Source2:        plfiorini-liri-nightly.repo
Source3:        lirios.conf

Requires:       fedora-repos(%{fedora})

BuildArch:      noarch

%description
Liri OS package repository files for dnf.


%package stable
Summary:        Liri OS stable repository definitions
Requires:       lirios-repos = %{version}-%{release}

%description stable
This package provides the Liri OS repository definition for the 'stable' channel.


%package nightly
Summary:        Liri OS nightly repository definitions
Requires:       lirios-repos = %{version}-%{release}

%description nightly
This package provides the Liri OS repository definition for the 'nightly' channel.


%package ostree
Summary:        OSTree remote definition for Liri OS
Requires:       fedora-repos-ostree

%description ostree
This package provides the OSTree remote definition for Liri OS.


%prep
%setup -c -T


%build


%install
# Install the .repo file
install -dm 755 %{buildroot}/etc/yum.repos.d
install -pm 644 %{_sourcedir}/*.repo %{buildroot}/etc/yum.repos.d

# Install ostree remote config
install -d -m 755 %{buildroot}/etc/ostree/remotes.d/
install -m 644 %{_sourcedir}/lirios.conf %{buildroot}/etc/ostree/remotes.d/


%files
%config(noreplace) /etc/yum.repos.d/plfiorini-lirios.repo

%files stable
%config(noreplace) /etc/yum.repos.d/plfiorini-liri-stable.repo

%files nightly
%config(noreplace) /etc/yum.repos.d/plfiorini-liri-nightly.repo

%files ostree
/etc/ostree/remotes.d/lirios.conf
