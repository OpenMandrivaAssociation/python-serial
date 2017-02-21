Name:			python-serial
Version:		3.2.1
Release:		1

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
perl -pi -e "s/#! python/#!\/usr\/bin\/env python/" serial/*.py
perl -pi -e "s/#!jython/#!\/usr\/bin\/env jython/" serial/*.py

#fix EOL
dos2unix examples/port_publisher.py

cp -a . %{py2dir}

%install
pushd %py2dir
python2 setup.py install --root %{buildroot}
popd

python setup.py install --root %{buildroot}

%clean

%files
%doc CHANGES.rst LICENSE.txt PKG-INFO README.rst examples
%{_bindir}/miniterm.py
%{py_puresitedir}/serial
%{py_puresitedir}/pyserial-%{version}-py%{py_ver}.egg-info

%files -n python2-serial
%doc CHANGES.rst LICENSE.txt PKG-INFO README.rst examples
%{py2_puresitedir}/serial
%{py2_puresitedir}/pyserial-%{version}-py%{py2_ver}.egg-info


%changelog
* Tue Nov 02 2010 Jani Välimaa <wally@mandriva.org> 2.5-1mdv2011.0
+ Revision: 592136
- new version 2.5
- don't use recorded file list as it contains non-installed files
- don't set executable bit for examples
- ease python BR
- fix EOLs
- clean spec a bit

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 2.4-3mdv2010.0
+ Revision: 442482
- rebuild

* Sun Jan 04 2009 Funda Wang <fwang@mandriva.org> 2.4-2mdv2009.1
+ Revision: 324112
- rebuild

* Sat Jul 12 2008 Guillaume Bedot <littletux@mandriva.org> 2.4-1mdv2009.0
+ Revision: 234052
- 2.4
- rpm spec policy proposal changes
- fixed license

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Apr 17 2007 Guillaume Bedot <littletux@mandriva.org> 2.2-4mdv2008.0
+ Revision: 13985
- 2008 build ( should also build on previous versions )


* Wed Mar 07 2007 Guillaume Bedot <littletux@mandriva.org> 2.2-3mdv2007.0
+ Revision: 134430
- mention bug report
- fixed typo in filename
- rebuilt for python 2.5 (added egg-info file)
- moved to svn
- Created package structure for python-serial.



