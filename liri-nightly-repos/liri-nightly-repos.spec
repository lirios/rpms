Name:           liri-nightly-repos
Summary:        Liri unstable repository
Version:        2
Release:        1%{?dist}
License:        MIT
Source0:        plfiorini-liri-nightly.repo

BuildArch:      noarch

%description
Liri nightly repository dnf configuration.


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
* Fri Dec 28 2018 Pier Luigi Fiorini <pierluigi.fiorini@gmail.com> - 2-1
- Rename to liri-nightly-repos.

* Sat Sep 15 2018 Pier Luigi Fiorini <pierluigi.fiorini@gmail.com> - 1-1
- Initial packaging.
