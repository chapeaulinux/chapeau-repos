Summary:        Chapeau package repositories
Name:           chapeau-repos
Version:        21
Release:        3
License:        MIT
Group:          System Environment/Base
URL:            https://chapeaulinux.org
Source:         %{name}-%{version}.tar.bz2
Requires:       fedora-repos(%{version})
Requires:       chapeau-release
Obsoletes:      fedora-repos-anaconda < 21-1
Obsoletes:      fedora-repos-rawhide < 21-0.4
Obsoletes:      fedora-release-rawhide <= 21-0.7
Provides:       rpmfusion-free-release
Provides:       rpmfusion-nonfree-release
BuildArch:      noarch

%description
Chapeau package repository files for yum and dnf along with gpg public keys

%prep
%setup -q

%build

%install
# Install the keys
install -d -m 755 $RPM_BUILD_ROOT/etc/pki/rpm-gpg
install -m 644 RPM-GPG-KEY* $RPM_BUILD_ROOT/etc/pki/rpm-gpg/
install -d -m 755 $RPM_BUILD_ROOT/etc/yum.repos.d
for file in *repo ; do
  install -m 644 $file $RPM_BUILD_ROOT/etc/yum.repos.d
done

%files
%defattr(-,root,root,-)
%dir /etc/yum.repos.d
%config /etc/yum.repos.d/chapeau*.repo
%config /etc/yum.repos.d/adobe*.repo
%config /etc/yum.repos.d/korora*.repo
%config /etc/yum.repos.d/livna*.repo
%config /etc/yum.repos.d/playonlinux*.repo
%config /etc/yum.repos.d/virtualbox*.repo
%dir /etc/pki/rpm-gpg
/etc/pki/rpm-gpg/*

%changelog

* Thu Jul 16 2015 Chris Palmer(PhnxRbrn) <pennstate5013@gmail.com> 22
- Added Provides RPMFusion

* Wed Feb 04 2015 Vince Pooley 21-3
- Added includepkg paterns to korora.repo

* Sun Feb 01 2015 Vince Pooley 21-2
- Set enabled to 0 & skip_if_unavailable to 1 on the Livna repo

* Sat Jan 03 2015 Vince Pooley 21-1
- New Chapeau repository package for Chapeau 21


