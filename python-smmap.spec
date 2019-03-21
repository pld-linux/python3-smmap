#
# Conditional build:
%bcond_without	python2	# CPython 2.x module
%bcond_without	python3	# CPython 3.x module
%bcond_without	tests	# unit tests

%define		module	smmap
Summary:	A pure Python implementation of a sliding window memory map manager
Summary(pl.UTF-8):	Czysto pythonowa implementacja zarządcy odwzorowania w pamięci z przesuwnym oknem
Name:		python-%{module}
Version:	2.0.5
Release:	2
License:	BSD
Group:		Development/Languages/Python
#Source0Download: https://github.com/gitpython-developers/smmap/releases
Source0:	https://github.com/gitpython-developers/smmap/archive/v%{version}/%{module}-%{version}.tar.gz
# Source0-md5:	e20f277aa4d654c85383d582c6339eb6
URL:		https://github.com/gitpython-developers/smmap
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-nose
BuildRequires:	python-nosexcover
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-nose
BuildRequires:	python3-nosexcover
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A pure Python implementation of a sliding window memory map manager.

%description -l pl.UTF-8
Czysto pythonowa implementacja zarządcy odwzorowania w pamięci z
przesuwnym oknem.

%package -n python3-%{module}
Summary:	A pure Python implementation of a sliding window memory map manager
Summary(pl.UTF-8):	Czysto pythonowa implementacja zarządcy odwzorowania w pamięci z przesuwnym oknem
Group:		Development/Languages/Python
Requires:	python3-modules >= 1:3.4

%description -n python3-%{module}
A pure Python implementation of a sliding window memory map manager.

%description -n python3-%{module} -l pl.UTF-8
Czysto pythonowa implementacja zarządcy odwzorowania w pamięci z
przesuwnym oknem.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/smmap/test

%py_postclean
%endif

%if %{with python3}
%py3_install

%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/smmap/test
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%dir %{py_sitescriptdir}/smmap
%{py_sitescriptdir}/smmap/*.py[co]
%{py_sitescriptdir}/smmap2-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%dir %{py3_sitescriptdir}/smmap
%{py3_sitescriptdir}/smmap/*.py
%{py3_sitescriptdir}/smmap/__pycache__
%{py3_sitescriptdir}/smmap2-%{version}-py*.egg-info
%endif
