%define upstream_name    IO-Async
%define upstream_version 0.29

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    A Loop using an C<IO::Poll> object
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://search.cpan.org/CPAN/authors/id/P/PE/PEVANS/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Async::MergePoint)
BuildRequires: perl(File::Temp)
BuildRequires: perl(Heap)
BuildRequires: perl(IO::Poll)
BuildRequires: perl(Socket::GetAddrInfo)
BuildRequires: perl(Storable)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::Refcount)
BuildRequires: perl(Time::HiRes)
BuildRequires: perl(Module::Build::Compat)
BuildRequires: perl-common-sense
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes
%{_mandir}/man3/*
%perl_vendorlib/*


