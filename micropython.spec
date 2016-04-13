#
# Conditional build:
%bcond_without	tests		# build without tests

Summary:	Implementation of Python 3 with very low memory footprint
Name:		micropython
Version:	1.6
Release:	1
License:	MIT
Group:		Development/Languages/Python
Source0:	https://github.com/micropython/micropython/archive/v%{version}.tar.gz
# Source0-md5:	e5c53c2c19bb454d0854b2ed8896e43c
URL:		http://micropython.org/
BuildRequires:	libffi-devel
BuildRequires:	pkgconfig
BuildRequires:	python
BuildRequires:	python-modules
BuildRequires:	readline-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Implementation of Python 3 with very low memory footprint.

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
install -p unix/micropython $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/micropython
