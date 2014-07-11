# revision 26313
# category Package
# catalog-ctan /graphics/fig4latex
# catalog-date 2009-11-09 22:14:03 +0100
# catalog-license gpl3
# catalog-version 0.2
Name:		texlive-fig4latex
Version:	0.2
Release:	9
Summary:	Management of figures for large LaTeX documents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/fig4latex
License:	GPL3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fig4latex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fig4latex.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Provides:	texlive-fig4latex.bin = %{EVRD}

%description
Fig4LaTeX simplifies management of the figures in a large LaTeX
document. Fig4LaTeX is appropriate for projects that include
figures with graphics created by XFig -- in particular,
graphics which use the combined PS/LaTeX (or PDF/LaTeX) export
method. An example document (with its output) is provided.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_bindir}/fig4latex
%{_texmfdistdir}/scripts/fig4latex/fig4latex
%doc %{_texmfdistdir}/doc/support/fig4latex/CHANGES
%doc %{_texmfdistdir}/doc/support/fig4latex/COPYING
%doc %{_texmfdistdir}/doc/support/fig4latex/README
%doc %{_texmfdistdir}/doc/support/fig4latex/example.pdf
%doc %{_texmfdistdir}/doc/support/fig4latex/example.tex
%doc %{_texmfdistdir}/doc/support/fig4latex/figs/div_alg_flowchart.fig
%doc %{_texmfdistdir}/doc/support/fig4latex/figs/if-then_flowchart.fig

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
    ln -sf %{_texmfdistdir}/scripts/fig4latex/fig4latex fig4latex
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}


%changelog
* Tue Aug 07 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.2-3
+ Revision: 812258
- Update to latest release.

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.2-2
+ Revision: 751835
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.2-1
+ Revision: 718432
- texlive-fig4latex
- texlive-fig4latex
- texlive-fig4latex
- texlive-fig4latex

