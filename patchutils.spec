#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : patchutils
Version  : 0.3.4
Release  : 14
URL      : http://cyberelk.net/tim/data/patchutils/stable/patchutils-0.3.4.tar.xz
Source0  : http://cyberelk.net/tim/data/patchutils/stable/patchutils-0.3.4.tar.xz
Summary  : A collection of programs for manipulating patch files.
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: patchutils-bin
Requires: patchutils-doc
BuildRequires : rpm-common
BuildRequires : vim
BuildRequires : xmlto

%description
This is a collection of programs that can manipulate patch files in
useful ways such as interpolating between two pre-patches, combining
two incremental patches, fixing line numbers in hand-edited patches,
and simply listing the files modified by a patch.

%package bin
Summary: bin components for the patchutils package.
Group: Binaries

%description bin
bin components for the patchutils package.


%package doc
Summary: doc components for the patchutils package.
Group: Documentation

%description doc
doc components for the patchutils package.


%prep
%setup -q -n patchutils-0.3.4

%build
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/combinediff
/usr/bin/dehtmldiff
/usr/bin/editdiff
/usr/bin/espdiff
/usr/bin/filterdiff
/usr/bin/fixcvsdiff
/usr/bin/flipdiff
/usr/bin/grepdiff
/usr/bin/interdiff
/usr/bin/lsdiff
/usr/bin/recountdiff
/usr/bin/rediff
/usr/bin/splitdiff
/usr/bin/unwrapdiff

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
