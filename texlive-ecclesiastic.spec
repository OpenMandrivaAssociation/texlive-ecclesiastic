Name:		texlive-ecclesiastic
Version:	0.3
Release:	1
Summary:	Typesetting Ecclesiastic Latin
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ecclesiastic
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ecclesiastic.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ecclesiastic.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ecclesiastic.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package modifies the way the latin option to babel operates
when typesetting Latin. The style is somewhat 'frenchified' in
respect of punctuation spacings and footnote style; shortcuts
are available in order to set accents on all vowels, including
y and the diphthongs ae and oe.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/ecclesiastic
%doc %{_texmfdistdir}/doc/latex/ecclesiastic
#- source
%doc %{_texmfdistdir}/source/latex/ecclesiastic

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
