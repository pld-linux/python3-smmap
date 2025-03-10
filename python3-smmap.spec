#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# unit tests

%define		module	smmap
Summary:	A pure Python implementation of a sliding window memory map manager
Summary(pl.UTF-8):	Czysto pythonowa implementacja zarządcy odwzorowania w pamięci z przesuwnym oknem
Name:		python3-%{module}
Version:	5.0.1
Release:	2
License:	BSD
Group:		Development/Languages/Python
#Source0Download: https://github.com/gitpython-developers/smmap/tags
Source0:	https://github.com/gitpython-developers/smmap/archive/v%{version}/%{module}-%{version}.tar.gz
# Source0-md5:	caa2f7b1b9ed70834d3e9459780201a7
URL:		https://github.com/gitpython-developers/smmap
BuildRequires:	python3-modules >= 1:3.7
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-pytest
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	sphinx-pdg-3
%endif
Requires:	python3-modules >= 1:3.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A pure Python implementation of a sliding window memory map manager.

%description -l pl.UTF-8
Czysto pythonowa implementacja zarządcy odwzorowania w pamięci z
przesuwnym oknem.

%package apidocs
Summary:	API documentation for Python smmap module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona smmap
Group:		Documentation

%description apidocs
API documentation for Python smmap module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona smmap.

%prep
%setup -q -n %{module}-%{version}

%build
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest smmap/test
%endif

%if %{with doc}
%{__make} -C doc html \
	SPHINXBUILD=sphinx-build-3
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/smmap/test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{py3_sitescriptdir}/smmap
%{py3_sitescriptdir}/smmap/*.py
%{py3_sitescriptdir}/smmap/__pycache__
%{py3_sitescriptdir}/smmap-%{version}-py*.egg-info

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc doc/build/html/{_static,*.html,*.js}
%endif
