Summary:	'top' for PostgreSQL process
Name:		pg_top
Version:	3.6.2
Release:	11%{?dist}
License:	BSD
Group:		Applications/Databases
Source0:	http://pgfoundry.org/frs/download.php/1780/%{name}-%{version}.tar.bz2
URL:		http://pgfoundry.org/projects/ptop
# Reported upstream: http://pgfoundry.org/tracker/index.php?func=detail&aid=1010710&group_id=1000300&atid=1129
Patch0:     pg_top-3.6.2-fix-totals.patch
BuildRequires:	postgresql-devel
BuildRequires:	libtermcap-devel
BuildRequires:	elfutils-libelf-devel
Requires:	postgresql-server
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%if 0%{?fedora} >= 10
BuildRequires:  systemtap-sdt-devel
%endif


%description
pg_top is 'top' for PostgreSQL processes. See running queries, 
query plans, issued locks, and table and index statistics.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1

%build
%configure
make %{?_smp_mflags} CFLAGS="%{optflags}"

%install
rm -rf %{buildroot}

install -Dp -m 755 %{name} %{buildroot}%{_bindir}/%{name}
install -Dp -m 644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_mandir}/man1/%{name}*
%{_bindir}/%{name}
%doc FAQ HISTORY INSTALL LICENSE README TODO Y2K

%changelog
* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Sep 26 2009 Alexey Torkhov <atorkhov@gmail.com> - 3.6.2-8
- Fix display of cumulative statistics (BZ#525763)

* Fri Sep 25 2009 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 3.6.2-7
- starting building for EPEL too

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 15 2009 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 3.6.2-5
- fix buildrequires, systemtap-sdt-devel is required for <sys/sdt.h>

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jan 21 2009 - Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 3.6.2-3
- include %%{optflags} during compilation.
- include DOC files, including license file
- fix %%defattr
- remove pointless patch
- include BR elfutils-libelf-devel

* Wed Jan 21 2009 - Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 3.6.2-2
- Rebuild for Fedora 10

* Thu May 15 2008 - Devrim GUNDUZ <devrim@commandprompt.com> 3.6.2-1
- Update to 3.6.2

* Sat Apr 12 2008 - Devrim GUNDUZ <devrim@commandprompt.com> 3.6.2-0.1.beta3
- Rename to pg_top
- Update to 3.6.2 beta3

* Mon Mar 10 2008 - Devrim GUNDUZ <devrim@commandprompt.com> 3.6.1-1
- Update to 3.6.1

* Sun Jan 20 2008 - Devrim GUNDUZ <devrim@commandprompt.com> 3.6.1-1.beta3
- Update to 3.6.1-beta3

* Mon Dec 13 2007 - Devrim GUNDUZ <devrim@commandprompt.com> 3.6.1-1.beta2
- Initial RPM packaging for Fedora
