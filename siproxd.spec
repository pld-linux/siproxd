Summary:	A SIP masquerading proxy with RTP support
Name:		siproxd
Version:	0.3.1
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	%{name}-%{version}.tar.gz
URL:		http://siproxd.sourceforge.net/
BuildRequires:	libosip2 >= 1.99.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Siprox is an proxy/masquerading daemon for the SIP protocol. It
handles registrations of SIP clients on a private IP network and
performs rewriting of the SIP message bodies to make SIP connections
possible via an masquerading firewall. It allows SIP clients (like
kphone, linphone) to work behind an IP masquerading firewall or
router.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README AUTHORS NEWS ChangeLog
%attr(755,root,root) %{_bindir}/siproxd
