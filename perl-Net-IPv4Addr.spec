%define upstream_name    Net-IPv4Addr
%define upstream_version 0.10

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 4

Summary:	Perl modules to manipulates Ipv4 addresses
License:	GPL+ or Artistic
Group:		System/Configuration/Networking
Url:		http://iNDev.iNsu.COM/IPv4Addr/
Source0:	http://iNDev.iNsu.COM/sources/%{upstream_name}-%{upstream_version}.tar.bz2

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
Net::IPv4Addr provides methods for parsing IPv4 addresses both in traditional
address/netmask format and in the new CIDR format. There are also methods for
calculating the network and broadcast address and also to see check if a given
address is in a specific network.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor 
make

%check
make test

%install
rm -fr %{buildroot}
%makeinstall_std

install -d %{buildroot}%{_sbindir}
mv -f %{buildroot}%{_bindir}/ipv4calc %{buildroot}%{_sbindir}/ipv4calc

%clean
rm -fr %{buildroot}

%files 
%defattr(-,root,root)
%doc README ChangeLog
%{_mandir}/*/*
%{_sbindir}/ipv4calc
%{perl_vendorlib}/Net/*
%{perl_vendorlib}/auto/Net/*
