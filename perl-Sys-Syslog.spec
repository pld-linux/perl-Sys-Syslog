#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Sys
%define	pnam	Syslog
Summary:	Sys::Syslog - Perl interface to the UNIX syslog(3) calls
#Summary(pl.UTF-8):	
Name:		perl-Sys-Syslog
Version:	0.27
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Sys/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c18de7bca86846c107df290d93414830
# generic URL, check or change before uncommenting
#URL:		http://search.cpan.org/dist/Sys-Syslog/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sys::Syslog is an interface to the UNIX syslog(3) program.
Call syslog() with a string priority and a list of printf() args
just like syslog(3).

You can find a kind of FAQ in "THE RULES OF SYS::SYSLOG".  Please read 
it before coding, and again before asking questions. 

# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a eg $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Sys/*.pm
%dir %{perl_vendorarch}/auto/Sys/Syslog
%{perl_vendorarch}/auto/Sys/Syslog/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Sys/Syslog/*.so
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
