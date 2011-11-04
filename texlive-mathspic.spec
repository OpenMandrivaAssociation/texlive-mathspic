# revision 23661
# category Package
# catalog-ctan /graphics/mathspic
# catalog-date 2011-06-24 10:29:05 +0200
# catalog-license lppl
# catalog-version 1.13
Name:		texlive-mathspic
Version:	1.13
Release:	1
Summary:	A Perl filter program for use with PiCTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/mathspic
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mathspic.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mathspic.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Provides:	texlive-mathspic.bin = %{EVRD}
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
MathsPIC(Perl) is a development of the earlier MathsPIC(DOS)
program, now implemented as a Perl script, being much more
portable than the earlier program. MathsPIC parses a plain text
input file and generates a plain text output-file containing
commands for drawing a diagram. Version 1.0 produces output
containing PiCTeX and (La)TeX commands, which may then be
processed by plain TeX or LaTeX in the usual way. MathsPIC also
outputs a comprehensive log-file. MathsPIC facilitates creating
figures using PiCTeX by providing an environment for
manipulating named points and also allows the use of variables
and maths (advance, multiply, and divide)--in short--it takes
the pain out of PiCTeX. Both the original DOS version and the
new Perl version are available.

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
%{_bindir}/mathspic
%{_texmfdistdir}/scripts/mathspic/mathspic.pl
%{_texmfdistdir}/tex/latex/mathspic/mathspic.sty
%doc %{_texmfdistdir}/doc/latex/mathspic/HELP.txt
%doc %{_texmfdistdir}/doc/latex/mathspic/MATHSPIC.BAT
%doc %{_texmfdistdir}/doc/latex/mathspic/README.txt
%doc %{_texmfdistdir}/doc/latex/mathspic/grabtexdata.tex
%doc %{_texmfdistdir}/doc/latex/mathspic/mathsPICfigures.zip
%doc %{_texmfdistdir}/doc/latex/mathspic/mathsPICmanual.pdf
%doc %{_texmfdistdir}/doc/latex/mathspic/mathsPICmanual.zip
%doc %{_texmfdistdir}/doc/latex/mathspic/mathspic.1
%doc %{_texmfdistdir}/doc/latex/mathspic/mathspic.lib
%doc %{_texmfdistdir}/doc/latex/mathspic/mathspic.sh
%doc %{_texmfdistdir}/doc/latex/mathspic/sourcecode113.html
%doc %{_texmfdistdir}/doc/latex/mathspic/sourcecode113.nw
%doc %{_texmfdistdir}/doc/latex/mathspic/sourcecode113.pdf
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
    ln -sf %{_texmfdistdir}/scripts/mathspic/mathspic.pl mathspic
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
