#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Math
%define		pnam	Fleximal
Summary:	Math::Fleximal - Integers with flexible representations
Summary(pl):	Math::Fleximal - liczby ca�kowite z elastyczn� reprezentacj�
Name:		perl-Math-Fleximal
Version:	0.03
Release:	2
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e88f4b1a2034ae8768ecf64c1a17333e
BuildRequires:	perl-devel >= 5.6
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

%description -l pl
Ten pakiet s�u�y do arytmetyki na liczbach ca�kowitych przy u�yciu
innej ni� normalna reprezentacji. W arytmetyce o podstawie n jest n
symboli maj�cych reprezentacj�. Autor zamierza� nazwa� je "glifami",
ale jako �e s� to �a�cuchy tekstowe, nie by�a to najlepsza nazwa.
Po dziwnej sugestii Tye McQueena modu� zosta� nazwany Math::Fleximal,
zbi�r tekstowych reprezentacji "fleksem", a reprezentacje pojedynczych
cyfr "flekami". Te nazwy nie s� oficjalne... Modu� pozwala na
wykonywanie podstawowych dzia�a� arytmetycznych przy u�yciu dowolnych
cyfr i przeliczanie ich mi�dzy r�nymi reprezentacjami. Podobnie do
Math::BigInt modu� mo�e liczy� na bardzo du�ych liczbach, ale
wydajno�� nie jest najlepsza.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Math/Fleximal.pm
%{_mandir}/man3/*
