Name:		texlive-fig4latex
Version:	26313
Release:	2
Summary:	Management of figures for large LaTeX documents
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/fig4latex
License:	GPL3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fig4latex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fig4latex.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
ln -sf %{_texmfdistdir}/scripts/fig4latex/fig4latex fig4latex
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
