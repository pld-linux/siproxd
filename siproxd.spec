Summary:	A SIP masquerading proxy with RTP support
Summary(pl):	Proxy z maskarad± SIP ze wsparciem dla RTP
Name:		siproxd
Version:	0.3.5
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://dl.sourceforge.net/siproxd/%{name}-%{version}.tar.gz
# Source0-md5:	8db82f78bf71a04570a85bf897f5d5e5
URL:		http://siproxd.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libosip2-devel >= 2.0.0
BuildRequires:	libosip2 >= 2.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Siprox is an proxy/masquerading daemon for the SIP protocol. It
handles registrations of SIP clients on a private IP network and
performs rewriting of the SIP message bodies to make SIP connections
possible via an masquerading firewall. It allows SIP clients (like
kphone, linphone) to work behind an IP masquerading firewall or
router.

%description -l pl
Siprox jest to demon proxy/maskarady dla protoko³u SIP. Obs³uguje on
rejestracjê klientów SIP w prywatnej sieci IP oraz przepisuje
komunikaty SIP w sposób umo¿liwiaj±cy po³±czenia poprzez firewall z
maskarad±. Umo¿liwia on klientom (takim jak kphone, linphone) pracê
zza firewalla lub routera z maskarad±.

%prep
%setup -q

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}

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
%doc AUTHORS ChangeLog README RELNOTES TODO doc/FAQ   doc/siproxd.conf.example doc/siproxd_passwd.cfg
%attr(755,root,root) %{_bindir}/siproxd
