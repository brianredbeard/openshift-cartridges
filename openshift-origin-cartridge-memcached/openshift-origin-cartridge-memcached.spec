%global cartridgedir %{_libexecdir}/openshift/cartridges/v2/memcached

Summary:       Embedded memcached support for OpenShift
Name:          openshift-origin-cartridge-memcached
Version:       1.2
Release:       1%{?dist}
Group:         Network/Daemons
License:       ASL 2.0
URL:           http://www.openshift.com
Source0:       http://mirror.openshift.com/pub/openshift-origin/source/%{name}/%{name}-%{version}.tar.gz
Requires:      memcached
Requires:      rubygem(openshift-origin-node)
Requires:      openshift-origin-node-util
BuildArch:     noarch

%description
Provides memcached cartridge support to OpenShift

%prep
%setup -q

%build
%__rm %{name}.spec

%install
%__mkdir -p %{buildroot}%{cartridgedir}
%__cp -r * %{buildroot}%{cartridgedir}

%post
%{_sbindir}/oo-admin-cartridge --action install --source %{cartridgedir}

%files
%dir %{cartridgedir}
%attr(0755,-,-) %{cartridgedir}/bin/
%attr(0755,-,-) %{cartridgedir}
%doc %{cartridgedir}/README.md
%doc %{cartridgedir}/COPYRIGHT
%doc %{cartridgedir}/LICENSE

%changelog
* Tue May 21 2013 Brian Harrington <bharrington@redhat.com> 1.2-1
- apparently none of my files were committed (bharrington@redhat.com)

* Tue May 21 2013 Brian Harrington <bharrington@redhat.com> 1.1-1
- new package built with tito

* Tue May 21 2013 Brian Harrington <bharrington@redhat.com> 1.0
- Creation of initial cartridge

