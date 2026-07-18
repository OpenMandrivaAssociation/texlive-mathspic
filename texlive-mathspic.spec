%global tl_name mathspic
%global tl_revision 79618
%global tl_bin_links mathspic:%{_texmfdistdir}/scripts/mathspic/mathspic.pl

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.13
Release:	%{tl_revision}.1
Summary:	A Perl filter program for use with PiCTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/mathspic
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mathspic.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mathspic.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(mathspic.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}
Provides:	texlive(%{tl_name}.bin) = %{tl_revision}
Provides:	texlive-%{tl_name}.bin = %{EVRD}

%description
MathsPIC(Perl) is a development of the earlier MathsPIC(DOS) program,
now implemented as a Perl script, being much more portable than the
earlier program. MathsPIC parses a plain text input file and generates a
plain text output-file containing commands for drawing a diagram.
Version 1.0 produces output containing PiCTeX and (La)TeX commands,
which may then be processed by plain TeX or LaTeX in the usual way.
MathsPIC also outputs a comprehensive log-file. MathsPIC facilitates
creating figures using PiCTeX by providing an environment for
manipulating named points and also allows the use of variables and maths
(advance, multiply, and divide)--in short--it takes the pain out of
PiCTeX. Both the original DOS version and the new Perl version are
available.

