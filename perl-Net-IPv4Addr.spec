%define modname Net-IPv4Addr
%define modver 0.10

Summary:	Perl modules to manipulates Ipv4 addresses
Name:		perl-%{modname}
Version:	%{modver}
Release:	20
License:	GPLv2+ or Artistic
Group:		System/Configuration/Networking
Url:		https://iNDev.iNsu.COM/IPv4Addr/
Source0:	https://cpan.metacpan.org/authors/id/F/FR/FRAJULAC/Net-IPv4Addr-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	make
BuildRequires:	perl(Test)
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


%files 
%doc README ChangeLog
%{_bindir}/ipv4calc
%{perl_vendorlib}/Net/*
%{perl_vendorlib}/auto/Net/*
%{_mandir}/man1/*
%{_mandir}/man3/*

