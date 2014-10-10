%define upstream_name    IO-Async
%define upstream_version 0.45

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	A Loop using an C<IO::Poll> object
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/P/PE/PEVANS/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Async::MergePoint)
BuildRequires:	perl(CPS)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(Heap)
BuildRequires:	perl(IO::Poll)
BuildRequires:	perl(Socket::GetAddrInfo)
BuildRequires:	perl(Storable)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::Identity)
BuildRequires:	perl(Test::Fatal)
BuildRequires:	perl(Test::More)
BuildRequires:	perl-Test-Pod
BuildRequires:	perl(Test::Refcount)
BuildRequires:	perl-Test-Warn
BuildRequires:	perl(Time::HiRes)
BuildRequires:	perl(Module::Build::Compat)
BuildRequires:	perl-common-sense
BuildArch:	noarch

%description
This collection of modules allows programs to be written that perform
asynchronous filehandle IO operations. A typical program using them would
consist of a single subclass of 'IO::Async::Loop' to act as a container o
other objects, which perform the actual IO work required by the program. As
as IO handles, the loop also supports timers and signal handlers, and
includes more higher-level functionallity built on top of these basic
parts.

Because there are a lot of classes in this collection, the following
overview gives a brief description of each.

File Handle IO
    A the IO::Async::Handle manpage object represents a single IO handle
    that is being managed. While in most cases it will represent a single
    filehandle, such as a socket (for example, an 'IO::Socket::INET'
    connection), it is possible to have separate reading and writing
    handles (most likely for a program's 'STDIN' and 'STDOUT' streams, or a
    pair of pipes connected to a child process).

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sun Nov 27 2011 Götz Waschk <waschk@mandriva.org> 0.450.0-1mdv2012.0
+ Revision: 733719
- update to new version 0.45

* Sun Oct 16 2011 Götz Waschk <waschk@mandriva.org> 0.440.0-1
+ Revision: 704891
- update to new version 0.44

* Fri Aug 05 2011 Götz Waschk <waschk@mandriva.org> 0.430.0-1
+ Revision: 693274
- update to new version 0.43

* Wed Jun 29 2011 Götz Waschk <waschk@mandriva.org> 0.420.0-1
+ Revision: 688213
- update to new version 0.42

* Mon Jun 20 2011 Götz Waschk <waschk@mandriva.org> 0.410.0-1
+ Revision: 686136
- update to new version 0.41

* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.400.0-2
+ Revision: 657442
- rebuild for updated spec-helper

* Tue Mar 15 2011 Götz Waschk <waschk@mandriva.org> 0.400.0-1
+ Revision: 644886
- update to new version 0.40

* Mon Feb 28 2011 Funda Wang <fwang@mandriva.org> 0.390.0-2
+ Revision: 640767
- rebuild to obsolete old packages

* Fri Feb 11 2011 Götz Waschk <waschk@mandriva.org> 0.390.0-1
+ Revision: 637250
- update to new version 0.39
- update build deps

* Fri Feb 04 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.380.0-1
+ Revision: 635801
- update to new version 0.38

* Fri Jan 21 2011 Götz Waschk <waschk@mandriva.org> 0.370.0-1
+ Revision: 631983
- new version

* Sun Jan 16 2011 Götz Waschk <waschk@mandriva.org> 0.360.0-1
+ Revision: 631139
- update to new version 0.36

* Wed Jan 05 2011 Götz Waschk <waschk@mandriva.org> 0.350.0-1mdv2011.0
+ Revision: 628688
- update to new version 0.35

* Fri Dec 31 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.340.0-1mdv2011.0
+ Revision: 626888
- new version

* Thu Dec 23 2010 Götz Waschk <waschk@mandriva.org> 0.330.0-1mdv2011.0
+ Revision: 624033
- update to new version 0.33

* Fri Dec 17 2010 Götz Waschk <waschk@mandriva.org> 0.320.0-1mdv2011.0
+ Revision: 622538
- update to new version 0.32

* Sat Nov 27 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.310.0-1mdv2011.0
+ Revision: 602094
- new version

* Wed Sep 22 2010 Götz Waschk <waschk@mandriva.org> 0.300.0-1mdv2011.0
+ Revision: 580486
- update to new version 0.30

* Sat Jul 10 2010 Götz Waschk <waschk@mandriva.org> 0.290.0-1mdv2011.0
+ Revision: 550489
- update build deps
- update to new version 0.29

* Thu Mar 11 2010 Götz Waschk <waschk@mandriva.org> 0.280.0-1mdv2010.1
+ Revision: 517948
- update to new version 0.28

* Fri Dec 25 2009 Götz Waschk <waschk@mandriva.org> 0.270.0-1mdv2010.1
+ Revision: 482200
- new version
- fix source URL

* Tue Nov 24 2009 Jérôme Quelin <jquelin@mandriva.org> 0.260.0-1mdv2010.1
+ Revision: 469442
- update to 0.26

* Fri Nov 06 2009 Götz Waschk <waschk@mandriva.org> 0.250.0-1mdv2010.1
+ Revision: 460843
- update to new version 0.25

* Fri Nov 06 2009 Götz Waschk <waschk@mandriva.org> 0.240.0-1mdv2010.1
+ Revision: 460829
- update build deps
- update to new version 0.24

* Thu Aug 20 2009 Jérôme Quelin <jquelin@mandriva.org> 0.230.0-1mdv2010.0
+ Revision: 418632
- update to 0.23

* Fri Jul 24 2009 Jérôme Quelin <jquelin@mandriva.org> 0.220.0-1mdv2010.0
+ Revision: 399268
- update to 0.22

* Mon Jun 29 2009 Götz Waschk <waschk@mandriva.org> 0.210.0-1mdv2010.0
+ Revision: 390518
- import perl-IO-Async


* Mon Jun 29 2009 cpan2dist 0.21-1mdv
- initial mdv release, generated with cpan2dist

