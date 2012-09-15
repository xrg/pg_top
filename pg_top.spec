%define git_repo pg_top
%define git_head HEAD

%define version %git_get_ver

Summary:	'top' for PostgreSQL process
Name:		pg_top
Version:	%{version}
Release:	%mkrel %git_get_rel
License:	BSD
Group:		Applications/Databases
Source:		%git_bs_source %{name}-%{version}.tar.gz
URL:		http://pgfoundry.org/projects/ptop
BuildRequires:	postgresql-devel
BuildRequires:	libtermcap-devel
%if %{_target_vendor} == mageia
BuildRequires:	libelfutils-devel
%else
BuildRequires:	elfutils-libelf-devel
%endif
Requires:	postgresql-server
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%if 0%{?fedora} >= 10
BuildRequires:  systemtap-sdt-devel
%endif


%description
pg_top is 'top' for PostgreSQL processes. See running queries, 
query plans, issued locks, and table and index statistics.

%prep
%git_get_source
%setup -q

%build
./autogen.sh
%configure
%make

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

%changelog -f %{_sourcedir}/%{name}-changelog.gitrpm.txt
