%define upstream_name    Net-IPv4Addr
%define upstream_version 0.10

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6

Summary:	Perl modules to manipulates Ipv4 addresses
License:	GPL+ or Artistic
Group:		System/Configuration/Networking
Url:		http://iNDev.iNsu.COM/IPv4Addr/
Source0:	http://iNDev.iNsu.COM/sources/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

%description
Net::IPv4Addr provides methods for parsing IPv4 addresses both in traditional
address/netmask format and in the new CIDR format. There are also methods for
calculating the network and broadcast address and also to see check if a given
address is in a specific network.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor 
make

%check
make test

%install
%makeinstall_std

install -d %{buildroot}%{_sbindir}
mv -f %{buildroot}%{_bindir}/ipv4calc %{buildroot}%{_sbindir}/ipv4calc

%files 
%doc README ChangeLog
%{_mandir}/*/*
%{_sbindir}/ipv4calc
%{perl_vendorlib}/Net/*
%{perl_vendorlib}/auto/Net/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.100.0-4mdv2012.0
+ Revision: 765530
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.100.0-3
+ Revision: 764054
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.100.0-2
+ Revision: 667274
- mass rebuild

* Mon Aug 03 2009 Jérôme Quelin <jquelin@mandriva.org> 0.100.0-1mdv2011.0
+ Revision: 407814
- rebuild using %%perl_convert_version

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.10-11mdv2009.0
+ Revision: 223872
- rebuild

* Thu Mar 06 2008 Oden Eriksson <oeriksson@mandriva.com> 0.10-10mdv2008.1
+ Revision: 180513
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sun Jan 14 2007 Olivier Thauvin <nanardon@mandriva.org> 0.10-9mdv2007.0
+ Revision: 108470
- rebuild

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - Import perl-Net-IPv4Addr

