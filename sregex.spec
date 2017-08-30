Name:           sregex
Version:        0.0.1
Release:        1%{?dist}
Summary:        libsregex - A non-backtracking NFA/DFA-based Perl-compatible regex engine library for matching on large data streams

License:        BSD
URL:            https://github.com/openresty/%{name}
Source0:        https://github.com/openresty/%{name}/archive/v%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make

%description


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q


%build
make PREFIX=/usr %{?_smp_mflags}

%install
%make_install PREFIX=/usr
find %{buildroot} -name '*.la' -exec rm -f {} ';'


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%doc
%{_bindir}/*
/usr/lib/*.so*

%files devel
%doc
%{_bindir}/*
%{_includedir}/*
/usr/lib/*.so*


%changelog
* Wed Aug 30 2017 David Beitey <david.beitey@jcu.edu.au>
- First sregex package
