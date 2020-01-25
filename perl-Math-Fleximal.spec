#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Math
%define		pnam	Fleximal
Summary:	Math::Fleximal - Integers with flexible representations
Summary(pl.UTF-8):	Math::Fleximal - liczby całkowite z elastyczną reprezentacją
Name:		perl-Math-Fleximal
Version:	0.06
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	885a886fd7d9e4e21dab121348ff39ac
URL:		http://search.cpan.org/dist/Math-Fleximal/
BuildRequires:	perl-Module-Build
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a package for doing integer arithmetic while using a different
base representation than normal. In base n arithmetic you have n
symbols which have a representation. Author was going to call them
"glyphs", but being text strings they are not really. On Tye McQueen's
whimsical suggestion the author settled on the name Math::Fleximal,
the set of text representations is called a "flex", and the
representation of individual digits are the "flecks". These names are
somewhat unofficial... This allows you to do basic arithmetic using
whatever digits you want, and to convert from one to another. Like
Math::BigInt it is able to handle very large numbers, though
performance is not very good.

%description -l pl.UTF-8
Ten pakiet służy do arytmetyki na liczbach całkowitych przy użyciu
innej niż normalna reprezentacji. W arytmetyce o podstawie n jest n
symboli mających reprezentację. Autor zamierzał nazwać je "glifami",
ale jako że są to łańcuchy tekstowe, nie była to najlepsza nazwa. Po
dziwnej sugestii Tye McQueena moduł został nazwany Math::Fleximal,
zbiór tekstowych reprezentacji "fleksem", a reprezentacje pojedynczych
cyfr "flekami". Te nazwy nie są oficjalne... Moduł pozwala na
wykonywanie podstawowych działań arytmetycznych przy użyciu dowolnych
cyfr i przeliczanie ich między różnymi reprezentacjami. Podobnie do
Math::BigInt moduł może liczyć na bardzo dużych liczbach, ale
wydajność nie jest najlepsza.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	installdirs=vendor \
	destdir=$RPM_BUILD_ROOT
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Math/Fleximal.pm
%{_mandir}/man3/*
