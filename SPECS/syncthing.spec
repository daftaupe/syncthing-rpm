%define debug_package %{nil}
%define repo github.com/syncthing/syncthing
Name:           syncthing
Version:        0.14.49
Release:        1%{?dist}
Summary:        Open, trustworthy and decentralized sync

License:        MPLv2.0
URL:            https://%{repo}
Source0:        https://%{repo}/releases/download/v%{version}/%{name}-source-v%{version}.tar.gz

BuildRequires:  git golang systemd

AutoReq:        no
AutoReqProv:    no

%description
Syncthing replaces proprietary sync and cloud services with something open,
trustworthy and decentralized. Your data is your data alone and you deserve
to choose where it is stored, if it is shared with some third party and how
it's transmitted over the Internet.

%prep
%setup -q -c -n %{name}
mkdir -p $(dirname src/%{repo})
mv %{name} src/%{repo}

%build
export GOPATH="$(pwd)"
export PATH=$PATH:"$(pwd)"/bin
cd src/%{repo}
./build.sh noupgrade

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_userunitdir}

cp src/%{repo}/syncthing %{buildroot}%{_bindir}
cp src/%{repo}/etc/linux-systemd/system/syncthing\@.service  %{buildroot}%{_unitdir}
cp src/%{repo}/etc/linux-systemd/system/syncthing-resume.service  %{buildroot}%{_unitdir}
cp src/%{repo}/etc/linux-systemd/user/syncthing.service %{buildroot}%{_userunitdir}


%files
%{_bindir}/syncthing
%{_unitdir}/syncthing@.service
%{_unitdir}/syncthing-resume.service
%{_userunitdir}/syncthing.service
%license src/%{repo}/LICENSE

%changelog
* Wed Jul 25 2018 Pierre-Alain TORET <pierre-alain.toret@protonmail.com> 0.14.49-1
- Update to v0.14.49

* Tue Jun 05 2018 Pierre-Alain TORET <pierre-alain.toret@protonmail.com> 0.14.48-1
- Update to v0.14.48

* Tue May 01 2018 Pierre-Alain TORET <pierre-alain.toret@protonmail.com> 0.14.47-1
- Update to v0.14.47

* Thu Apr 05 2018 Pierre-Alain TORET <pierre-alain.toret@protonmail.com> 0.14.46-1
- Improve build process
- Add license file

* Thu Apr 05 2018 Pierre-Alain TORET <pierre-alain.toret@protonmail.com> 0.14.46
- Update to v0.14.46

* Wed Apr 04 2018 Pierre-Alain TORET <pierre-alain.toret@protonmail.com> 0.14.45
- Update to v0.14.45

* Sat Jan 13 2018 Pierre-Alain TORET <pierre-alain.toret@protonmail.com> 0.14.43
- Update to v0.14.43

* Wed Dec 27 2017 Pierre-Alain TORET <pierre-alain.toret@protonmail.com> 0.14.42
- Update to v0.14.42

* Wed Dec 06 2017 Pierre-Alain TORET <pierre-alain.toret@protonmail.com> 0.14.41
- Update to v0.14.41

* Wed Nov 15 2017 Pierre-Alain TORET <pierre-alain.toret@protonmail.com> 0.14.40
- Update to v0.14.40

* Thu Oct 12 2017 Pierre-Alain TORET <pierre-alain.toret@protonmail.com> 0.14.39
- Update to v0.14.39

* Wed Sep 20 2017 daftaupe <daftaupe@protonmail.com> 0.14.38
- Update to v0.14.38

* Thu Sep 07 2017 daftaupe <daftaupe@protonmail.com> 0.14.37
- Update to v0.14.37

* Fri Aug 25 2017 daftaupe <daftaupe@protonmail.com> 0.14.33
- Update to v0.14.33

* Tue Jul 25 2017 daftaupe <daftaupe@protonmail.com> 0.14.32
- Update to v0.14.32

* Tue Jun 27 2017 daftaupe <daftaupe@protonmail.com> 0.14.31
- Update to v0.14.31

* Tue Jun 13 2017 daftaupe <daftaupe@protonmail.com> 0.14.30
- Update to v0.14.30

* Mon Jun 12 2017 daftaupe <daftaupe@protonmail.com> 0.14.29
- Update to v0.14.29

* Mon Jun 12 2017 daftaupe <daftaupe@protonmail.com> 0.14.28
- Update to v0.14.28

* Mon Jun 12 2017 daftaupe <daftaupe@protonmail.com> 0.14.27
- Update to v0.14.27

* Mon Jun 12 2017 daftaupe <daftaupe@protonmail.com> 0.14.26
- Bump syncthing version 0.14.25 -> 0.14.26

* Sun Mar 26 2017 daftaupe <daftaupe@protonmail.com> 0.14.25
- Bump syncthing version 0.14.24 -> 0.14.25

* Sun Mar 26 2017 daftaupe <daftaupe@protonmail.com> 0.14.24
- Bump syncthing version 0.14.23 -> 0.14.24

* Fri Feb 10 2017 daftaupe <daftaupe@protonmail.com> 0.14.23
- Adapted from Javier Wilson spec file to build from source tarball

* Thu Feb  9 2017 daftaupe <daftaupe@protonmail.com> 0.14.23
- Bump syncthing version 0.14.7 -> 0.14.23

* Thu Sep 22 2016 Logan Owen <logan@s1network.com> 0.14.7
- Bump syncthing version 0.13.1 -> 0.14.7

* Mon Feb 08 2016 Martin Lazarov <martin@lazarov.bg> 0.13.1
- Initial spec version
