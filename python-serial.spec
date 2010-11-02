Name:			python-serial
Version:		2.5
Release:		%mkrel 1

Summary:	Python serial port extension
License:	Python license
Group:          Development/Python
URL:		http://pyserial.sourceforge.net
Source0:	http://downloads.sourceforge.net/pyserial/pyserial-%{version}.tar.gz

BuildArch:	noarch
BuildRequires:	python-devel
BuildRequires:	dos2unix
BuildRoot:	%{_tmppath}/%{name}-%{version}

Obsoletes:	pyserial < %{version}-%{release}
Provides:	pyserial = %{version}-%{release}

%description
This module encapsulates the access for the serial port.
It provides backends for Python running on Windows, Linux, BSD (possibly any 
POSIX compilant system) and Jython. The module named "serial" automatically 
selects the appropriate backend.

%prep
%setup -q -n pyserial-%{version}

#fix shebangs
perl -pi -e "s/#! python/#!\/usr\/bin\/env python/" serial/*.py
perl -pi -e "s/#!jython/#!\/usr\/bin\/env jython/" serial/*.py

#fix EOL
dos2unix examples/port_publisher.py

%install
rm -rf %{buildroot}
python setup.py install --root %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES.txt LICENSE.txt PKG-INFO README.txt examples
%{_bindir}/miniterm.py
%{python_sitelib}/serial
%{python_sitelib}/pyserial-%{version}-py%{py_ver}.egg-info
