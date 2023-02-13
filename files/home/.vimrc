set nocompatible

set backspace=indent,eol,start

set smartindent
"filetype on
"filetype plugin on
"filetype indent on
set tabstop=2
set shiftwidth=2
set expandtab

syntax on

set nu
set relativenumber

set hlsearch
set incsearch
set showmatch
set ignorecase
set smartcase

set ruler
"set cursorline
set visualbell
set showcmd

set encoding=utf-8
"inoremap " ""<left>
"inoremap ' ''<left>
"inoremap ( ()<left>
"inoremap {<CR> {<CR>}<ESC>O
"inoremap {;<CR> {<CR>};<ESC>O
"inoremap [ []<left>
nnoremap <CR> :noh<CR>

colorscheme slate
