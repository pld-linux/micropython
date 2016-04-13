%bcond_without	tests

Summary:	Implementation of Python 3 with very low memory footprint
Name:		micropython
Version:	1.6
Release:	1
License:	MIT
Group:		Development/Languages/Python
URL:		http://micropython.org/
Source0:	https://github.com/micropython/micropython/archive/v%{version}.tar.gz
# Source0-md5:	e5c53c2c19bb454d0854b2ed8896e43c
BuildRequires:	libffi-devel
BuildRequires:	python3-devel
BuildRequires:	readline-devel

%description
Implementation of Python 3 with very low memory footprint

%prep
%setup -q

%build
%{__make} -C unix \
	CC="%{__cc}" \
	V=1

%{?with_tests:%{__make} -C unix test}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}
install -pm 755 unix/micropython $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/micropython
