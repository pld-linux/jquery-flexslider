# TODO
# - demo package
%define		plugin	flexslider
Summary:	Fully responsive jQuery slider toolkit
Name:		jquery-%{plugin}
Version:	2.1
Release:	2
License:	GPL v2
Group:		Applications/WWW
Source0:	https://github.com/woothemes/FlexSlider/archive/version/2.1.tar.gz?/%{plugin}-%{version}.tgz
# Source0-md5:	600b83649e1cb12657e84170da605a46
Patch0:		https://github.com/Dizzzy/FlexSlider/commit/6a171c4c1b80edc3df10cfef710818107d5f7207.patch
# Patch0-md5:	54612e491caf02a96e688cf51eef5d70
URL:		http://www.woothemes.com/flexslider/
BuildRequires:	closure-compiler
BuildRequires:	js
BuildRequires:	rpmbuild(macros) >= 1.553
Requires:	jquery >= 1.4.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_datadir}/jquery/%{plugin}

%description
An awesome, fully responsive jQuery slider plugin.

%prep
%setup -q -n FlexSlider-version-%{version}
%patch0 -p1

%build
install -d build

# compress .js
for js in jquery.%{plugin}.js; do
	out=build/${js#*/}
%if 0%{!?debug:1}
	closure-compiler --js $js --charset UTF-8 --js_output_file $out
	js -C -f $out
%else
	cp -p $js $out
%endif
done

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}

cp -p build/jquery.%{plugin}.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.min.js
cp -p jquery.%{plugin}.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.js
ln -s %{plugin}-%{version}.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.src.js
ln -s %{plugin}-%{version}.min.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.js

cp -p %{plugin}.css $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.css
ln -s %{plugin}-%{version}.css $RPM_BUILD_ROOT%{_appdir}/%{plugin}.css

cp -a images/* $RPM_BUILD_ROOT%{_appdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.mdown
%{_appdir}
