Name:           liri-stable-repos
Summary:        Liri stable repository
Version:        1
Release:        1%{?dist}
License:        MIT
Source0:        plfiorini-liri-stable.repo

BuildArch:      noarch

%description
Liri stable repository dnf configuration.


%prep
%setup -c -T


%build


%install
# Install the .repo file
install -dm 755 %{buildroot}%{_sysconfdir}/yum.repos.d
install -pm 644 %{SOURCE0} \
    %{buildroot}%{_sysconfdir}/yum.repos.d


%files
%config(noreplace) %{_sysconfdir}/yum.repos.d/*


%changelog
* Sat Sep 15 2018 Pier Luigi Fiorini <pierluigi.fiorini@gmail.com> - 1-1
- Initial packaging.
