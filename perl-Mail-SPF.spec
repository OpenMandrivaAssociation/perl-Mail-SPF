%define real_name Mail-SPF

Summary:	Perl implementation of Sender Policy Framework and Sender ID
Name:		perl-%{real_name}
Version:	2.005
Release:	%mkrel 2
License:	BSD
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	http://search.cpan.org/CPAN/authors/id/J/JM/JMEHNLE/mail-spf/%{real_name}-v%{version}.tar.bz2
BuildRequires:	perl-devel
BuildRequires:	perl-Error
BuildRequires:	perl-Mail-SPF-Test
BuildRequires:	perl-Module-Build
BuildRequires:	perl-NetAddr-IP
BuildRequires:	perl-Net-DNS
BuildRequires:	perl-Net-DNS-Resolver-Programmable
BuildRequires:	perl-URI
BuildRequires:	perl-version
BuildRequires:	perl-YAML
BuildRequires:	perl-Test-Pod
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Mail::SPF is an object-oriented Perl implementation of the Sender Policy
Framework (SPF) e-mail sender authentication system <http://www.openspf.org>.

It supports both the TXT and SPF RR types as well as both SPFv1 (v=spf1) and
Sender ID (spf2.0) records, and it is fully compliant to RFCs 4408 and 4406.
(It does not however implement the patented PRA address selection algorithm
described in RFC 4407.)

%package -n	spf-tools
Summary:	SPF tools (spfquery, spfd) based on the Mail::SPF Perl module
Group:		Development/Perl
#Obsoletes:	perl-Mail-SPF-Query
#Provides:	perl-Mail-SPF-Query = %{version}-%{release}

%description -n	spf-tools
A collection of Sender Policy Framework (SPF) tools that are based on the
fully RFC-conforming Mail::SPF Perl module.  The following tools are included
in this package:

 * mail-spfquery:  A command-line tool for performing SPF checks.
 * mail-spfd:      A daemon for services that perform SPF checks frequently.

%prep

%setup -q -n %{real_name}-v%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

#%%check
#make test

%install
rm -rf %{buildroot}

%makeinstall_std

# fix file clash with perl-Mail-SPF-Query
mv %{buildroot}%{_bindir}/spfquery %{buildroot}%{_bindir}/mail-spfquery
mv %{buildroot}%{_sbindir}/spfd %{buildroot}%{_sbindir}/mail-spfd
mv %{buildroot}%{_mandir}/man1/spfquery.1 %{buildroot}%{_mandir}/man1/mail-spfquery.1 

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES README TODO
%{perl_vendorlib}/Mail/*.pm
%{perl_vendorlib}/Mail/SPF/Mech/*.pm
%{perl_vendorlib}/Mail/SPF/Mod/*.pm
%{perl_vendorlib}/Mail/SPF/*.pm
%{perl_vendorlib}/Mail/SPF/v1/*.pm
%{perl_vendorlib}/Mail/SPF/v2/*.pm
%{_mandir}/man3/*

%files -n spf-tools
%defattr(-,root,root)
%{_bindir}/mail-spfquery
%{_sbindir}/mail-spfd
%{_mandir}/man1/mail-spfquery.1*
