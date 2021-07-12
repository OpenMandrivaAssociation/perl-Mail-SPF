%define modname	Mail-SPF
%define modver 2.9.0

Summary:	Perl implementation of Sender Policy Framework and Sender ID

Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	7
License:	BSD
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Mail/%{modname}-v%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Error)
BuildRequires:	perl(Mail::SPF::Test)
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(NetAddr::IP)
BuildRequires:	perl(Net::DNS)
BuildRequires:	perl(Net::DNS::Resolver::Programmable)
BuildRequires:	perl(Test::Pod)
BuildRequires:	perl(URI)
BuildRequires:	perl(YAML)
BuildRequires:	perl-version

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

%description -n	spf-tools
A collection of Sender Policy Framework (SPF) tools that are based on the
fully RFC-conforming Mail::SPF Perl module.  The following tools are included
in this package:

 * mail-spfquery:	A command-line tool for performing SPF checks.
 * mail-spfd:	A daemon for services that perform SPF checks frequently.

%prep
%setup -qn %{modname}-v%{modver}

%build
%__perl Build.PL installdirs=vendor
./Build

%check
#./Build test

%install
./Build install destdir=%{buildroot}

# fix file clash with perl-Mail-SPF-Query
mv %{buildroot}%{_bindir}/spfquery %{buildroot}%{_bindir}/mail-spfquery
mv %{buildroot}%{_sbindir}/spfd %{buildroot}%{_sbindir}/mail-spfd
mv %{buildroot}%{_mandir}/man1/spfquery.1 %{buildroot}%{_mandir}/man1/mail-spfquery.1 

%files
%doc CHANGES README TODO
%{perl_vendorlib}/Mail/*.pm
%{perl_vendorlib}/Mail/SPF/Mech/*.pm
%{perl_vendorlib}/Mail/SPF/Mod/*.pm
%{perl_vendorlib}/Mail/SPF/*.pm
%{perl_vendorlib}/Mail/SPF/v1/*.pm
%{perl_vendorlib}/Mail/SPF/v2/*.pm
%{_mandir}/man3/*

%files -n spf-tools
%{_bindir}/mail-spfquery
%{_sbindir}/mail-spfd
%{_mandir}/man1/mail-spfquery.1*
