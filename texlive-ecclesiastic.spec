%global tl_name ecclesiastic
%global tl_revision 38172

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.3
Release:	%{tl_revision}.1
Summary:	Typesetting Ecclesiastic Latin
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/ecclesiastic
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ecclesiastic.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ecclesiastic.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ecclesiastic.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package modifies the way the latin option to babel operates when
typesetting Latin. The style is somewhat 'frenchified' in respect of
punctuation spacings and footnote style; shortcuts are available in
order to set accents on all vowels, including y and the diphthongs ae
and oe.

