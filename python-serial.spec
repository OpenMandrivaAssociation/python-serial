Name:			python-serial
Version:		3.2.1
Release:		2

Summary:	Python serial port extension
License:	Python license
Group:          Development/Python
URL:		http://pyserial.sourceforge.net
Source0:	https://github.com/pyserial/pyserial/releases/download/v%{version}/pyserial-%{version}.tar.gz

BuildArch:	noarch
BuildRequires:	python-devel
BuildRequires:	dos2unix

Obsoletes:	pyserial < %{version}-%{release}
Provides:	pyserial = %{version}-%{release}

%description
This module encapsulates the access for the serial port.
It provides backends for Python running on Windows, Linux, BSD (possibly any 
POSIX compilant system) and Jython. The module named "serial" automatically 
selects the appropriate backend.

%package -n python2-serial
Summary:        Python 2 serial port extension
Group:          Development/Python

%description -n python2-serial
This module encapsulates the access for the serial port.
It provides backends for Python running on Windows, Linux, BSD (possibly any
POSIX compilant system) and Jython. The module named "serial" automatically
selects the appropriate backend.

%prep
%setup -q -n pyserial-%{version}

#fix shebangs
perl -pi -e "s/#!(.*)python//" serial/*.py serial/*/*.py
perl -pi -e "s/#!jython//" serial/*.py serial/*/*.py

#fix EOL
dos2unix examples/port_publisher.py

cp -a . %{py2dir}

%install
pushd %py2dir
python2 setup.py install --root %{buildroot}
popd

python setup.py install --root %{buildroot}

%files
%doc CHANGES.rst LICENSE.txt PKG-INFO README.rst examples
%{_bindir}/miniterm.py
%{py_puresitedir}/serial
%{py_puresitedir}/pyserial-%{version}-py%{py_ver}.egg-info

%files -n python2-serial
%doc CHANGES.rst LICENSE.txt PKG-INFO README.rst examples
%{py2_puresitedir}/serial
%{py2_puresitedir}/pyserial-%{version}-py%{py2_ver}.egg-info
