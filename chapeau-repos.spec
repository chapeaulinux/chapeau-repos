Summary:        Chapeau package repositories
Name:           chapeau-repos
Version:        23
Release:        2
License:        MIT
Group:          System Environment/Base
URL:            https://chapeaulinux.org
Source:         %{name}-%{version}.tar.bz2
BuildArch:      noarch

%description
Chapeau package repository files for yum and dnf along with gpg public keys

%prep
%setup -c

%build

%install
# Install the keys
install -d -m 755 $RPM_BUILD_ROOT/etc/pki/rpm-gpg
install -m 644 RPM-GPG-KEY* $RPM_BUILD_ROOT/etc/pki/rpm-gpg/
install -d -m 755 $RPM_BUILD_ROOT/etc/yum.repos.d
for file in *repo ; do
  install -m 644 $file $RPM_BUILD_ROOT/etc/yum.repos.d
done

%post
test -f /etc/yum.repos.d/korora.repo && rm -f /etc/yum.repos.d/korora.repo

%files
%defattr(-,root,root,-)
%dir /etc/yum.repos.d
%config /etc/yum.repos.d/chapeau*.repo
%config /etc/yum.repos.d/adobe*.repo
%config /etc/yum.repos.d/playonlinux*.repo
%config /etc/yum.repos.d/virtualbox*.repo
%config /etc/yum.repos.d/rpmfusion*.repo
%dir /etc/pki/rpm-gpg
/etc/pki/rpm-gpg/*

%changelog
* Wed Nov 18 2015 Vince Pooley 23-2
- Pull in changed RPMFusion GPG keys

* Tue Nov 03 2015 Vince Pooley 23-1
- Repos & keys updated for Chapeau 23
- Korora repo removed

* Sun May 24 2015 Vince Pooley 22-3
- RPMFusion free & non-free repos now enabled, development repos disabled.

* Sat Apr 18 2015 Vince Pooley 22-2
- RPMFusion development repos switched from mirrors to base

* Sat Apr 04 2015 Vince Pooley 22-1
- Livna removed
- Removed requirement for fedora-repos & chapeau-release
- Removed obsoletes

* Wed Feb 04 2015 Vince Pooley 21-3
- Added includepkg paterns to korora.repo

* Sun Feb 01 2015 Vince Pooley 21-2
- Set enabled to 0 & skip_if_unavailable to 1 on the Livna repo

* Sat Jan 03 2015 Vince Pooley 21-1
- New Chapeau repository package for Chapeau 21


