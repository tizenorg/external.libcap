#
# Please submit bugfixes or comments via http://bugs.meego.com/
#

Name:           libcap
Version:        2.21
Release:        1
Summary:        Library for getting and setting POSIX
Source:         http://www.kernel.org/pub/linux/libs/security/linux-privs/libcap2/%{name}-%{version}.tar.gz
Source1001: packaging/libcap.manifest 

License:        LGPLv2+
Url:            http://ftp.kernel.org/pub/linux/libs/security/linux-privs/kernel-2.6/
Group:          System/Libraries
BuildRequires:  libattr-devel

%description
libcap is a library for getting and setting POSIX.1e (formerly POSIX 6)
draft 15 capabilities.

%package devel
Summary:        Development files for libcap
Group:          Development/Libraries
Requires:       %{name} = %{version}

%description devel
Development files (Headers, libraries for static linking, etc) for libcap.

libcap is a library for getting and setting POSIX.1e (formerly POSIX 6)
draft 15 capabilities.

Install libcap-devel if you want to develop or compile applications using
libcap.

%prep
%setup -q

%build
cp %{SOURCE1001} .
# libcap can not be build with _smp_mflags:
make PREFIX=%{_prefix} LIBDIR=%{_lib} SBINDIR=%{_sbindir} \
     INCDIR=%{_includedir} MANDIR=%{_mandir} COPTFLAG="%{optflags}"

%install
make RAISE_SETFCAP=no install DESTDIR=%{buildroot} \
             LIBDIR=%{buildroot}/%{_lib} \
             SBINDIR=%{buildroot}/%{_sbindir} \
             INCDIR=%{buildroot}/%{_includedir} \
             MANDIR=%{buildroot}/%{_mandir}/ \
             COPTFLAG="%{optflags}"

# remove static lib
rm -f %{buildroot}/%{_lib}/libcap.a

chmod +x %{buildroot}/%{_lib}/*.so.*

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%docs_package

%files
%manifest libcap.manifest
%defattr(-,root,root,-)
/%{_lib}/*.so.*
%{_sbindir}/*

%files devel
%manifest libcap.manifest
%defattr(-,root,root,-)
%{_includedir}/*
/%{_lib}/*.so
%{_mandir}/*

