Name:		texlive-fig4latex
Version:	0.2
Release:	1
Summary:	Management of figures for large LaTeX documents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/fig4latex
License:	GPL3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fig4latex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fig4latex.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Provides:	texlive-fig4latex.bin = %{EVRD}
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Fig4LaTeX simplifies management of the figures in a large LaTeX
document. Fig4LaTeX is appropriate for projects that include
figures with graphics created by XFig -- in particular,
graphics which use the combined PS/LaTeX (or PDF/LaTeX) export
method. An example document (with its output) is provided.

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
