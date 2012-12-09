# revision 26294
# category Package
# catalog-ctan /macros/latex/contrib/mh
# catalog-date 2011-06-09 21:04:00 +0200
# catalog-license lppl1.3
# catalog-version undef
Name:		texlive-mh
Version:	20110609
Release:	3
Summary:	The MH bundle
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/mh
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mh.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mh.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mh.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The mh bundle is a series of packages designed to enhance the
appearance of documents containing a lot of math. The main
backbone is amsmath, so those unfamiliar with this required
part of the LaTeX system will probably not find the packages
very useful. Component parts of the bundle are: breqn, empheq,
flexisym, mathstyle and mathtools, mhsetup, The empheq package
is a visual markup extension of amsmath. Empheq allows
sophisticated boxing and other marking of multi-line maths
displays, and fixes problems with the way that the ntheorem
package places end-of-theorem markers. The mathtools package
provides many useful tools for mathematical typesetting. It
fixes various deficiencies of amsmath and standard LaTeX. The
mhsetup package defines various programming tools needed by
both empheq and mathtools. The breqn package makes more easy
the business of preparing displayed equations in LaTeX,
including permitting automatic line-breaking within displayed
equations. (Breqn uses the mathstyle package to keep track of
the current maths typesetting style, something that raw TeX
hides from the programmer.).

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/mh/breqn.sty
%{_texmfdistdir}/tex/latex/mh/cmbase.sym
%{_texmfdistdir}/tex/latex/mh/empheq.sty
%{_texmfdistdir}/tex/latex/mh/flexisym.sty
%{_texmfdistdir}/tex/latex/mh/mathpazo.sym
%{_texmfdistdir}/tex/latex/mh/mathptmx.sym
%{_texmfdistdir}/tex/latex/mh/mathstyle.sty
%{_texmfdistdir}/tex/latex/mh/mathtools.sty
%{_texmfdistdir}/tex/latex/mh/mhsetup.sty
%{_texmfdistdir}/tex/latex/mh/msabm.sym
%doc %{_texmfdistdir}/doc/latex/mh/README
%doc %{_texmfdistdir}/doc/latex/mh/breqn-technotes.pdf
%doc %{_texmfdistdir}/doc/latex/mh/breqn.pdf
%doc %{_texmfdistdir}/doc/latex/mh/empheq.pdf
%doc %{_texmfdistdir}/doc/latex/mh/flexisym.pdf
%doc %{_texmfdistdir}/doc/latex/mh/mathstyle.pdf
%doc %{_texmfdistdir}/doc/latex/mh/mathtools.pdf
%doc %{_texmfdistdir}/doc/latex/mh/mhsetup.pdf
#- source
%doc %{_texmfdistdir}/source/latex/mh/breqn-technotes.tex
%doc %{_texmfdistdir}/source/latex/mh/breqn.dtx
%doc %{_texmfdistdir}/source/latex/mh/empheq.dtx
%doc %{_texmfdistdir}/source/latex/mh/flexisym.dtx
%doc %{_texmfdistdir}/source/latex/mh/mathstyle.dtx
%doc %{_texmfdistdir}/source/latex/mh/mathtools.dtx
%doc %{_texmfdistdir}/source/latex/mh/mhsetup.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Mon Jun 11 2012 Paulo Andrade <pcpa@mandriva.com.br> 20110609-3
+ Revision: 804942
- Update to latest release.

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20110609-2
+ Revision: 753978
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20110609-1
+ Revision: 719015
- texlive-mh
- texlive-mh
- texlive-mh
- texlive-mh

