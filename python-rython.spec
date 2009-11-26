%define	module	rython

Summary:	Transparently mixes Ruby code into Python
Name:		python-%{module}
Version:	0.0.1
Release:	%mkrel 1
License:	BSD
Group:		Development/Python
Url:		http://pypi.python.org/pypi/rython/
Source0:	%{module}-%{version}.tar.gz
%py_requires -d
Requires:	ruby
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
If you've ever needed to use Ruby for a particular task, but wanted to use
Python as your primary language, Rython lets you easily mix the two languages
together.

Why would I want to mix Ruby and Python? There are many reasons:
* you need a Ruby Gem that provides unique functionality which no Python module
  provides
* you need a simpler syntax for manipulating regular expressions
* you want to quickly bridge to code you've already written in Ruby

%prep
%setup -qn %{module}-%{version}

%build
python setup.py build

%install
rm -rf %{buildroot}
python setup.py install --root=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README.txt LICENSE.txt
%dir %{python_sitelib}/%{module}
%{python_sitelib}/%{module}/*.py*
%{python_sitelib}/%{module}*.egg-info

