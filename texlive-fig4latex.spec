%global tl_name fig4latex
%global tl_revision 26313

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.2
Release:	%{tl_revision}.1
Summary:	Management of figures for large LaTeX documents
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/fig4latex
License:	gpl3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fig4latex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fig4latex.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Requires:	texlive(fig4latex.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Fig4LaTeX simplifies management of the figures in a large LaTeX
document. Fig4LaTeX is appropriate for projects that include figures
with graphics created by XFig -- in particular, graphics which use the
combined PS/LaTeX (or PDF/LaTeX) export method. An example document
(with its output) is provided.

