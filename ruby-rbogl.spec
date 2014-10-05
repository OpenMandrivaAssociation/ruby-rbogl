%define name ruby-rbogl
%define version 0.32g
%define release  20

Summary: Ruby extension library to use OpenGL
Name: %{name}
Version: %{version}
Release: %{release}
URL: http://www2.giganet.net/~yoshi/
Source0: rbogl-%{version}.tar.bz2
Patch0:  opengl-0.32g-RString.patch
Patch1:	opengl-0.32g-ruby2.0.patch
License: GPL
Group: Development/Ruby
Requires: ruby >= 1.8
BuildRequires: ruby-devel
BuildRequires: pkgconfig(x11)
BuildRequires: mesa-common-devel

%description
Ruby extension library to use OpenGL.

%prep
%setup -q -n opengl-%{version}
%apply_patches

%build
ruby extconf.rb --with-x11-lib=/usr/%{_lib}/X11
CFLAGS=${RPM_OPT_FLAGS} make
sed -i 's|/usr/local|/usr|' sample/*.rb

%install
make install DESTDIR=%buildroot
rm -rf sample/.svn

%files
%{ruby_sitearchdir}/*.so
%doc README.EUC ChangeLog sample 


%changelog
* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 0.32g-10mdv2011.0
+ Revision: 669461
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 0.32g-9mdv2011.0
+ Revision: 607381
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 0.32g-8mdv2010.1
+ Revision: 523934
- rebuilt for 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.32g-7mdv2010.0
+ Revision: 426966
- rebuild

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 0.32g-6mdv2009.0
+ Revision: 219587
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Apr 21 2007 Pascal Terjan <pterjan@mandriva.org> 0.32g-5mdv2008.0
+ Revision: 16627
- Use Development/Ruby group

* Sat Apr 21 2007 Pascal Terjan <pterjan@mandriva.org> 0.32g-4mdv2008.0
+ Revision: 16625
- Use std macros


* Mon Mar 19 2007 Pascal Terjan <pterjan@mandriva.org> 0.32g-3mdv2007.1
+ Revision: 146572
- rbogl switched to svn
- Import ruby-rbogl

* Mon Sep 11 2006 Emmanuel Andry <eandry@mandriva.org> 0.32g-2mdv2007.0
- fix deps

* Tue Jul 04 2006 Emmanuel Andry <eandry@mandriva.org> 0.32g-1mdv2007.0
- 0.32g
- %%mkrel
- fix deps
- fix X11 path

* Fri Apr 01 2005 Pascal Terjan <pterjan@mandrake.org> 0.32f-3mdk
- lib64 fix

* Sat Jul 24 2004 Pascal Terjan <pterjan@mandrake.org> 0.32f-2mdk
- fix install path

* Wed Jul 21 2004 Pascal Terjan <pterjan@mandrake.org> 0.32f-1mdk 
- 0.32f

