# revision 19440
# category Package
# catalog-ctan /macros/latex/contrib/ecclesiastic
# catalog-date 2008-08-19 08:58:40 +0200
# catalog-license lppl
# catalog-version 0.1
Name:		texlive-ecclesiastic
Version:	0.1
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
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package modifies the way the latin option to babel operates
when typesetting Latin. The style is somewhat 'frenchified' in
respect of punctuation spacings and footnote style; shortcuts
are available in order to set accents on all vowels, including
y and the diphthongs ae and oe.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/ecclesiastic/ecclesiastic.sty
%doc %{_texmfdistdir}/doc/latex/ecclesiastic/README
%doc %{_texmfdistdir}/doc/latex/ecclesiastic/README.TEXLIVE
%doc %{_texmfdistdir}/doc/latex/ecclesiastic/ecclesiastic.pdf
%doc %{_texmfdistdir}/doc/latex/ecclesiastic/manifest.txt
#- source
%doc %{_texmfdistdir}/source/latex/ecclesiastic/ecclesiastic.dtx
%doc %{_texmfdistdir}/source/latex/ecclesiastic/ecclesiastic.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
