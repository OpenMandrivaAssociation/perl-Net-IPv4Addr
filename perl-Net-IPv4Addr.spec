%define modname	Net-IPv4Addr
%define modver	0.10

Summary:	Perl modules to manipulates Ipv4 addresses
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	9
License:	GPLv2+ or Artistic
Group:		System/Configuration/Networking
Url:		http://iNDev.iNsu.COM/IPv4Addr/
Source0:	http://iNDev.iNsu.COM/sources/%{modname}-%{modver}.tar.bz2
BuildArch:	noarch
BuildRequires:	perl-devel

%description
Net::IPv4Addr provides methods for parsing IPv4 addresses both in traditional
address/netmask format and in the new CIDR format. There are also methods for
calculating the network and broadcast address and also to see check if a given
address is in a specific network.

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor 
%make

%check
make test

%install
%makeinstall_std

install -d %{buildroot}%{_sbindir}
mv -f %{buildroot}%{_bindir}/ipv4calc %{buildroot}%{_sbindir}/ipv4calc

%files 
%doc README ChangeLog
%{_sbindir}/ipv4calc
%{perl_vendorlib}/Net/*
%{perl_vendorlib}/auto/Net/*
%{_mandir}/man1/*
%{_mandir}/man3/*

