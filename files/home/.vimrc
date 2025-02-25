set nocompatible
filetype off

set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
Plugin 'VundleVim/Vundle.vim'
call vundle#end()

set backspace=indent,eol,start

set tabstop=2
set shiftwidth=2
set expandtab
set autoindent
set nu
set relativenumber

"set smartindent

syntax on
filetype on

"autocmd FileType yaml setlocal ai ts=2 et nu rnu


set hlsearch
set incsearch
set showmatch
set ignorecase
set smartcase

set ruler
set cursorline
set visualbell
set showcmd

set encoding=utf-8
inoremap " ""<left>
inoremap ' ''<left>
inoremap ( ()<left>
inoremap { {}<left>
inoremap [ []<left>
nnoremap <CR> :noh<CR>

colorscheme slate
