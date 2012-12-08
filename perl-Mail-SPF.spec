%define upstream_name    Mail-SPF
%define upstream_version 2.8.0

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    1

Summary:	Perl implementation of Sender Policy Framework and Sender ID
License:	BSD
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source:     http://www.cpan.org/modules/by-module/Mail/%{upstream_name}-v%{upstream_version}.tar.gz
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
BuildArch:	noarch

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

 * mail-spfquery:  A command-line tool for performing SPF checks.
 * mail-spfd:      A daemon for services that perform SPF checks frequently.

%prep
%setup -q -n %{upstream_name}-v%{upstream_version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

#%%check
#./Build test

%install
rm -rf %{buildroot}
./Build install destdir=%{buildroot}

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


%changelog
* Sat Jun 09 2012 Bernhard Rosenkraenzer <bero@bero.eu> 2.8.0-1
+ Revision: 803804
- Update to 2.8.0
- Don't obsolete perl-Mail-SPF-Query

* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 2.7.0-6
+ Revision: 765449
- rebuilt for perl-5.14.2
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 2.7.0-4
+ Revision: 667252
- mass rebuild

* Sun May 09 2010 Funda Wang <fwang@mandriva.org> 2.7.0-3mdv2010.1
+ Revision: 544110
- obsoletes perl-Mail-SPF-Query

* Mon Jan 11 2010 Guillaume Rousse <guillomovitch@mandriva.org> 2.7.0-2mdv2010.1
+ Revision: 489723
- use Module::Build
- spec cleanup

* Fri Nov 06 2009 Jérôme Quelin <jquelin@mandriva.org> 2.7.0-1mdv2010.1
+ Revision: 461793
- update to v2.007

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 2.006-2mdv2010.0
+ Revision: 426521
- rebuild

* Wed Dec 24 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.006-1mdv2009.1
+ Revision: 318290
- update to new version 2.006

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 2.005-3mdv2009.0
+ Revision: 223812
- rebuild

* Thu Mar 06 2008 Oden Eriksson <oeriksson@mandriva.com> 2.005-2mdv2008.1
+ Revision: 180448
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Jul 26 2007 Oden Eriksson <oeriksson@mandriva.com> 2.005-1mdv2008.0
+ Revision: 55913
- disable the test suite for now due to unknown failures...
- fix deps (perl-Test-Pod)
-fix deps (perl-YAML)
- fix deps (perl-version)
- Import perl-Mail-SPF



* Mon Jul 02 2007 Oden Eriksson <oeriksson@mandriva.com> 2.005-1mdv2008.0
- initial Mandriva package 
