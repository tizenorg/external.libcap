#
# Please submit bugfixes or comments via http://bugs.meego.com/
#

Name:           libcap
Version:        2.21
Release:        1
VCS:            external/libcap#submit/trunk/20121022.071522-2-g987e044673c6ec4df12d1862a80b9a4650499a9b
Summary:        Library for getting and setting POSIX
Source:         http://www.kernel.org/pub/linux/libs/security/linux-privs/libcap2/%{name}-%{version}.tar.gz

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

mkdir -p %{buildroot}/usr/share/license
cp License %{buildroot}/usr/share/license/%{name}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%docs_package

%files
%manifest libcap.manifest
%defattr(-,root,root,-)
/%{_lib}/*.so.*
%{_sbindir}/*
/usr/share/license/%{name}

%files devel
%defattr(-,root,root,-)
%{_includedir}/*
/%{_lib}/*.so
%{_mandir}/*
