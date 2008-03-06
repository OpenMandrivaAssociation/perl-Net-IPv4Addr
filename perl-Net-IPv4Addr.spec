Summary:	Perl modules to manipulates Ipv4 addresses
Name:		perl-Net-IPv4Addr
Version:	0.10
Release:	%mkrel 10

Source:		http://iNDev.iNsu.COM/sources/Net-IPv4Addr-%{version}.tar.bz2

License:	GPL or Artistic
Group:		System/Configuration/Networking
URL:		http://iNDev.iNsu.COM/IPv4Addr/
BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch:	noarch

%description
Net::IPv4Addr provides methods for parsing IPv4 addresses both in traditional
address/netmask format and in the new CIDR format. There are also methods for
calculating the network and broadcast address and also to see check if a given
address is in a specific network.

%prep
%setup -q -n Net-IPv4Addr-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor 
make

%check
make test

%install
rm -fr $RPM_BUILD_ROOT
%makeinstall_std

install -d $RPM_BUILD_ROOT%{_sbindir}
mv -f $RPM_BUILD_ROOT%{_bindir}/ipv4calc $RPM_BUILD_ROOT%{_sbindir}/ipv4calc

%clean
rm -fr $RPM_BUILD_ROOT

%files 
%defattr(-,root,root)
%doc README ChangeLog
%{_mandir}/*/*
%{_sbindir}/ipv4calc
%{perl_vendorlib}/Net/*
%{perl_vendorlib}/auto/Net/*


