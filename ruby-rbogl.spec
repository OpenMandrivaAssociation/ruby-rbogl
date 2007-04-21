%define name ruby-rbogl
%define version 0.32g
%define release %mkrel 4

Summary: Ruby extension library to use OpenGL
Name: %{name}
Version: %{version}
Release: %{release}
URL: http://www2.giganet.net/~yoshi/
Source0: rbogl-%{version}.tar.bz2
License: GPL
Group: Development/Other
BuildRoot: %{_tmppath}/%{name}-buildroot
Requires: ruby >= 1.8
BuildRequires: ruby-devel libx11-devel mesaglu-devel mesaglut-devel

%description
Ruby extension library to use OpenGL.

%prep
%setup -q -n opengl-%{version}

%build
ruby extconf.rb --with-x11-lib=/usr/%{_lib}/X11
CFLAGS=${RPM_OPT_FLAGS} make
sed -i 's|/usr/local|/usr|' sample/*.rb

%install
rm -rf %buildroot

make install DESTDIR=%buildroot
rm -rf sample/.svn

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%{ruby_sitearchdir}/*.so
%doc README.EUC ChangeLog sample 


