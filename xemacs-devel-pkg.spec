Summary:	Emacs Lisp developer support
Summary(pl.UTF-8):	Wsparcie dla programistów Emacs Lisp
Name:		xemacs-devel-pkg
%define 	srcname	xemacs-devel
Version:	1.80
Release:	1
License:	GPL
Group:		Applications/Editors/Emacs
Source0:	http://ftp.xemacs.org/xemacs/packages/%{srcname}-%{version}-pkg.tar.gz
# Source0-md5:	50a2fe1426937ae8e9d04d1b9138bb09
Patch0:		%{name}-info.patch
URL:		http://www.xemacs.org/
BuildRequires:	texinfo
BuildArch:	noarch
Conflicts:	xemacs-sumo
Requires:	xemacs
Requires:	xemacs-base-pkg
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Emacs Lisp developer support.

%description -l pl.UTF-8
Wsparcie dla programistów Emacs Lisp.

%prep
%setup -q -c
%patch -P0 -p1

%build
makeinfo man/xemacs-devel/patcher.texi

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/xemacs-packages/lisp,%{_infodir}}

cp -a lisp/* $RPM_BUILD_ROOT%{_datadir}/xemacs-packages/lisp

install *.info* $RPM_BUILD_ROOT%{_infodir}

# remove .el file if corresponding .elc file exists
find $RPM_BUILD_ROOT -type f -name "*.el" | while read i; do test ! -f ${i}c || rm -f $i; done

%post	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc lisp/xemacs-devel/ChangeLog
%dir %{_datadir}/xemacs-packages/lisp/*
%{_datadir}/xemacs-packages/lisp/*/*.el*
%{_infodir}/*.info*
